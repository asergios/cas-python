# __init__.py

from pathlib import Path

import cas.db

BASE_DIR = Path(__file__).resolve().parent

# Define the path to the JSON database
DATABASE_PATH = BASE_DIR / "database" / "database.json"

# Create an instance of CASDatabase using the specified path
database = cas.db.CASDatabase(database_path=DATABASE_PATH)
