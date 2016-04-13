import datetime, json, math, csv, time
from decimal import Decimal, ROUND_UP
from numpy import median
from app.mws import *

pick_pack_const = {
    'standard': Decimal(1.06),
    'small_oversize': Decimal(4.09),
    'medium_oversize': Decimal(5.20),
    'large_oversize': Decimal(8.40),
    'special_oversize': Decimal(10.53),
}

# Function for single ASIN lookup in app - app.py
def lookup_asin_data(asin):
    asin, title, upc, list_price, model, mpn, brand, color, rank, category, binding, is_clothing, width, height, length, weight = get_attributes(asin)
    commission, minimum, vcf = get_commission(asin)
    is_media = True if vcf else False
    bb_amt, new_offers, fba = offers_api(asin)
    fba = 'Y' if fba == '1' else 'N'
    has_amz, fba_count = offers_scrape(asin)
    has_amz = 'Y' if has_amz >= 1 else 'N'
    if any(x == '0' for x in (width, height, length, weight)):
        result = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
        vcf = 'N/A'
    else:
        result = calculate_fees(asin, width, height, length, weight, 100.0, commission, is_clothing, is_media)

    final = {
        'asin': asin,
        'title': title,
        'upc': upc,
        'list_price': list_price,
        'model': model,
        'mpn': mpn,
        'brand': brand,
        'color': color,
        'rank': rank,
        'category': category,
        'binding': binding,
        'pick_pack': result[0],
        'weight_handling': result[1],
        'order_handling': result[2],
        '30d': result[3],
        'fees': result[4],
        'vcf': vcf,
        'referral': commission,
        'total': result[5],
        'width': width,
        'height': height,
        'length': length,
        'weight': weight,
        'bb_amt': bb_amt,
        'fba': fba,
        'new_offers': new_offers,
        'fba_count': fba_count,
        'has_amz': has_amz,
    }
    return(final)

# Function for multiple ASINs in csv - read.py
def get_scout_data(asin):
    time.sleep(1)
    asin, title, upc, list_price, model, mpn, brand, color, rank, category, binding, is_clothing, width, height, length, weight = get_attributes(asin)
    time.sleep(1)
    commission, minimum, vcf = get_commission(asin)
    is_media = True if vcf else False
    bb_amt, new_offers, fba = offers_api(asin)
    fba = 'Y' if fba == '1' else 'N'
    has_amz, fba_count = offers_scrape(asin)
    has_amz = 'Y' if has_amz >= 1 else 'N'
    if any(x == '0' for x in (width, height, length, weight)):
        result = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
        vcf = 'N/A'
    else:
        result = calculate_fees(asin, width, height, length, weight, 100.0, commission, is_clothing, is_media)

    return(
        asin,
        title,
        upc,list_price,
        model,
        mpn,
        brand,
        color,
        rank,
        category,
        result[0],
        result[1],
        result[2],
        result[3],
        result[4],
        vcf,
        commission,
        width,
        height,
        length,
        weight,
        bb_amt,
        fba,
        new_offers,
        fba_count,
        has_amz
        )

def get_30_day(standard_or_oversize, cubic_foot):
    month = datetime.datetime.now().month
    if month <= 9:
        if standard_or_oversize == 'standard':
            return Decimal(0.54) * Decimal(cubic_foot)
        return Decimal(0.43) * Decimal(cubic_foot)
    else:
        if standard_or_oversize == 'standard':
            return Decimal(0.72) * Decimal(cubic_foot)
        return Decimal(0.57) * Decimal(cubic_foot)

def get_standard_or_oversize(length, width, height, weight):
    # Determine if object is standard size or oversized
    if any([(weight > 20),
            (max(length, width, height) > 18),
            (min(length, width, height) > 8),
            (median([length, width, height]) > 14)]):
        return 'oversize'
    return 'standard'

def get_dimensional_weight(length, width, height):
    dw = (height * length * width) / Decimal(166.0)
    return Decimal(dw)


def get_girth_and_length(length, width, height):
    gl = max(length, width, height) + (median([length, width, height]) * 2) + (min(length, width, height) * 2)

    return round(Decimal(gl), 1)

def get_cubic_foot(length, width, height):
    return (length * width * height) / Decimal(1728.0)

