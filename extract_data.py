import pyodbc
import pandas as pd

conn = pyodbc.connect("DSN=MACSYS;UID=VRJ;PWD=jv321")

gender_mapping = {
    "0": "Vrouw",
    "1": "Man",
    "9": "Onbekend"
}

language_mapping = {
    "D": "Duits",
    "E": "Engels",
    "F": "Frans",
    "N": "Nederlands"
}

def extract_DOCTOR():

    query = ("""SELECT 
                    GHNR05,
                    GHWP05, 
                    GHNM05,
                    GHVN05,
                    DPGESLACHT,
                    GHAD05,
                    TAKD05,
                    OKNAAM
                FROM DOKTER
                LEFT JOIN DOKPRM AS DP ON GHNR05 = DP.DPGHNR
                LEFT JOIN (grpdok LEFT JOIN grpdok2 ON okgpnr = k2gpnr) ON ghnr05 = k2ghnr""")
    
    # Define column datatypes while loading
    dtype_dict = {
        "GHNR05": int,           
        "GHWP05": str,           
        "GHNM05": str,           
        "GHVN05": str,           
        "DPGESLACHT": str,        
        "GHAD05": str,           
        "TAKD05": str,
        "OKNAAM": str            
    }

    df = pd.read_sql(query, conn, dtype=dtype_dict)

    # Inital transformation for data staging
    column_mapping = {
        "GHNR05": "id",
        "GHWP05": "city",
        "GHNM05": "name",
        "GHVN05": "first_name",
        "DPGESLACHT": "gender",
        "GHAD05": "address",
        "TAKD05": "language",
        "OKNAAM": "group_practice_name"
    }

    # Rename columns
    df.rename(columns=column_mapping, inplace=True) 

    #Preliminary transformations
    df["gender"] = df["gender"].map(gender_mapping).fillna("Onbekend")  # Make gender codes verbose
    df["language"] = df["language"].map(language_mapping).fillna("Onbekend")  # Make language codes verbose



    return df





