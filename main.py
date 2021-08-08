import create_reports
from utils import mongo_utils, json_utils

#Read counts data and insert to 'Inventory' database
counts = json_utils.read_counts(file = "inventory/counts.json")
mongo_utils.insert_counts(mongo_utils.create_db_connection(), counts)

#Read master data and insert to 'Inventory' database
master = json_utils.read_master(file = "inventory/master.json")
mongo_utils.insert_master(mongo_utils.create_db_connection(), master)

#Create report files.
lba_list = create_reports.create_LBA_report(mongo_utils.create_db_connection())
create_reports.create_BA_report(lba_list)
create_reports.create_aggregated_report(mongo_utils.create_db_connection(), lba_list)
