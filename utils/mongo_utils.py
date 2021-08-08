import pymongo

class MongoDB():
    def __init__ (self, database = 'Inventory'):
    #TODO: Catch connection errors
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.connection[database]

    # Methods for 'Master' collection
    def insert_master(self, elements):
        insert = self.db["Master"].insert_many(elements)
        return insert.inserted_ids

    def find_master(self):
        return list(self.db['Master'].find())

    def drop_master(self):
        return self.db['Master'].drop()

    # Methods for 'Counts' collection
    def insert_counts(self, elements):
        insert = self.db["Counts"].insert_many(elements)
        return insert.inserted_ids

    def find_counts(self):
        return list(self.db['Counts'].find())

    def drop_counts(self):
        return self.db['Counts'].drop()

    def __del__(self):
        self.connection.close()
        print("db connection closed..")
