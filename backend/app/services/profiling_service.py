import pandas as pd


def profile_dataset(file_path: str):
    """
    Read a CSV file and return basic dataset profile.
    """

    df = pd.read_csv(file_path)

    rows, columns = df.shape

    missing_values = int(
        df.isnull().sum().sum()
    )

    duplicate_rows = int(
        df.duplicated().sum()
    )

    return {
        "rows": rows,
        "columns_count": columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "columns": list(df.columns),
        "preview": df.head().to_dict(
            orient="records"
        )
    }