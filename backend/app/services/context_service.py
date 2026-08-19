import pandas as pd


def normalize_column_name(column):
    """
    Normalize column names so that variations such as:

    SatisfactionScore
    satisfaction_score
    Satisfaction Score
    satisfaction-score

    can be detected as the same logical column.
    """

    return (
        str(column)
        .strip()
        .lower()
        .replace("_", "")
        .replace(" ", "")
        .replace("-", "")
    )


def find_column(df, possible_names):
    """
    Find a dataframe column using normalized column names.
    """

    normalized_columns = {
        normalize_column_name(column): column
        for column in df.columns
    }

    for name in possible_names:

        normalized_name = normalize_column_name(name)

        if normalized_name in normalized_columns:
            return normalized_columns[normalized_name]

    return None


def build_business_context(
    profile,
    health,
    insights,
    kpis,
    df
):
    """
    Build a detailed business context for Gemini AI Q&A.

    The context is designed specifically for dataset Q&A.

    Includes:
    - Dataset profile
    - Dataset columns
    - KPIs
    - Business insights
    - Numeric statistics
    - Categorical values
    - Category counts
    - Group averages
    - Churn analysis
    - Churn by category
    - Satisfaction by churn status
    - Correlations
    - Explicit Q&A instructions
    """

    context = f"""
# BUSINESS DATASET CONTEXT

## Dataset Profile

Rows: {profile.get('rows', 'N/A')}
Columns: {profile.get('columns_count', 'N/A')}
Health Score: {health.get('score', 'N/A')}%

Missing Values: {profile.get('missing_values', 'N/A')}
Duplicate Rows: {profile.get('duplicate_rows', 'N/A')}

IMPORTANT DATA RULE:

The information below is generated directly from the uploaded
dataset.

Use ONLY the information contained in this context.

Do NOT invent values.

Do NOT assume information that is not present.

If a requested value exists anywhere in this context,
you MUST use it.

"""


    context += "\n## Dataset Columns\n"

    for column in df.columns:

        dtype = str(df[column].dtype)

        unique_count = df[column].nunique(
            dropna=True
        )

        context += (
            f"- {column}: "
            f"type={dtype}, "
            f"unique_values={unique_count}\n"
        )


    context += "\n## Key Performance Indicators\n"

    for kpi in kpis:

        title = kpi.get(
            "title",
            "Unknown KPI"
        )

        value = kpi.get(
            "value",
            "N/A"
        )

        context += (
            f"- {title}: {value}\n"
        )


    context += "\n## Business Insights\n"

    for insight in insights:

        context += (
            f"- {insight}\n"
        )

    churn_column = find_column(
        df,
        [
            "Churn",
            "Churned",
            "IsChurned",
            "ChurnStatus"
        ]
    )

    satisfaction_column = find_column(
        df,
        [
            "SatisfactionScore",
            "Satisfaction_Score",
            "Satisfaction Score",
            "Satisfaction"
        ]
    )


    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    context += "\n## Numeric Column Statistics\n"

    for column in numeric_columns:

        series = pd.to_numeric(
            df[column],
            errors="coerce"
        ).dropna()

        if series.empty:
            continue

        context += f"\n### {column}\n"

        context += (
            f"- Average: {series.mean():.2f}\n"
        )

        context += (
            f"- Median: {series.median():.2f}\n"
        )

        context += (
            f"- Minimum: {series.min():.2f}\n"
        )

        context += (
            f"- Maximum: {series.max():.2f}\n"
        )

        context += (
            f"- Count: {series.count()}\n"
        )


    categorical_columns = df.select_dtypes(
        include=[
            "object",
            "category",
            "bool"
        ]
    ).columns.tolist()

    context += (
        "\n## Categorical Columns and Values\n"
    )

    for column in categorical_columns:

        values = (
            df[column]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if len(values) > 20:
            continue

        context += f"\n### {column}\n"

        for value in sorted(values):

            context += (
                f"- {value}\n"
            )


    numeric_categorical_columns = []

    for column in numeric_columns:

        unique_count = df[column].nunique(
            dropna=True
        )

        if unique_count <= 10:

            numeric_categorical_columns.append(
                column
            )

    context += (
        "\n## Numeric Status / Category Columns\n"
    )

    for column in numeric_categorical_columns:

        values = (
            df[column]
            .dropna()
            .unique()
            .tolist()
        )

        context += f"\n### {column}\n"

        for value in sorted(values):

            count = int(
                (
                    df[column] == value
                ).sum()
            )

            context += (
                f"- {column} = {value}: "
                f"{count} records\n"
            )


    if churn_column is not None:

        context += "\n## Churn Analysis\n"

        context += (
            f"Churn column: {churn_column}\n"
        )

        if pd.api.types.is_numeric_dtype(
            df[churn_column]
        ):

            churn_numeric = pd.to_numeric(
                df[churn_column],
                errors="coerce"
            )

            churn_rate = (
                churn_numeric.mean() * 100
            )

            context += (
                f"Overall churn rate: "
                f"{churn_rate:.2f}%\n"
            )

            context += (
                "Churn interpretation: "
                "0 = Active / Not Churned, "
                "1 = Churned.\n"
            )

            for value in sorted(
                churn_numeric.dropna().unique()
            ):

                count = int(
                    (
                        churn_numeric == value
                    ).sum()
                )

                if value == 1:
                    label = "Churned"

                elif value == 0:
                    label = "Active"

                else:
                    label = str(value)

                context += (
                    f"- {label}: "
                    f"{count} members\n"
                )


        else:

            churn_counts = (
                df[churn_column]
                .dropna()
                .astype(str)
                .value_counts()
            )

            context += (
                "Churn values are categorical.\n"
            )

            for value, count in (
                churn_counts.items()
            ):

                context += (
                    f"- {value}: "
                    f"{int(count)} members\n"
                )

    else:

        context += (
            "\n## Churn Analysis\n"
            "No churn column was detected "
            "in the uploaded dataset.\n"
        )


    grouping_columns = (
        categorical_columns
        + [
            column
            for column in numeric_categorical_columns
            if column not in categorical_columns
        ]
    )


    context += (
        "\n## Categorical Group Analysis\n"
    )

    for category in grouping_columns:

        unique_count = df[category].nunique(
            dropna=True
        )

        if (
            unique_count == 0
            or unique_count > 20
        ):
            continue

        context += (
            f"\n### Group: {category}\n"
        )

        counts = (
            df[category]
            .value_counts(
                dropna=True
            )
        )

        context += "Member Counts:\n"

        for group_name, count in (
            counts.items()
        ):

            context += (
                f"- {category} = "
                f"{group_name}: "
                f"{int(count)} members\n"
            )


        for numeric_column in numeric_columns:

            if numeric_column == category:
                continue

            grouped = (
                df.groupby(
                    category,
                    dropna=True
                )[numeric_column]
                .mean()
                .dropna()
                .sort_values(
                    ascending=False
                )
            )

            if grouped.empty:
                continue

            context += (
                f"\nAverage {numeric_column} "
                f"by {category}:\n"
            )

            for group_name, value in (
                grouped.items()
            ):

                context += (
                    f"- {category} = "
                    f"{group_name}: "
                    f"{value:.2f}\n"
                )


    if churn_column is not None:

        context += (
            "\n## Churn Rate by Category\n"
        )

        if pd.api.types.is_numeric_dtype(
            df[churn_column]
        ):

            for category in grouping_columns:

                if category == churn_column:
                    continue

                unique_count = (
                    df[category]
                    .nunique(
                        dropna=True
                    )
                )

                if (
                    unique_count == 0
                    or unique_count > 20
                ):
                    continue

                grouped_churn = (
                    df.groupby(
                        category,
                        dropna=True
                    )[churn_column]
                    .mean()
                    .dropna()
                    * 100
                )

                if grouped_churn.empty:
                    continue

                context += (
                    f"\nChurn Rate by "
                    f"{category}:\n"
                )

                for group_name, rate in (
                    grouped_churn
                    .sort_values(
                        ascending=False
                    )
                    .items()
                ):

                    context += (
                        f"- {category} = "
                        f"{group_name}: "
                        f"{rate:.2f}% churn\n"
                    )

    
    if (
        churn_column is not None
        and satisfaction_column is not None
    ):

        context += (
            "\n## Satisfaction by Churn Status\n"
        )

        context += (
            f"Satisfaction column: "
            f"{satisfaction_column}\n"
        )

        context += (
            f"Churn column: "
            f"{churn_column}\n"
        )

        # Numeric churn
        if pd.api.types.is_numeric_dtype(
            df[churn_column]
        ):

            grouped = (
                df.groupby(
                    churn_column
                )[satisfaction_column]
                .mean()
                .dropna()
            )

            for status, value in (
                grouped.items()
            ):

                if status == 0:
                    label = "Active"

                elif status == 1:
                    label = "Churned"

                else:
                    label = str(status)

                context += (
                    f"- {label}: "
                    f"Average "
                    f"{satisfaction_column} = "
                    f"{value:.2f}\n"
                )

        # Categorical churn
        else:

            grouped = (
                df.groupby(
                    churn_column
                )[satisfaction_column]
                .mean()
                .dropna()
            )

            for status, value in (
                grouped.items()
            ):

                context += (
                    f"- {status}: "
                    f"Average "
                    f"{satisfaction_column} = "
                    f"{value:.2f}\n"
                )

    else:

        context += (
            "\n## Satisfaction by Churn Status\n"
            "A compatible churn column and "
            "satisfaction column were not both "
            "detected.\n"
        )

    
    context += (
        "\n## Numeric Correlations\n"
    )

    if len(numeric_columns) >= 2:

        correlation_matrix = (
            df[numeric_columns]
            .corr()
        )

        added_pairs = set()

        for column1 in numeric_columns:

            for column2 in numeric_columns:

                if column1 == column2:
                    continue

                pair = tuple(
                    sorted(
                        [
                            column1,
                            column2
                        ]
                    )
                )

                if pair in added_pairs:
                    continue

                correlation = (
                    correlation_matrix
                    .loc[
                        column1,
                        column2
                    ]
                )

                if pd.notna(correlation):

                    context += (
                        f"- Correlation between "
                        f"{column1} and "
                        f"{column2}: "
                        f"{correlation:.2f}\n"
                    )

                    added_pairs.add(pair)

    
    context += """

## Q&A Guidance

When answering user questions:

1. Treat this Dataset Context as the source of truth.

2. Search the ENTIRE context before saying
   information is unavailable.

3. If the requested value appears anywhere in
   the context, answer using that value.

4. For average questions:
   use Numeric Column Statistics or
   Average <column> by <category>.

5. For highest questions:
   compare all relevant groups and identify
   the highest value.

6. For lowest questions:
   compare all relevant groups and identify
   the lowest value.

7. For count questions:
   use Member Counts.

8. For churn questions:
   use Churn Analysis and Churn Rate by Category.

9. For churned vs active questions:
   use Satisfaction by Churn Status when available.

10. For correlation questions:
    use Numeric Correlations.

11. For business recommendations:
    use numerical evidence from this context.

12. Never invent a value.

13. Never assume a value that is not present.

14. Do not say:
    "The uploaded dataset does not contain enough information."
    when the requested information exists in this context.

15. If the requested information genuinely does not exist
    in this context, then say:
    "The uploaded dataset does not contain enough information."

16. Answer simple questions directly.

17. Keep answers concise unless the user asks for
    a detailed explanation or report.

"""

    return context