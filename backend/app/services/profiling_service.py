import pandas as pd
from pandas.api.types import is_string_dtype

def profile_dataset(df: pd.DataFrame):
    """
    Read a CSV file and return basic dataset profile.
    """

    rows, columns = df.shape

    missing_values = int(
        df.isnull().sum().sum()
    )

    duplicate_rows = int(
        df.duplicated().sum()
    )

    numeric_columns = (
        df.select_dtypes(include=["number"]).columns.tolist()
    )

    categorical_columns = (
        df.select_dtypes(exclude=["number"]).columns.tolist()
    )
    column_types = (
    df.dtypes
    .astype(str)
    .to_dict()
    )

    memory_usage_kb = round(
    df.memory_usage(deep=True).sum() / 1024,2
    )
    

    date_columns = []

    for column in df.columns:
        if is_string_dtype(df[column]):
            try:
                pd.to_datetime(df[column], errors="raise")
                date_columns.append(column)
            except Exception:
                pass

    return {
    "rows": rows,
    "columns_count": columns,
    "missing_values": missing_values,
    "duplicate_rows": duplicate_rows,
    "numeric_columns": numeric_columns,
    "categorical_columns": categorical_columns,
    "column_types": column_types,
    "memory_usage_kb": memory_usage_kb,
    "date_columns": date_columns,
    "columns": list(df.columns),
    "preview": df.head().to_dict(
        orient="records"
    )
}