def get_weight_handling(product_tier, outbound, is_media=False):
    outbound = math.ceil(outbound)

    if product_tier == 'small_standard':
        return Decimal(0.5)

    if product_tier == 'large_standard':
        if outbound <= 1:
            if is_media:
                return Decimal(0.85)
            return Decimal(0.96)

        if is_media:
            if outbound <= 2:
                return Decimal(1.24)
            return Decimal(1.24) + (outbound - 2) * Decimal(0.41)

        if outbound <= 2:
            return Decimal(1.95)
        return Decimal(1.95) + (outbound - 2) * Decimal(0.39)

    if product_tier == 'special_oversize':
        if outbound <= 90:
            return Decimal(124.58)
        return Decimal(124.58) + (outbound - 90) * Decimal(0.80)

    if product_tier == 'large_oversize':
        if outbound <= 90:
            return Decimal(63.98)
        return Decimal(63.98) + (outbound - 90) * Decimal(0.80)

    if product_tier == 'medium_oversize':
        if outbound <= 2:
            return Decimal(2.73)
        return Decimal(2.73) + (outbound - 2) * Decimal(0.39)

    if outbound <= 2:
        return Decimal(2.06)
    return Decimal(2.06) + (outbound - 2) * Decimal(0.39)


def calculate_fees(asin, length, width, height, weight, price=0.0, commission=0.15, is_clothing=False, is_media=False):
    # Calculate the FBA fees for the given variables
    length, width, height, weight = Decimal(length), Decimal(width), Decimal(height), Decimal(weight)
    price = Decimal(price)
    commission = Decimal(commission)
    dimensional_weight = get_dimensional_weight(length, width, height)
    girth_length = get_girth_and_length(length, width, height)

    standard_or_oversize = get_standard_or_oversize(length, width, height, weight)

    cubic_foot = get_cubic_foot(length, width, height)

    if standard_or_oversize == 'standard':
        if is_media:
            fee_weight = Decimal(0.875)
        else:
            fee_weight = Decimal(0.75)

        if all(
            [
                (fee_weight >= weight),
                (max(length, width, height) <= 15),
                (min(length, width, height) <= 0.75),
                (median([length, width, height]) <= 12)
            ]
        ):
            product_tier = 'small_standard'
        else:
            product_tier = 'large_standard'
    else:
        if any(
            [
                (girth_length > 165),
                (weight > 150),
                (max(length, width, height) > 108),
             ]
        ):
            product_tier = 'special_oversize'
        elif girth_length > 130:
            product_tier = 'large_oversize'
        elif any(
            [
                (weight > 70),
                (max(length, width, height) > 60),
                (median([length, width, height]) > 30),
            ]
        ):
            product_tier = 'medium_oversize'
        else:
            product_tier = 'small_oversize'

    if is_media:
        outbound = weight + Decimal(0.125)
    else:
        if standard_or_oversize == 'standard':
            if weight <= 1:
                outbound = weight + Decimal(0.25)
            else:
                outbound = max(weight, dimensional_weight) + Decimal(0.25)
        else:
            if product_tier == 'special_oversize':
                outbound = weight + 1
            else:
                outbound = max(weight, dimensional_weight) + 1

    if is_media or standard_or_oversize == 'oversize':
        order_handling = Decimal(0.00)
    else:
        order_handling = Decimal(1.00)

    pick_pack = pick_pack_const.get(standard_or_oversize, pick_pack_const.get(product_tier))

    if is_clothing:
        pick_pack += Decimal(0.40)

    weight_handling = round(get_weight_handling(product_tier, outbound, is_media), 2)

    thirty_day = get_30_day(standard_or_oversize, cubic_foot)

    fba_fees = Decimal(pick_pack) + Decimal(weight_handling) + Decimal(thirty_day) + Decimal(order_handling)

    # Add the referral fees if we know how much we plan to sell the product for
    minimum, vcf = get_commission(asin)[1:3]
    referral_fee = round(price * commission, 2)
    if minimum:
        referral_fee = Decimal(minimum)
    total = fba_fees + referral_fee + Decimal(vcf)

    return(
        str(round(pick_pack, 2)),
        str(round(weight_handling, 2)),
        str(round(order_handling, 2)),
        str(round(thirty_day, 2)),
        str(round(fba_fees, 2)),
        str(round(total, 2))
    )