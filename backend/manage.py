import importlib
import sys
import os
from app import create_app
from datetime import datetime

# Obtenha o diretório atual do script manage.py
current_dir = os.path.dirname(os.path.realpath(__file__))
migrations_dir = os.path.join(current_dir, 'migrations', str(datetime.now().year))

# Adicione o diretório de migrações ao sys.path
sys.path.append(migrations_dir)

app = create_app()

def run_migration(migration_name, direction='up'):
    try:
        # Importe o módulo de migração específico
        migration_module = importlib.import_module(f'migrations.{str(datetime.now().year)}.{migration_name}')

        # Execute a migração na direção especificada
        if direction == 'up':
            migration_module.up()
        elif direction == 'down':
            migration_module.down()
        elif direction == 'run':
            migration_instance = migration_module.InitialSetup()
            migration_instance.run()
        elif direction == 'rollback':
            migration_instance = migration_module.InitialSetup()
            migration_instance.rollback()
        else:
            print("Invalid direction. Use 'up', 'down', 'run' or 'rollback'.")
    except ModuleNotFoundError as e:
        print(f"Módulo não encontrado: {e}")

if __name__ == '__main__':
    migration_name = input("Enter migration name (e.g., 20240705_initial_setup): ")
    direction = input("Enter direction (up, down, run or rollback): ")
    run_migration(migration_name, direction)
