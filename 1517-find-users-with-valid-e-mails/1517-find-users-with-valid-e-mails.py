import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Regular expression pattern to match valid e-mails
    pattern = '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
    
    # Filter the DataFrame using str.contains with regex=True
    valid_df = users[users['mail'].str.contains(pattern, regex=True, na=False)]
    
    return valid_df