import pandas as pd
import extract_data_to_staging


# Extract tables from the sources to the staging area
# Data is filtered and cleaned during extraction
# Staging area is still a classic normalized database
def extract_tables_to_staging():
    extract_data_to_staging.extract_DOCTOR()


if __name__ == "__main__":
    
    extract_tables_to_staging()
    