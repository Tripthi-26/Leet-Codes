import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Match 'DIAB1' at the start of the string or preceded by whitespace
    pattern = r'(^|\s)DIAB1'
    
    return patients[patients['conditions'].str.contains(pattern, regex=True, na=False)]