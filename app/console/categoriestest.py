def get_referral_pct(category, binding):
  percentage = {
    # 3D Printed Products 15% - 0 min
    '3d printed products': 12,
    # Amazon Device Accessories: 45% - 1.00 min
    'amazon device accessories': 45,
    # Amazon Kindle: 15% - 0 min
    'amazon kindle': 15,
    # Automotive & Powersports: 12%, 10% for tires and wheels - 1.00 min
    'automotive': 12,
    'automotive and powersports': 12,
    'automotive & powersports': 12,
    # Baby Products (excluding Baby Apparel): 15% - 1.00 min
    'baby products': 15,
    'baby product': 15,
    # Beauty: 15% - 1.00 min
    'beauty': 15,
    # Books: 15% - 0 min
    'books': 15,
    'book': 15,
    # Camera & Photo: 8% - 1.00 min
    'camera & photo': 8,
    'camera': 8,
    # Cell Phone Devices: 8% - 0 min
    'cell phone devices': 8,
    'unlocked cell phones': 8,
    # Clothing & Accessories: 15% - 1.00 min
    'apparel': 15,
    'clothing & accessories': 15,
    'clothing': 15,
    'clothing and accessories': 15,
    'eyewear': 15,
    'glasses': 15,
    # Collectable Coins: 15% <= 250 + 10% <= 1000 + 6% > 1000 - 1.00 min
    'collectible coins': 15,
    # Consumer Electronics: 8% - 1.00 min
    'consumer electronics': 8,
    # Electronics Accessories: 15% <= 100 + 8% > 100 - 1.00 min
    'electronics accessories': 15,
    # Entertainment Collectibles: 20% <= 100 + 10% <= 1000 + 6% > 1000 - 1.00 min
    'entertainment collectibles': 20,
    # Furniture & Decor: 15% - 1.00 min
    'furniture and decor': 15,
    'furniture': 15,
    # Grocery & Gourmet Foods: 15% - 0 min
    'gourmet': 15,
    'grocery': 15,
    # Health & Personal Care (including Personal Care Appliances): 15% - 1.00 min
    'health & personal care': 15,
    'health and personal care': 15,
    'health & beauty': 15,
    'health and beauty': 15,
    # Home & Garden (including Pet Supplies): 15% - 1.00 min
    'home & garden': 15,
    'home and garden': 15,
    'pet supplies': 15,
    'pet products': 15,
    'lawn and patio': 15,
    'lawn & patio': 15,
    'lawn & garden': 15,
    'lawn and garden': 15,
    # Independent Design: 25% - 1.00 mi
    'independent design': 25,
    # Industrial & Scientific (including Food Service and Janitorial & Sanitation): 12% - 1.00 min
    'industrial & scientific': 12,
    'biss': 12,
    # Jewelry: 20% - 2.00 min
    'jewelry': 20,
    # Kitchen: 15% - 1.00 min
    'kitchen': 15,
    # Luggage & Travel Accessories: 15% - 1.00 min
    'luggage & travel accessories': 15,
    # Major Appliances: 15% <= 300 + 8% > 300 - 1.00 min
    'major appliances': 15,
    'appliances': 15,
    # Music: 15% - 0 min
    'music': 15,
    # Musical Instruments: 15% - 1.00 min
    'musical instruments': 15,
    'musical instrument': 15,
    # Office Products: 15% - 1.00 min
    'office products': 15,
    'office product': 15,
    'office': 15,
    # Outdoors: 15% - 1.00 min
    'outdoors': 15,
    # Personal Computers: 6% - 1.00 min
    'personal computers': 6,
    # Shoes, Handbags and Sunglasses: 15% - 1.00 min
    'shoes, handbags and sunglasses': 15,
    # Software & Computer/Video Games: 15% - 0 min
    'software & computer/video games': 15,
    'mac games': 15,
    'pc games': 15,
    'software': 15,
    'pc game downloads': 15,
    # Sports: 15% - 1.00 min
    'sports': 15,
    'sports and outdoors': 15,
    # Sports Collectibles: 20% <= 100 + 10% <= 1000 + 6% > 1000 - 0 min
    'sports collectibles': 20,
    # Tools & Home Improvement: 15%, 12% for base equipment power tools - 1.00 min
    'tools & home improvement': 15,
    # Toys & Games: 15% - 1.00 min
    'toys & games': 15,
    'toys': 15,
    'toy': 15,
    'board game': 15,
    'games': 15,
    'game': 15,
    # Video & DVD: 15% - 0 min
    'video & dvd': 15,
    'video and dvd': 15,
    'cd': 15,
    'cd-rom': 15,
    'dvd': 15,
    'video dvd': 15,
    'dvd video': 15,
    'blu-ray': 15,
    'blue ray': 15,
    # Video Games: 15% - 0 min
    'video games': 15,
    'video game': 15,
    # Video Game Consoles: 8% - 0 min
    'video game consoles': 8,
    'console': 8,
    # Watches: 15% - 2.00 min
    'watches': 15,
    # Everything Else: 15% - 0 min
    'misc.': 15,
    'misc': 15,
    'everything else': 15,
  };
  return(percentage.get(category.lower(), percentage.get(binding.lower(), 15)))

