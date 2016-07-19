import requests, time, bottlenose, math, json, os, csv, urllib
from bs4 import BeautifulSoup
from mws import mws
from decimal import Decimal
from random import randint
from app.categories import *
from app_config import *

sids = app.config['MWS_SID'] # replace with your seller id
tokens = app.config['MWS_TOKEN'] # replace with your MWS token
access_key = app.config['MWS_API_KEY'] # replace with your access key
secret_key = app.config['MWS_API_SECRET'] # replace with your secret key
marketplaceid = app.config['AMZ_US']

def get_buy_box_data(asin):
	attempts = 0
	try:
		time.sleep(0.5)
		rand = randint(0,13)
		merchant_id = sids[rand]
		auth_token = tokens[rand]
		x = mws.Products(access_key=access_key, secret_key=secret_key, account_id=merchant_id, auth_token=auth_token)
		report = x.get_lowest_priced_offers_for_asin(marketplaceid=marketplaceid, asin=asin, condition="New", excludeme="False")
		response_data = report.original
		soup = BeautifulSoup(response_data, "lxml")
		total_offers = soup.find('totaloffercount').text if soup.find('totaloffercount') != None else '0'
		total_fba = soup.find('offercount', fulfillmentchannel="Amazon").text if soup.find('offercount', fulfillmentchannel="Amazon") != None else '0'
		feedback_count = 0
		feedback_rating = 0
		amz_on = 0
		if soup.find('offer') == None:
			amz_on = 0
			feedback_count = '0'
			feedback_rating = '0'
		else:
			for x in soup.findAll('offer'):
				temp_rating = x.find('sellerpositivefeedbackrating').text if x.find('sellerpositivefeedbackrating') != None else '0'
				temp_count = x.find('feedbackcount').text if x.find('feedbackcount') != None else '0'
				if x.find('isbuyboxwinner') == None:
					feedback_rating = 'N/A'
					feedback_count = 'N/A'
				elif x.find('isbuyboxwinner').text == 'true':
					feedback_rating = x.find('sellerpositivefeedbackrating').text if x.find('sellerpositivefeedbackrating') != None else '0'
					feedback_count = x.find('feedbackcount').text if x.find('feedbackcount') != None else '0'
				if temp_rating == '91.0' and temp_count == '387':
					amz_on = 1
					feedback_rating = 'AMZ'
					feedback_count = 'AMZ'
		amz_on = 'Y' if amz_on == 1 else 'N'
		return(feedback_count, feedback_rating, total_offers, total_fba, amz_on)
		c.writerow([asin, feedback_count, feedback_rating, total_offers, total_fba, amz_on])
	except urllib.error.HTTPError:
		attempts += 1
		print('http fail: ' + str(attempts))
		time.sleep(attempts*3)
	except KeyboardInterrupt:
		exit()
	except Exception as exception:
		attempts += 1
		print("Error: " + str(exception).partition(":")[0] + " - " + asin + " errored")
		if attempts == 2: pass
