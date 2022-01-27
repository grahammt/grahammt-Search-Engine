"""Insta485 development configuration."""

import pathlib

# URL of the index server
INDEX_API_URL = "http://localhost:8001/api/v1/hits/"

PROJ_DIR = pathlib.Path('search')

DATABASE_FILENAME = PROJ_DIR/'search'/'var'/'index.sqlite3'
