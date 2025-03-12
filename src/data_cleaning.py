import pandas as pd

def to_snake_case(df):
    """
    Standardizes column names by converting them to lowercase and replacing spaces with underscores.
    """
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df

def replace_hyphen(df):
    """
    Standardizes column names by converting them to lowercase and replacing spaces with underscores.
    """
    df.columns = [col.lower().replace("-", "_") for col in df.columns]
    return df

def remove_nans_by_column(df, column_name):
    """
    Removes rows with missing values from the DataFrame.
    """
    return df.dropna(subset=[column_name])

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def fill_nans_mean(df, column_name):
    """
    Fills missing values in a specific column with the mean.
    """
    df[column_name] = df[column_name].fillna(df[column_name].mean())
    return df

def forward_fill_data(df):
    """
    This function applies forward fill (ffill) to fill missing values in the DataFrame.
    """
    return df.ffill()

def convert_to_float(df, column_name):
    """
    Converts a specified column to float format.
    """
    try:
        df[column_name] = df[column_name].astype(float)
    except ValueError as e:
        print(f"Error: Could not convert column '{column_name}' to integer. {e}")
    return df

def convert_to_int(df, column_name):
    """
    Converts a specified column to int format, removes commas.
    """
    try:
        # Remove commas from the column and convert to integers
        df[column_name] = df[column_name].replace({',': ''}, regex=True).astype(int)
    except ValueError as e:
        print(f"Error: Could not convert column '{column_name}' to integer. {e}")
    return df
def remove_outliers(df, column_name):
    """
    Remove outliers
    """
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    mask = (df[column_name] > lower_bound) & (df[column_name] < upper_bound)
    return df[mask]