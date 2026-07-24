import pandas as pd

def correlation_analysis(df: pd.DataFrame):
    """
    Perform correlation analysis on a dataset.
    """

    numeric_df = df.select_dtypes(include=["number"])

    correlation_matrix = numeric_df.corr(numeric_only=True)

    results = []

    for i in range(len(correlation_matrix.columns)):
        for j in range(i + 1, len(correlation_matrix.columns)):

            column_1 = correlation_matrix.columns[i]
            column_2 = correlation_matrix.columns[j]

            correlation = round(
                correlation_matrix.iloc[i, j],
                2
            )

            if correlation >= 0.80:
                strength = "Very Strong Positive"

            elif correlation >= 0.60:
                strength = "Strong Positive"

            elif correlation >= 0.50:
                strength = "Moderate Positive"

            elif correlation <= -0.80:
                strength = "Very Strong Negative"

            elif correlation <= -0.60:
                strength = "Strong Negative"

            else:
                strength = "Moderate Negative"

            if abs(correlation) >= 0.5:
                results.append(
                    {
                    "column_1": column_1,
                    "column_2": column_2,
                    "correlation": correlation,
                    "strength": strength
                }
)

    return results