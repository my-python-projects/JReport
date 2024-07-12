from migrations.base_migration import BaseMigration

class InitialSetup(BaseMigration):
    def __init__(self):
        super().__init__()
        self.db_name = 'jreport'

    def run(self):
        self.create_database()
        self.create_collection('users')
        print("'InitialSetup' migration executed successfully.")

    def rollback(self):
        self.drop_collection('users')
        self.drop_database()

        print("'InitialSetup' migration successfully rolled back.")
