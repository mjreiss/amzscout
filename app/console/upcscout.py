import csv, urllib, time
from mwstest import *
from calctest import *
# get_data(row)
start_time = time.time() 
i = 0
with open('upc.csv', "rt", encoding='utf8') as f:
    reader = csv.reader(f)
    next(reader, None)
    c = csv.writer(open("files/results/upcresults.csv", "w"))
    e = csv.writer(open("files/results/upcerrors.csv", "w"))
    c.writerow([
        "ASIN", "Name", "UPC", "List Price", "Model", "MPN", "Brand", "Color", "Sales Rank", "Category",
        "Pick & Pack", "Weight Handling", "Order Handling", "30d Storage", "FBA Fees", "VCF", "Referral",
        "Width","Height","Length","Weight",
        "Buy Box", "FBA BB", "New Offers", "FBA Offers", "AMZ on Listing"
        ])
    e.writerow(["ASIN"])
    for row in reader:
        try:
            all_asin = upc_to_asin(str(row[0]))
            for x in all_asin:
                attempts = 0
                while attempts < 4:
                    try:
                        print(x)
                        asin, title, upc, list_price, model, mpn, brand, color, rank, category, pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral, width, height, length, weight, bb_amt, fba_bb, new_offers, fba_count, has_amz = get_scout_data(x)
                        c.writerow([
                            ("*%s" % upc), asin, title, list_price, model, mpn, brand, color, rank, category,
                            pick_pack, weight_handling, order_handling, thirty_day, total_fee, vcf, referral,
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
            
print("--- %s seconds ---" % (time.time() - start_time))