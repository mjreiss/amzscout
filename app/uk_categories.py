def get_referral_pct(category, binding, product_type):
    percentage = {
        # Amazon Device Accessories: 45%
        'amazon device accessories': 45,
        # Amazon Kindle: 15%
        'amazon kindle': 15,
        'amazon ereaders': 15,
        'kindle': 15,
        # Baby Products: 15%
        'baby': 15,
        'baby products': 15,
        'baby product': 15,
        # Beauty: 15%
        'beauty': 15,
        # Beer & Wine
        'beer': 12,
        'wine': 12,
        # Books, Music, Videos, DVDs: 15%
        'books': 15,
        'book': 15,
        'ebook': 15,
        'audio book': 15,
        'video & dvd': 15,
        'video and dvd': 15,
        'cd': 15,
        'cd-rom': 15,
        'dvd': 15,
        'video dvd': 15,
        'dvd video': 15,
        'blu-ray': 15,
        'blue ray': 15,
        # Car & Motorbike: 15%, 10% for tyres
        'automotive': 15,
        'auto_accessory': 15,
        'Automotive Parts and Accessories': 15,
        'tyre': 10,
        'tyres': 10,
        'tires': 10,
        # Clothing & Accessories: 15%
        'apparel': 15,
        'clothing & accessories': 15,
        'clothing': 15,
        'clothing and accessories': 15,
        'clothing_accessories': 15,
        'handbags': 15,
        'sunglasses': 15,
        'eyewear': 15,
        'glasses': 15,
        'shirt': 15,
        'pants': 15,
        'shoes': 15,
        'hat': 15,
        'scarf': 15,
        'socks': 15,
        # Computers: 7%
        'personal computers': 7,
        'personal computer': 7,
        'personal_computer': 7,
        'personal_computers': 7,
        'computers': 7,
        'computer': 7,
        # Consumer Electronics:7%
        'electronics': 7,
        'consumer electronics': 7,
        'ce': 7,
        'headphones': 7,
        'television': 7,
        'camera': 7,
        'camera_digital': 7,
        'phone': 7,
        # Electronics Accessories: 12%
        'electronics accessories': 12,
        'electronics_accessories': 12,
        'wireless accessories': 12,
        'wireless_accessories': 12,
        'wireless phone accessory': 12,
        'wireless_accessory': 12,
        'computer accessories': 12,
        'compuer accessory': 12,
        'computer_accessories': 12,
        'computer_accessory': 12,
        'accessory_or_part_or_supply': 12,
        # DIY & Tools: 12%
        'tools & home improvement': 12,
        'tools': 12,
        'home improvement': 12,
        'diy & tools': 12,
        'tool': 12,
        # Grocery: 15%
        'gourmet': 15,
        'grocery': 15,
        'pantry': 15,
        # Health & Personal Care: 15%
        'health & personal care': 15,
        'health and personal care': 15,
        'health & beauty': 15,
        'health and beauty': 15,
        'personal care': 15,
        'personal_care': 15,
        # Jewelry: 25%
        'jewelry': 25,
        'jewellry': 25,
        'finenecklacebraceletanklet': 25,
        'finering': 25,
        # Kitchen
        'kitchen': 15,
        'home & kitchen': 15,
        # Large Appliances (Not Accessories, Microwaves and Range Hoods): 7%
        'major appliances': 7,
        'major_appliances': 7,
        'major_appliance': 7,
        'appliances': 7,
        'appliance': 7,
        'large appliances': 7,
        'refrigeration_appliance': 7,
        'laundry_appliance': 7,
        'cooking_oven': 7,
        # Musical Instruments: 12%
        'musical instruments': 12,
        'musical instrument': 12,
        'brass_and_woodwind_instruments': 12,
        'sound_and_recording_equipment': 12,
        'guitars': 12,
        # Software & Computer/Video Games: 15%
        'software & computer/video games': 15,
        'mac games': 15,
        'pc games': 15,
        'software': 15,
        'pc game downloads': 15,
        # Spirits: 10%
        'spirits': 10,
        # Sports: 15%
        'sports': 15,
        'sports and outdoors': 15,
        'sporting goods': 15,
        'sporting_goods': 15,
        # Video Games: 15% - 0 min
        'video game': 15,
        # Video Game Consoles: 8% - 0 min
        'video game consoles': 8,
        'console': 8,
        # Watches: 15%
        'watches': 15,
        'watch': 15,
        # Everything Else: 15% - 0 min
        'misc.': 15,
        'misc': 15,
        'everything else': 15,
    };

    return(
        percentage.get(product_type.lower(), 
        percentage.get(category.lower(), 
        percentage.get(binding.lower(),
        15)))
    )

