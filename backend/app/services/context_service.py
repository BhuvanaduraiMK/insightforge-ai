import pandas as pd


def build_business_context(profile, health, insights, kpis, df):
    """
    Build an analysis-ready business context for Gemini.
    """

    context = f"""
Business Dataset Summary

Rows: {profile['rows']}
Columns: {profile['columns_count']}
Health Score: {health['score']}%

Missing Values: {profile['missing_values']}
Duplicate Rows: {profile['duplicate_rows']}

"""

    # --------------------------------------------------
    # KPIs
    # --------------------------------------------------

    context += "\nKey Performance Indicators:\n"

    for kpi in kpis:
        context += f"- {kpi['title']}: {kpi['value']}\n"


    # --------------------------------------------------
    # Business Insights
    # --------------------------------------------------

    context += "\nBusiness Insights:\n"

    for insight in insights:
        context += f"- {insight}\n"


    # --------------------------------------------------
    # Dataset Schema
    # --------------------------------------------------

    context += "\nDataset Columns:\n"

    for column in df.columns:
        context += f"- {column}: {df[column].dtype}\n"


    # --------------------------------------------------
    # Numerical Statistics
    # --------------------------------------------------

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        context += "\nNumerical Statistics:\n"

        for column in numeric_columns:

            context += (
                f"- {column}: "
                f"count={df[column].count()}, "
                f"mean={df[column].mean():.2f}, "
                f"min={df[column].min():.2f}, "
                f"max={df[column].max():.2f}\n"
            )


    # --------------------------------------------------
    # Categorical → Numerical Analysis
    # --------------------------------------------------

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if categorical_columns and numeric_columns:

        context += "\nGrouped Business Analysis:\n"

        for categorical in categorical_columns:

            # Avoid extremely high-cardinality columns
            if df[categorical].nunique() > 30:
                continue

            for numeric in numeric_columns:

                grouped = (
                    df.groupby(categorical)[numeric]
                    .mean()
                    .dropna()
                )

                if grouped.empty:
                    continue

                context += (
                    f"\nAverage {numeric} by {categorical}:\n"
                )

                for category, value in grouped.items():

                    context += (
                        f"- {categorical}={category}: "
                        f"average {numeric}={value:.2f}\n"
                    )


    return context