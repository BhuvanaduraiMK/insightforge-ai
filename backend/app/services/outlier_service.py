import pandas as pd

def detect_outliers(df:pd.DataFrame):
    """
    Detect Outliers using the IQR method
    """

    results = []

    numeric_df = df.select_dtypes(include =["number"])

    for column in numeric_df.columns:
        if numeric_df[column].nunique() <= 2:
            continue

        q1 = numeric_df[column].quantile(0.25)
        q3 = numeric_df[column].quantile(0.75)
        iqr = q3-q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outlier_count = (
            (numeric_df[column] < lower_bound) |
            (numeric_df[column] > upper_bound)
        ).sum()

        if outlier_count > 0:
            results.append(
                {
                "column": column,
                "outlier_count": int(outlier_count)
            }
            )
                                         

    return results