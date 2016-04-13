import csv, urllib, time
from app.mws import *
from app.calc import *
# get_data(row)

def run_scout(path, result_file, error_file):
    with open(path, "rt", encoding='utf8') as f:
        reader = csv.reader(f)
        header = next(reader)[0]
        if header.lower() == "asin":
            c = csv.writer(open("app/files/results/" + result_file, "w"))
            e = csv.writer(open("app/files/errors/" + error_file, "w"))
            c.writerow([
                "UPC", "ASIN", "Name", "List Price", "Model", "MPN", "Brand", "Color", "Sales Rank", "Category",
                "Pick & Pack", "Weight Handling", "Order Handling", "30d Storage", "VCF", "FBA Fees", "Referral",
                "Width","Height","Length","Weight",
                "Buy Box", "FBA BB", "New Offers", "FBA Offers", "AMZ on Listing"
                ])
            e.writerow(["ASIN"])
            for row in reader:
                attempts = 0
                while attempts < 5:
                    try:
                        asin, title, upc, list_price, model, mpn, brand, color, rank, category, pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral, width, height, length, weight, bb_amt, fba_bb, new_offers, fba_count, has_amz = init_scout(str(row[0]))
                        c.writerow([
                            ("*%s" % upc), asin, title, list_price, model, mpn, brand, color, rank, category,
                            pick_pack, weight_handling, order_handling, thirty_day, vcf, total_fee, referral,
                            width, height, length, weight,
                            bb_amt, fba_bb, new_offers, fba_count, has_amz
                        ])
                        break
                    except urllib.error.HTTPError:
                        attempts += 1
                        print('fail: ' + str(attempts))
                        time.sleep(attempts*3)
                    except KeyboardInterrupt:
                        exit()

        # UPC Scout
        else:
            c = csv.writer(open("app/files/results/" + result_file, "w"))
            e = csv.writer(open("app/files/errors/" + error_file, "w"))
            c.writerow([
                "UPC", "ASIN", "Name", "List Price", "Model", "MPN", "Brand", "Color", "Sales Rank", "Category",
                "Pick & Pack", "Weight Handling", "Order Handling", "30d Storage", "VCF", "FBA Fees", "Referral",
                "Width","Height","Length","Weight",
                "Buy Box", "FBA BB", "New Offers", "FBA Offers", "AMZ on Listing"
                ])
            e.writerow(["UPC"])
            count = 1
            for row in reader:
                try:
                    print("Line: " + str(count))
                    print("UPC: " + str(row[0]))
                    count += 1
                    all_asin = ean_to_asin(str(row[0])) if len(str(row[0])) == 13 else upc_to_asin(str(row[0]))
                    for x in all_asin:
                        attempts = 0
                        while attempts < 6:
                            try:
                                asin, title, upc, list_price, model, mpn, brand, color, rank, category, pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral, width, height, length, weight, bb_amt, fba_bb, new_offers, fba_count, has_amz = get_scout_data(x)
                                c.writerow([
                                    ("*%s" % upc), asin, title, list_price, model, mpn, brand, color, rank, category,
                                    pick_pack, weight_handling, order_handling, thirty_day, vcf, total_fee, referral,
                                    width, height, length, weight,
                                    bb_amt, fba_bb, new_offers, fba_count, has_amz
                                ])
                                break
                            except urllib.error.HTTPError:
                                attempts += 1
                                print('http fail: ' + str(attempts))
                                time.sleep(attempts*3)
                            except KeyboardInterrupt:
                                exit()
                            except Exception as exception:
                                print("Error: " + str(exception).partition(":")[0] + " - " + ''.join(row) + " added to errors.csv")
                                e.writerow([''.join(row)])
                except urllib.error.HTTPError:
                    print('UPC to ASIN failed - trying again')
                    time.sleep(1)
                except Exception as exception:
                    print("Error: " + str(exception).partition(":")[0] + " - " + ''.join(row) + " added to errors.csv")
                    e.writerow([''.join(row)])