def get_minimum_fee(category, binding):
  minimum_fee = {
    # Amazon Device Accessories: 45% - 1.00 min
    'amazon device accessories': 1,
    # Automotive & Powersports: 12%, 10% for tires and wheels - 1.00 min
    'automotive': 1,
    'automotive and powersports': 1,
    'automotive & powersports': 1,
    # Baby Products (excluding Baby Apparel): 15% - 1.00 min
    'baby products': 1,
    'baby product': 1,
    # Beauty: 15% - 1.00 min
    'beauty': 1,
    # Camera & Photo: 8% - 1.00 min
    'camera & photo': 1,
    'camera': 1,
    # Clothing & Accessories: 15% - 1.00 min
    'apparel': 1,
    'clothing & accessories': 1,
    'clothing': 1,
    'clothing and accessories': 1,
    'eyewear': 1,
    'glasses': 1,
    # Collectable Coins: 15% <= 250 + 10% <= 1000 + 6% > 1000 - 1.00 min
    'collectible coins': 1,
    # Consumer Electronics: 8% - 1.00 min
    'consumer electronics': 1,
    # Electronics Accessories: 15% <= 100 + 8% > 100 - 1.00 min
    'electronics accessories': 1,
    # Entertainment Collectibles: 20% <= 100 + 10% <= 1000 + 6% > 1000 - 1.00 min
    'entertainment collectibles': 1,
    # Furniture & Decor: 15% - 1.00 min
    'furniture and decor': 1,
    'furniture': 1,
    # Health & Personal Care (including Personal Care Appliances): 15% - 1.00 min
    'health & personal care': 1,
    'health and personal care': 1,
    'health & beauty': 1,
    'health and beauty': 1,
    # Home & Garden (including Pet Supplies): 15% - 1.00 min
    'home & garden': 1,
    'home and garden': 1,
    'pet supplies': 1,
    'pet products': 1,
    'lawn and patio': 1,
    'lawn & patio': 1,
    'lawn & garden': 1,
    'lawn and garden': 15,
    # Independent Design: 25% - 1.00 mi
    'independent design': 1,
    # Industrial & Scientific (including Food Service and Janitorial & Sanitation): 12% - 1.00 min
    'industrial & scientific': 1,
    'biss': 1,
    # Jewelry: 20% - 2.00 min
    'jewelry': 2,
    # Kitchen: 15% - 1.00 min
    'kitchen': 1,
    # Luggage & Travel Accessories: 15% - 1.00 min
    'luggage & travel accessories': 1,
    # Major Appliances: 15% <= 300 + 8% > 300 - 1.00 min
    'major appliances': 1,
    'appliances': 1,
    # Musical Instruments: 15% - 1.00 min
    'musical instruments': 1,
    'musical instrument': 1,
    # Office Products: 15% - 1.00 min
    'office products': 1,
    'office product': 1,
    'office': 1,
    # Outdoors: 15% - 1.00 min
    'outdoors': 1,
    # Personal Computers: 6% - 1.00 min
    'personal computers': 1,
    # Shoes, Handbags and Sunglasses: 15% - 1.00 min
    'shoes, handbags and sunglasses': 1,
    # Sports: 15% - 1.00 min
    'sports': 1,
    'sports and outdoors': 1,
    # Tools & Home Improvement: 15%, 12% for base equipment power tools - 1.00 min
    'tools & home improvement': 1,
    # Toys & Games: 15% - 1.00 min
    'toys & games': 1,
    'toys': 1,
    'toy': 1,
    'board game': 1,
    'games': 1,
    'game': 1,
    # Watches: 15% - 2.00 min
    'watches': 2,
  };
  return(minimum_fee.get(category.lower(), minimum_fee.get(binding.lower(), 0)))

def get_variable_closing_fee(category, binding):
  variable_closing_fee = {
    'books': 1.35,
    'book': 1.35,
    'video & dvd': 1.35,
    'video and dvd': 1.35,
    'cd': 1.35,
    'cd-rom': 1.35,
    'dvd': 1.35,
    'video dvd': 1.35,
    'dvd video': 1.35,
    'blu-ray': 1.35,
    'blue ray': 1.35,
    'music': 1.35,
    'software & computer/video games': 1.35,
    'mac games': 1.35,
    'pc games': 1.35,
    'software': 1.35,
    'pc game downloads': 1.35,
    'video games': 1.35,
    'video game': 1.35,
    'video game consoles': 1.35,
    'video game console': 1.35,
    'console': 1.35,
  };
  return(variable_closing_fee.get(category.lower(), variable_closing_fee.get(binding.lower(), 0)))