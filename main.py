import pandas as pd
import extract_data


if __name__ == "__main__":
    doctor_df = extract_data.extract_DOCTOR()
    print(doctor_df.info())
    print(doctor_df.head())