from pymongo import MongoClient
from config import CONNECTION_STRING
from config import DATABASE


class Database:  # Wraps all Mongo db methods

    def __init__(self):
        self.connection_string = CONNECTION_STRING
        self.db = {}
        self.client = {}

    def connect_to_database(self):  # Connects to clusters
        """Makes connection to Mongo clusters"""
        self.client = MongoClient(self.connection_string)
        self.db = self.client[DATABASE]

    def get_instance_of_database(self):  # Returns already initialed db object
        """Returns a instance of mongo db connection"""
        return self.db

    def insert_data(self, data_entity, collection):  # Insert a document in given collection
        """Insert a single document in projects database
        :type data_entity: object
        """

        try:
            self.db[collection].insert_one(data_entity.__dict__)
        except:
            self.db[collection].insert_one(data_entity)

    def get_one(self, search_for, collection):  # Get one document by given search criteria
        """Get one document by search criteria from projects database"""
        return self.db[collection].find_one(search_for)

    def list_all_documents(self, collection):  # List all documents in database
        """Return all documents in projects database"""
        return self.db[collection].find()

    def find(self, search_for, collection):  # Search for documents by given criteria
        """Return all documents in projects database"""
        return self.db[collection].find(search_for)
