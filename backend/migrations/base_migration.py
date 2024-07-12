# Classe Base de Migração com Operações Comuns

from pymongo import MongoClient
from config import Config

class BaseMigration:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client.get_default_database()

    def create_database(self):
        print(Config.MONGO_URI)
        print(self.client.get_default_database())
        """Cria o banco de dados se não existir."""
        if self.db_name not in self.client.list_database_names():
            self.db.command("ping")
            print(f"Banco de dados '{self.db_name}' criado com sucesso.")
        else:
            print(f"Banco de dados '{self.db_name}' já existe.")

    def drop_database(self):
        """Remove o banco de dados."""
        self.client.drop_database(self.db_name)
        print(f"Banco de dados '{self.db_name}' removido com sucesso.")

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
