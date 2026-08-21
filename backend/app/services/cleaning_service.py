import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].mean())

    # Fill missing values in categorical columns
    categorical_columns = df.select_dtypes(exclude=["number"]).columns

    for column in categorical_columns:
        df[column] = df[column].fillna("Unknown")

    return df