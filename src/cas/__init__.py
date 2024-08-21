# __init__.py

from pathlib import Path

import cas.db

# Define the path to the JSON database
DATABASE_PATH = Path("cas/database/database.json")

# Create an instance of CASDatabase using the specified path
database = cas.db.CASDatabase(database_path=DATABASE_PATH)
