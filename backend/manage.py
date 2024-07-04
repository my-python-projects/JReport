# Script de Gerenciamento de Migrações

import importlib
from app import create_app

app = create_app()

def run_migration(migration, direction='up'):
    migration_module = importlib.import_module(f'migrations.{migration}')
    migration_class = getattr(migration_module, migration)
    migration_instance = migration_class()
    
    if direction == 'up':
        migration_instance.up()
    elif direction == 'down':
        migration_instance.down()
    else:
        print("Invalid direction. Use 'up' or 'down'.")

if __name__ == '__main__':
    migration_name = input("Enter migration name (e.g., Migration1): ")
    direction = input("Enter direction (up or down): ")
    run_migration(migration_name, direction)
