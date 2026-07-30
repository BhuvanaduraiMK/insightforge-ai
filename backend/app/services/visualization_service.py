import os

import matplotlib.pyplot as plt
import pandas as pd

#histograms
def generate_histogram(df: pd.DataFrame):
    """
    Generate histogram for the first numeric column.
    """

    numeric_columns = df.select_dtypes(include=["number"]).columns

    if len(numeric_columns) == 0:
        return None

    chart_paths = []

    for column in numeric_columns:
        if df[column].nunique() <= 2:
                    continue

        plt.figure(figsize=(10, 6))

        plt.hist(df[column], bins=10,color="steelblue",edgecolor="black",alpha=0.8)

        plt.title(f"{column} Distribution histogram")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.grid(axis = "y", linestyle = "--",alpha = 0.5)

        os.makedirs("charts/histogram", exist_ok=True)

        chart_path = f"charts/histogram/{column}_histogram.png"

        plt.savefig(chart_path, dpi = 300, bbox_inches = "tight")

        plt.close()

        chart_paths.append(chart_path)

    return chart_path

#bar chart
def generate_bar_charts(df: pd.DataFrame):
    """
    Generate bar charts for categorical columns.
    """

    categorical_columns = df.select_dtypes(exclude=["number"]).columns

    if len(categorical_columns) == 0:
        return None

    chart_paths = []

    for column in categorical_columns:    
        if df[column].nunique() > 20:
            continue

        plt.figure(figsize=(8, 5))

        value_counts = df[column].value_counts()

        plt.bar(
            value_counts.index.astype(str),
            value_counts.values,
            color="cornflowerblue",
            edgecolor="black"
        )

        plt.title(f"{column} Distribution Bar chart")
        plt.xlabel(column)
        plt.ylabel("Count")

        plt.grid(axis = "y", linestyle = "--", alpha = 0.5)

        plt.xticks(rotation=45)

        os.makedirs("charts/bar", exist_ok=True)

        chart_path = f"charts/bar/{column}_bar_chart.png"

        plt.tight_layout()

        plt.savefig(chart_path, dpi = 300, bbox_inches = "tight")

        plt.close()

        chart_paths.append(chart_path)

    if len(chart_paths) > 0:
            return chart_paths
    return None 

#box plot
def generate_boxplot(df:pd.DataFrame):
    """
    Generate boxplot for numeric columns.
    """
    numeric_columns = df.select_dtypes(include = ["number"]).columns

    if len(numeric_columns) == 0:
        return None

    chart_paths = []

    for column in numeric_columns:
        if df[column].nunique() <= 2:
            continue

        plt.figure(figsize = (8,6))
        plt.boxplot(df[column].dropna(),
                    patch_artist = True,
                    boxprops = dict(facecolor = "lightgreen", color = "black"),
                    medianprops = dict(color = "red", linewidth = 2),
                    whiskerprops = dict(color = "black"),
                    capprops = dict(color = "black"),
                    flierprops = dict(
                        marker = "o",
                        markerfacecolor = "red",
                        markersize = 5
                    ))

        plt.title(f"{column} Outlier Analysis (Boxplot)")

        plt.ylabel(column)

        os.makedirs("charts/box", exist_ok = True)

        chart_path = f"charts/box/{column}_boxplot.png"

        plt.tight_layout()
        plt.savefig(chart_path, dpi = 300, bbox_inches = "tight")

        plt.close()

        chart_paths.append(chart_path)

    if len(chart_paths) > 0:
        return chart_paths
    return None

