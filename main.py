import create_reports
from utils.mongo_utils import MongoDB
from utils import json_utils

if __name__ == "__main__":
    counts = json_utils.read_counts(file = "inventory/counts-simple.json")
    MongoDB().insert_counts(counts)

    master = json_utils.read_master(file = "inventory/master-simple.json")
    MongoDB().insert_master(master)

    lba_list = create_reports.create_LBA_report(MongoDB())
    create_reports.create_BA_report(lba_list)
    create_reports.create_aggregated_report(MongoDB(), lba_list)

#    MongoDB().drop_counts()
#    MongoDB().drop_master()