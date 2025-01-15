import pandas as pd
import extract_data_to_staging as staging
import transform_data_load_to_dwh as dwh


# Extract tables from the sources to the staging area
# Data is filtered and cleaned during extraction
# Staging area is still a classic normalized database
def extract_tables_to_staging():
    staging.extract_DOCTOR()

# Create general dimensions like DATE and LOCATION
# from data in the staging area
def prepare_dwh_dimensions():
    pass


if __name__ == "__main__":
    
    extract_tables_to_staging()
    