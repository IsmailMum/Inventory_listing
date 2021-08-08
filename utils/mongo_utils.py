import pymongo


class mongoDB():
    def __init__ (self, database = 'Inventory'):
    #TODO: Catch connection errors
        self.connection = pymongo.MongoClient("mongodb://localhost:27016/")
        self.db = self.connection[database]

    # Methods for 'Master' collection
    def insert_master(self, elements):
        insert = self.db["Master"].insert_many(elements)
        return insert.inserted_ids

    def find_master(self):
        return list(self.db['Master'].find())

    # Methods for 'Counts' collection
    def insert_counts(self, elements):
        insert = self.db["Counts"].insert_many(elements)
        return insert.inserted_ids

    def find_counts(self):
        return list(self.db['Counts'].find())

    def __del__(self):
        self.connection.close()
        print("db connection closed..")


# Returns MongoDB connection to 'Inventory' database
def create_db_connection():
    return pymongo.MongoClient("mongodb://localhost:27017/")["Inventory"]


# Methods for 'Master' collection
def insert_master(db_connection, elements):
#    inventory_db = db_connection["Inventory"]
    insert = db_connection["Master"].insert_many(elements)
    return insert.inserted_ids

def remove_master(db_connection, id):
    pass

def find_master(db_connection):
    return list(db_connection['Master'].find())


# Methods for 'Counts' collection
def insert_counts(db_connection, elements):
#    inventory_db = db_connection["Inventory"]
    insert = db_connection["Counts"].insert_many(elements)
    return insert.inserted_ids


def remove_counts(db_connection, id):
    pass

def find_counts(db_connection):
    return list(db_connection['Counts'].find())