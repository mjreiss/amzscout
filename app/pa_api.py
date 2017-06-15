import requests, time, bottlenose, math, urllib, csv
from bs4 import BeautifulSoup
from amazon_scraper import AmazonScraper # https://github.com/adamlwgriffiths/amazon_scraper
from decimal import Decimal
from app.categories import *
from app_config import *

# Amazon scraper + Amazon API wrapper
amazon = AmazonScraper(app.config['AMZ_API_KEY'], app.config['AMZ_API_SECRET'], app.config['AMZ_ASSOCIATE'])
	
# Access Raw Amazon XML Response
amazon_raw = bottlenose.Amazon(app.config['AMZ_API_KEY'], app.config['AMZ_API_SECRET'], app.config['AMZ_ASSOCIATE'])

def upc_to_asin(upc):
	time.sleep(1)
	p = amazon.lookup(ItemId=upc, IdType='UPC', SearchIndex='All')
	if type(p) != list:
		asin = [p.asin]
	else:
		asin = []
		count = 0
		while count <= len(p) - 1:
			asin.append(p[count].asin)
			count += 1
	return(asin)

def ean_to_asin(ean):
	time.sleep(1)
	p = amazon.lookup(ItemId=ean, IdType='EAN', SearchIndex='All')
	if type(p) != list:
		asin = [p.asin]
	else:
		asin = []
		count = 0
		while count <= len(p) - 1:
			asin.append(p[count].asin)
			count += 1
	return(asin)

# part of run_bulk_asin()
def get_raw_data(asin):
	p = amazon.lookup(ItemId=asin, IdType='ASIN', ResponseGroup='Large')
	time.sleep(0.2)
	raw_data = amazon_raw.ItemLookup(ItemId=asin, IdType='ASIN', ResponseGroup="Large")
	soup = BeautifulSoup(raw_data, "lxml")
	return(p, soup)

def get_attributes(asin):
	# time.sleep(1)
	p = amazon.lookup(ItemId=asin, IdType='ASIN', ResponseGroup='Large')
	raw_data = amazon_raw.ItemLookup(ItemId=asin, IdType='ASIN', ResponseGroup="Large")
	soup = BeautifulSoup(raw_data, "lxml")

	# Product Attributes
	asin = p.asin
	title = p.title
	upc = p.upc
	list_price = p.list_price[0]
	model = p.model
	mpn = p.mpn
	brand = p.brand
	color = p.color
	rank = p.sales_rank
	binding = p.binding
	product_group = soup.find('productgroup').string
	binding = 'Misc.' if binding is None else binding
	product_group = 'Misc.' if product_group is None else product_group
	# Check if Clothing
	is_clothing = False
	if soup.findAll('clothingsize'):
		is_clothing = True
	for node in soup.findAll('name'):
		if 'Clothing' in node:
			is_clothing = True

	# Product Dimensions
	search_dims = [
		'PackageDimensions.Width',
		'PackageDimensions.Height',
		'PackageDimensions.Length',
		'PackageDimensions.Weight',
	]
	raw_dims = p.get_attributes(search_dims)
	width = Decimal(raw_dims['PackageDimensions.Width'])/Decimal(100.0) if 'PackageDimensions.Width' in raw_dims else 0
	height = Decimal(raw_dims['PackageDimensions.Height'])/Decimal(100.0) if 'PackageDimensions.Height' in raw_dims else 0
	length = Decimal(raw_dims['PackageDimensions.Length'])/Decimal(100.0) if 'PackageDimensions.Length' in raw_dims else 0
	weight = Decimal(raw_dims['PackageDimensions.Weight'])/Decimal(100.0) if 'PackageDimensions.Weight' in raw_dims else 0

	return(
		asin,
		title,
		upc,
		list_price,
		model,
		mpn,
		brand,
		color,
		rank,
		product_group,
		binding,
		is_clothing,
		str(width),
		str(height),
		str(length),
		str(weight)
	)

def get_commission(asin, category, binding, product_type):
	pct = get_referral_pct(category, binding, product_type)
	minimum = get_minimum_fee(category, binding, product_type)
	vcf = get_variable_closing_fee(category, binding, product_type)
	return((pct/100), minimum, vcf)

def offers_api(asin):
	# time.sleep(1)
	raw_data = amazon_raw.ItemLookup(ItemId=asin, IdType='ASIN', ResponseGroup="Offers")
	soup = BeautifulSoup(raw_data, "lxml")
	amount = "N/A"
	fba = 0
	# Find buy box offer price
	for x in soup.findAll('price'):
		amount = x.find('amount').text if x.find('amount') else 0
		amount = int(amount)/100

	for x in soup.findAll('offersummary'):
		# Total number of new offers
		new_offers = x.find('totalnew').text
		# Find if buy box offer is FBA
		for x in soup.findAll('offerlisting'):
			fba = x.find('iseligibleforprime').text

	return(amount, new_offers, fba)

def offers_scrape(asin):
	new_offers = int(offers_api(asin)[1])
	pages = math.ceil(new_offers / 10)
	index = 0
	fba_count = 0
	amz = 0
	# Find all pages of offers
	while index < (pages):
		time.sleep(0.5)
		# URL for all pages
		url = 'http://www.amazon.com/gp/offer-listing/' + asin + '/ref=olp_f_new?ie=UTF8&f_new=true&overridePriceSuppression=1&startIndex=' + str(index) + '0'
		response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
		soup = BeautifulSoup(response.content, "lxml")

		# Amazon on the listing
		for x in soup.findAll("h3", { "class" : "olpSellerName" }):
			for y in x.findAll("img", { "alt" : "Amazon.com" }):
				amz += 1
		# Total number of FBA offers
		for x in soup.findAll("span", { "class" : "supersaver" }):
			fba_count += 1
		index += 1

	return(amz, fba_count)
