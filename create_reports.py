import utils.json_utils as json_utils
from utils.mongo_utils import MongoDB


def create_LBA_list(db_connection):
    pass

def create_LBA_report(db: MongoDB, report_file = 'reports/location_barcode_amount.txt'):
    counts = db.find_counts()
    location_barcode_amount = list()

    with open(report_file, 'w') as file :
        file.write("location;barcode;amount\n")

        for location in counts:
            for content in location['completedCounts'][0]['contents']:
                file.write(location['locationCode'] + ";" + content['barcode'] + ";" + str(content['amount']) + "\n")

                location_barcode_amount.append({
                    'location': location['locationCode'],
                    'barcode': content['barcode'],
                    'amount': content['amount'],
                }.copy())

    return location_barcode_amount


def create_BA_report(lba_list, report_file = 'reports/barcode_amount.txt'):
    ba_report = {}

    for item in lba_list:
        ba_report.setdefault(item['barcode'], []).append(item)

    with open(report_file, 'w') as file:
        file.write("barcode;amount\n")
        amount = 0
        for barcode in ba_report:
            for each in ba_report[barcode]:
                amount += each['amount']
            file.write(barcode + ";" + str(amount) + "\n")
            amount = 0

def create_aggregated_report(db: MongoDB, lba_list, report_file= 'reports/aggregated_report.txt'):
    master = db.find_master()

    with open(report_file, 'w') as file:
        file.write("location;barcode;amount;sku;urun adi\n")

        for m in master:
            for lba in lba_list:
                if m['barcode'] == lba['barcode']:
                    file.write(lba['location'] + ";" + lba['barcode'] + ";" + str(lba['amount']) + ";" + m['sku'] + ";" + m["urun adi"] + "\n")