def get_minimum_fee(category, binding, product_type):
    minimum_fee = {
        # Amazon Device Accessories: 45%
        'amazon device accessories': 0.40,
        # Beauty: 15%
        'beauty': 0.40,
        # Car & Motorbike: 15%, 10% for tyres
        'automotive': 0.40,
        'auto_accessory': 0.40,
        'Automotive Parts and Accessories': 0.40,
        'tyre': 0.40,
        'tyres': 0.40,
        'tires': 0.40,
        # Clothing & Accessories: 15%
        'apparel': 0.40,
        'clothing & accessories': 0.40,
        'clothing': 0.40,
        'clothing and accessories': 0.40,
        'clothing_accessories': 0.40,
        'handbags': 0.40,
        'sunglasses': 0.40,
        'eyewear': 0.40,
        'glasses': 0.40,
        'shirt': 0.40,
        'pants': 0.40,
        'shoes': 0.40,
        'hat': 0.40,
        'scarf': 0.40,
        'socks': 0.40,
        # Computers: 7%
        'personal computers': 0.40,
        'personal computer': 0.40,
        'personal_computer': 0.40,
        'personal_computers': 0.40,
        'computers': 0.40,
        'computer': 0.40,
        # Consumer Electronics:7%
        'electronics': 0.40,
        'consumer electronics': 0.40,
        'ce': 0.40,
        'headphones': 0.40,
        'television': 0.40,
        'camera': 0.40,
        'camera_digital': 0.40,
        'phone': 0.40,
        # Electronics Accessories: 12%
        'electronics accessories': 0.40,
        'electronics_accessories': 0.40,
        'wireless accessories': 0.40,
        'wireless_accessories': 0.40,
        'wireless phone accessory': 0.40,
        'wireless_accessory': 0.40,
        'computer accessories': 0.40,
        'compuer accessory': 0.40,
        'computer_accessories': 0.40,
        'computer_accessory': 0.40,
        'accessory_or_part_or_supply': 0.40,
        # DIY & Tools: 12%
        'tools & home improvement': 0.40,
        'tools': 0.40,
        'home improvement': 0.40,
        'diy & tools': 0.40,
        'tool': 0.40,
        # Grocery: 15%
        'gourmet': 15,
        'grocery': 15,
        'pantry': 15,
        # Health & Personal Care: 15%
        'health & personal care': 0.40,
        'health and personal care': 0.40,
        'health & beauty': 0.40,
        'health and beauty': 0.40,
        'personal care': 0.40,
        'personal_care': 0.40,
        # Jewelry: 25%
        'jewelry': 1.25,
        'jewellry': 1.25,
        'finenecklacebraceletanklet': 1.25,
        'finering': 1.25,
        # Large Appliances (Not Accessories, Microwaves and Range Hoods): 7%
        'major appliances': 0.40,
        'major_appliances': 0.40,
        'major_appliance': 0.40,
        'appliances': 0.40,
        'appliance': 0.40,
        'large appliances': 0.40,
        'refrigeration_appliance': 0.40,
        'laundry_appliance': 0.40,
        'cooking_oven': 0.40,
        # Musical Instruments: 12%
        'musical instruments': 0.40,
        'musical instrument': 0.40,
        'brass_and_woodwind_instruments': 0.40,
        'sound_and_recording_equipment': 0.40,
        'guitars': 0.40,
        # Sports: 15%
        'sports': 0.40,
        'sports and outdoors': 0.40,
        'sporting goods': 0.40,
        'sporting_goods': 0.40,
        # Watches: 15%
        'watches': 1.25,
        'watch': 1.25,
    };

    return(
        minimum_fee.get(product_type.lower(),
        minimum_fee.get(category.lower(),
        minimum_fee.get(binding.lower(),
        0)))
    )

def get_variable_closing_fee(category, binding, product_type):
    variable_closing_fee = {
        'books': 0.43,
        'book': 0.43,
        'video': 1.15,
        'vhs tape': 1.15,
        'audio cd': 0.24,
        'cd': 0.24,
        'music': 0.24,
        'vinyl': 0.24,
        'dvd': 0.14,
        'video dvd': 0.14,
        'dvd video': 0.14,
        'blu-ray': 0.14,
        'blue ray': 0.14,
    };

    return(
        variable_closing_fee.get(product_type.lower(),
        variable_closing_fee.get(category.lower(),
        variable_closing_fee.get(binding.lower(),
        0)))
    )

def get_is_media(category, binding, product_type):
    is_media = {
        'books': True,
        'book': True,
        'video': True,
        'vhs tape': True,
        'audio cd': True,
        'cd': True,
        'music': True,
        'vinyl': True,
        'dvd': True,
        'video dvd': True,
        'dvd video': True,
        'video & dvd': True,
        'video and dvd': True,
        'blu-ray': True,
        'blue ray': True,
        'cd-rom': True,
        'software & computer/video games': True,
        'mac games': True,
        'pc games': True,
        'software': True,
        'pc game downloads': True,
        'video games': True,
        'video game': True,
        'video game consoles': True,
        'video game console': True,
        'console': True,
    };
    
    return(
        is_media.get(product_type.lower(),
        is_media.get(category.lower(),
        is_media.get(binding.lower(),
        False)))
    )
