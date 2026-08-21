import pandas as pd

def _format_column_name(column):
    """
    Convert column names into readable text.
    Example:
        MonthlyFee -> Monthly Fee
        Weight_start_kg -> Weight Start Kg
    """
    return str(column).replace("_"," ").strip()

def _format_number(value):
    """
    format numeric values cleanly.
    """
    if pd.isna(value):
        return "N/A"
    if isinstance(value, float):
        if value.is_integer():
            return f"{int(value):,}"
        return f"{value:,.2f}"
    return f"{value:,}" if isinstance(value, int) else str(value)

def generate_insights(df: pd.DataFrame) -> list:
    """
    Generate generic dataset insights.
    Work with different csv dataset without relying on dataset-specific column names.
    """

    insights = []
    if df is None or df.empty:
        return["The upload dataset is empty."]

    rows = len(df)
    columns = len(df.columns)

    insights.append(
        f'Dataset contains {rows:,} records across {columns} columns.'
    )

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    useful_numeric_columns = []

    for column in numeric_columns:
        unique_count = df[column].nunique(dropna = True)

        if unique_count == len(df):
            continue

        useful_numeric_columns.append(column)

    numeric_insights_added = 0

    for column in useful_numeric_columns:
        if numeric_insights_added>=5:
            break

        series = df[column].dropna()

        if series.empty:
            continue

        average = series.mean()
        column_name = _format_column_name(column)

        insights.append(
            f'Average{column_name} is {_format_number(average)}.'
        )

        numeric_insights_added +=1

    categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

    categorical_insights_added = 0

    for column in categorical_columns:
        if categorical_insights_added >= 5:
            break

        series = df[column].dropna()

        if series.empty:
            continue

        unique_count = series.nunique()

        if unique_count > 20:
            continue

        value_counts = series.value_counts()

        if value_counts.empty:
            continue

        most_common = value_counts.index[0]
        count = value_counts.iloc[0]

        column_name = _format_column_name(column)

        insights.append(
            f'The most common {column_name} is'
            f'{most_common} ({count:,} records).'
        )

        categorical_insights_added +=1



    binary_columns = []

    for column in df.columns:
        unique_values = df[column].dropna().unique()

        if len(unique_values) == 2:
            binary_columns.append(column)

    binary_insights_added = 0

    for column in binary_columns:
        if binary_insights_added >= 3:
            break
        series = df[column].dropna()

        if series.empty:
            continue

        value_counts = series.value_counts()

        if len(value_counts) != 2:
            continue

        most_common_value = value_counts.index[0]
        percentage = (value_counts.iloc[0]/len(series)*100)

        column_name = _format_column_name(column)

        insights.append(
            f"For {column_name}, "
            f"{most_common_value} is the most common value "
            f"({percentage:.2f}% of records)."
        )

        binary_insights_added +=1


    range_insights_added = 0

    for column in useful_numeric_columns:
        if range_insights_added >= 3:
            break

        series = df[column].dropna()
        if series.empty:
            continue

        minimum = series.min()
        maximum = series.max()

        column_name = _format_column_name(column)

        insights.append(
            f"{column_name} ranges from "
            f"{_format_number(minimum)} to"
            f"{_format_number(maximum)}."
        )

        range_insights_added += 1

    unique_insights = []
    seen = set()

    for insight in insights:
        if insight not in seen:
            unique_insights.append(insight)
            seen.add(insight)

    return unique_insights