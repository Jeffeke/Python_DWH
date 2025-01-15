import pyodbc
import pandas as pd
import time
from sqlalchemy import create_engine

# SQL Server connection
server = "WS-VRAJE-01"
database = "DWHTEST"

engine = create_engine(f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")


def create_location_table():
    pass
    # Query staging.DOCTOR
    # Parse locaties (gewest, land, provincie, postcode)
    # Load naar DWH