import csv, urllib, time
from app.pa_api import *
from app.calc import *
from app.mws_api import *
# get_data(row)

def run_scout(path, result_file, error_file):
    with open(path, "rt", encoding='utf8') as f:
        reader = csv.reader(f)
        header = next(reader)[0]
        # ASIN Scout
        if header.lower() == "asin":
            c = csv.writer(open("app/files/results/" + result_file, "w"))
            e = csv.writer(open("app/files/errors/" + error_file, "w"))
            c.writerow([
                "UPC", "ASIN", "Name", "List Price", "Model", "MPN", "Brand", "Color", "Sales Rank", "Category",
                "Pick & Pack", "Weight Handling", "Order Handling", "30d Storage", "VCF", "FBA Fees", "Referral",
                "Width", "Height", "Length", "Weight", "Total Offers", "New Offers", "FBA Offers", "AMZ on Listing", 
                "Buy Box", "FBA Buy Box?", "BB Feedback Count", "BB Feedback Rating",
                ])
            e.writerow(["ASIN"])
            for row in reader:
                attempts = 0
                while attempts < 4:
                    try:
                        print("ASIN: " + str(row[0]))
                        asin, title, upc, list_price, model, mpn, brand, color, rank, category, pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral, width, height, length, weight, bb_amt, fba_bb, new_offers = get_scout_data(str(row[0]))
                        feedback_count, feedback_rating, total_offers, total_fba, amz_on = get_buy_box_data(str(row[0]))
                        c.writerow([
                            ("*%s" % upc), row[0], title, list_price, model, mpn, brand, color, rank, category,
                            pick_pack, weight_handling, order_handling, thirty_day, vcf, total_fee, referral,
                            width, height, length, weight, total_offers, new_offers, total_fba, amz_on,
                            bb_amt, fba_bb, feedback_count, feedback_rating
                        ])
                        break
                    except urllib.error.HTTPError:
                        attempts += 1
                        print('fail: ' + str(attempts))
                        time.sleep(attempts*3)
                    except KeyboardInterrupt:
                        exit()
                    except Exception as exception:
                        attempts += 1
                        print("Error: " + str(exception).partition(":")[0] + " - " + row[0] + " added to errors.csv")
                        e.writerow(row[0])
                        if attempts == 2: pass

        # UPC Scout
        else:
            c = csv.writer(open("app/files/results/" + result_file, "w"))
            e = csv.writer(open("app/files/errors/" + error_file, "w"))
            c.writerow([
                "UPC", "ASIN", "Name", "List Price", "Model", "MPN", "Brand", "Color", "Sales Rank", "Category",
                "Pick & Pack", "Weight Handling", "Order Handling", "30d Storage", "VCF", "FBA Fees", "Referral",
                "Width", "Height", "Length", "Weight", "Total Offers", "New Offers", "FBA Offers", "AMZ on Listing", 
                "Buy Box", "FBA Buy Box?", "BB Feedback Count", "BB Feedback Rating",
                ])
            e.writerow(["UPC", "Error"])
            count = 1
            for row in reader:
                try:
                    print("UPC: " + str(row[0]))
                    count += 1
                    all_asin = ean_to_asin(str(row[0])) if len(str(row[0])) == 13 else upc_to_asin(str(row[0]))
                    for x in all_asin:
                        attempts = 0
                        while attempts < 4:
                            try:
                                asin, title, upc, list_price, model, mpn, brand, color, rank, category, pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral, width, height, length, weight, bb_amt, fba_bb, new_offers = get_scout_data(x)
                                feedback_count, feedback_rating, total_offers, total_fba, amz_on = get_buy_box_data(x)
                                c.writerow([
                                    ("*%s" % row[0]), asin, title, list_price, model, mpn, brand, color, rank, category,
                                    pick_pack, weight_handling, order_handling, thirty_day, vcf, total_fee, referral,
                                    width, height, length, weight, total_offers, new_offers, total_fba, amz_on,
                                    bb_amt, fba_bb, feedback_count, feedback_rating
                                ])
                                break
                            except urllib.error.HTTPError:
                                attempts += 1
                                print('http fail: ' + str(attempts))
                                time.sleep(attempts*3)
                            except KeyboardInterrupt:
                                exit()
                            except Exception as exception:
                                attempts += 1
                                print("Error: " + str(exception).partition(":")[0] + " - " + row[0] + " added to errors.csv")
                                e.writerow(row[0])
                                if attempts == 2: pass
                except urllib.error.HTTPError:
                    print('UPC to ASIN failed - trying again')
                    time.sleep(1)
                except Exception as exception:
                    print("Error: " + str(exception).partition(":")[0] + " - " + row[0] + " added to errors.csv")
                    e.writerow([row[0], str(exception).partition(":")[0]])
