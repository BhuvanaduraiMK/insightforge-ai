import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    missing_values = df.isnull().sum().sum()
    
    print(f'Before cleaning - Missing values: {missing_values}')

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].mean())

    # Fill missing values in categorical columns
    categorical_columns = df.select_dtypes(exclude=["number"]).columns

    for column in categorical_columns:
        df[column] = df[column].fillna("Unknown")
    #count missing values
    missing_values = df.isnull().sum().sum()

    print(f'after cleaning - Missing values: {missing_values}')

    return df