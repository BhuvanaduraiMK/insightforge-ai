import os

import matplotlib.pyplot as plt
import pandas as pd


def generate_histogram(df: pd.DataFrame):
    """
    Generate histogram for the first numeric column.
    """

    numeric_columns = df.select_dtypes(include=["number"]).columns

    if len(numeric_columns) == 0:
        return None

    chart_paths = []

    for column in numeric_columns:
        plt.figure(figsize=(8, 5))

        plt.hist(df[column], bins=10)

        plt.title(f"{column} Distribution")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        os.makedirs("charts", exist_ok=True)

        chart_path = f"charts/{column}_histogram.png"

        plt.savefig(chart_path)

        plt.close()

        chart_paths.append(chart_path)

    return chart_path