# Classe Base de Migração com Operações Comuns

from pymongo import MongoClient
from app import create_app

class BaseMigration:
    def __init__(self):
        self.app = create_app()
        self.client = MongoClient(self.app.config['MONGO_URI'])
        self.db = self.client[self.app.config['MONGO_DBNAME']]

    def create_collection(self, name):
        self.db.create_collection(name)
        print(f"Collection '{name}' created")

    def drop_collection(self, name):
        self.db.drop_collection(name)
        print(f"Collection '{name}' dropped")

    def add_field(self, collection_name, field_name, default_value):
        self.db[collection_name].update_many({}, {"$set": {field_name: default_value}})
        print(f"Field '{field_name}' added to collection '{collection_name}'")

    def remove_field(self, collection_name, field_name):
        self.db[collection_name].update_many({}, {"$unset": {field_name: ""}})
        print(f"Field '{field_name}' removed from collection '{collection_name}'")

    def update_field(self, collection_name, query, update):
        self.db[collection_name].update_many(query, {"$set": update})
        print(f"Field updated in collection '{collection_name}'")

    def delete_documents(self, collection_name, query):
        self.db[collection_name].delete_many(query)
        print(f"Documents deleted from collection '{collection_name}'")
