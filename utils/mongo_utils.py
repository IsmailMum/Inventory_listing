import pymongo

# Returns MongoDB connection to 'Inventory' database
def create_db_connection():
    return pymongo.MongoClient("mongodb://localhost:27017/")["Inventory"]


# Methods for 'Master' collection
def insert_master(db_connection, elements):
    insert = db_connection["Master"].insert_many(elements)
    return insert.inserted_ids

def remove_master(db_connection, id):
    pass

def find_master(db_connection):
    return list(db_connection['Master'].find())


# Methods for 'Counts' collection
def insert_counts(db_connection, elements):
    insert = db_connection["Counts"].insert_many(elements)
    return insert.inserted_ids


def remove_counts(db_connection, id):
    pass

def find_counts(db_connection):
    return list(db_connection['Counts'].find())