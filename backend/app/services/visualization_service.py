import os

import matplotlib.pyplot as plt
import pandas as pd


def generate_histogram(df: pd.DataFrame):
    """
    Generate histograms for numeric columns.

    Returns:
        list[str] | None
    """

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    if len(numeric_columns) == 0:
        return None

    chart_paths = []

    os.makedirs(
        "charts/histogram",
        exist_ok=True
    )

    for column in numeric_columns:

        # Skip binary/status columns
        if df[column].nunique() <= 2:
            continue

        series = pd.to_numeric(
            df[column],
            errors="coerce"
        ).dropna()

        if series.empty:
            continue

        plt.figure(figsize=(10, 6))

        plt.hist(
            series,
            bins=10,
            color="steelblue",
            edgecolor="black",
            alpha=0.8
        )

        plt.title(
            f"{column} Distribution"
        )

        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        chart_path = (
            f"charts/histogram/"
            f"{column}_histogram.png"
        )

        plt.savefig(
            chart_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        chart_paths.append(chart_path)

    if len(chart_paths) >0:
        return chart_paths

    return None


def generate_bar_charts(df: pd.DataFrame):
    """
    Generate bar charts for categorical columns.

    Returns:
        list[str] | None
    """

    categorical_columns = df.select_dtypes(
        exclude=["number"]
    ).columns

    if len(categorical_columns) == 0:
        return None

    chart_paths = []

    os.makedirs(
        "charts/bar",
        exist_ok=True
    )

    for column in categorical_columns:

        # Avoid very high-cardinality columns
        if df[column].nunique() > 20:
            continue

        value_counts = (
            df[column]
            .value_counts()
            .head(20)
        )

        if value_counts.empty:
            continue

        plt.figure(figsize=(8, 5))

        plt.bar(
            value_counts.index.astype(str),
            value_counts.values,
            color="cornflowerblue",
            edgecolor="black"
        )

        plt.title(
            f"{column} Distribution"
        )

        plt.xlabel(column)
        plt.ylabel("Count")

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        chart_path = (
            f"charts/bar/"
            f"{column}_bar_chart.png"
        )

        plt.tight_layout()

        plt.savefig(
            chart_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        chart_paths.append(chart_path)

    if len(chart_paths)>0:
        return chart_paths

    return None



def generate_boxplot(df: pd.DataFrame):
    """
    Generate box plots for numeric columns.

    Returns:
        list[str] | None
    """

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    if len(numeric_columns) == 0:
        return None

    chart_paths = []

    os.makedirs(
        "charts/box",
        exist_ok=True
    )

    for column in numeric_columns:

        # Skip binary/status columns
        if df[column].nunique() <= 2:
            continue

        series = pd.to_numeric(
            df[column],
            errors="coerce"
        ).dropna()

        if series.empty:
            continue

        plt.figure(figsize=(8, 6))

        plt.boxplot(
            series,
            patch_artist=True,
            boxprops=dict(
                facecolor="lightgreen",
                color="black"
            ),
            medianprops=dict(
                color="red",
                linewidth=2
            ),
            whiskerprops=dict(
                color="black"
            ),
            capprops=dict(
                color="black"
            ),
            flierprops=dict(
                marker="o",
                markerfacecolor="red",
                markersize=5
            )
        )

        plt.title(
            f"{column} Outlier Analysis"
        )

        plt.ylabel(column)

        chart_path = (
            f"charts/box/"
            f"{column}_boxplot.png"
        )

        plt.tight_layout()

        plt.savefig(
            chart_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        chart_paths.append(chart_path)

    if len(chart_paths)>0:
        return chart_paths

    return None