# import pandas as pd


# def generate_insights(df: pd.DataFrame) -> list:
#     """
#     Generate simple business insights from a dataset.
#     """

#     insights = []

#     # Dataset size
#     insights.append(
#         f"Dataset contains {len(df)} records."
#     )

#     if "Age" in df.columns:
#         avg_age = round(df["Age"].mean(), 2)

#         insights.append(
#             f"Average member age is {avg_age} years."
#         )

#     if "MonthlyFee" in df.columns:
#         average_monthly_fee = df["MonthlyFee"].mean()

#         insights.append(
#             f"Average monthly fee is ₹{average_monthly_fee:,.2f}."
#         )

#     if "SatisfactionScore" in df.columns:
#             average_Satisfaction_score = df["SatisfactionScore"].mean()
    
#             insights.append(
#                 f"Average satisfaction score is {average_Satisfaction_score:.2f}"
#             )

#     if "WeightLoss_kg" in df.columns:
#                 average_weight_loss = df["WeightLoss_kg"].mean()
        
#                 insights.append(
#                     f"Average weight loss is {average_weight_loss:.2f} kg"
#                 )

#     if "Churned" in df.columns:
#                     average_churn_rate = df["Churned"].mean()*100
            
#                     insights.append(
#                         f"Average churn rate is {average_churn_rate:.2f}"
#                     )       

#     if "MembershipType" in df.columns:
#         membership_counts = df["MembershipType"].value_counts()

#         most_popular = membership_counts.idxmax()
#         count = membership_counts.max()

#         insights.append(
#             f"The most popular membership type is {most_popular} ({count} members)."
#         )  

#     if "WorkoutType" in df.columns:
#         workout_counts = df["WorkoutType"].value_counts()

#         most_common_workout = workout_counts.idxmax()
#         most_common_count = workout_counts.max()

#         insights.append(
#             f"The most common workout type is {most_common_workout} ({most_common_count} members)."
#         )

#     if "Goal" in df.columns:
#             goal_counts = df["Goal"].value_counts()
    
#             most_common_goal = goal_counts.idxmax()
#             most_common_count = goal_counts.max()
    
#             insights.append(
#                 f"The most common goal is {most_common_goal} ({most_common_count} members)."
#             )

#     if "Gender" in df.columns:
#         gender_counts = df["Gender"].value_counts()

#         insights.append(
#             f"Female members: {gender_counts.get('Female', 0)}, "
#             f"Male members: {gender_counts.get('Male', 0)}."
#         )

#     if "SessionsPerWeek" in df.columns:
#         average_sessions = df["SessionsPerWeek"].mean()

#         insights.append(
#             f"Members attend an average of {average_sessions:.2f} sessions per week."
#         )

#     if "City" in df.columns:
#         city_counts = df["City"].value_counts()

#         top_city = city_counts.idxmax()
#         member_count = city_counts.max()

#         insights.append(
#             f"The city with the most members is {top_city} ({member_count} members)."
#         )

#     if "MonthlyFee" in df.columns:
#         total_revenue = df["MonthlyFee"].sum()

#         insights.append(
#             f"Estimated total monthly revenue is ₹{total_revenue:,.2f}."
#         )

#     if "Churned" in df.columns:
#         churn_rate = df["Churned"].mean() * 100

#         insights.append(
#             f"Average churn rate is {churn_rate:.2f}%."
#         )

#     if "MembershipType" in df.columns:
#         membership_counts = df["MembershipType"].value_counts()

#         most_popular = membership_counts.idxmax()
#         member_count = membership_counts.max()

#         insights.append(
#             f"The most popular membership type is {most_popular} ({member_count} members)."
#         )

#     if "WorkoutType" in df.columns:
#         workout_counts = df["WorkoutType"].value_counts()

#         most_common_workout = workout_counts.idxmax()
#         member_count = workout_counts.max()

#         insights.append(
#             f"The most common workout type is {most_common_workout} ({member_count} members)."
#         )

#     if "Goal" in df.columns:
#         goal_counts = df["Goal"].value_counts()

#         most_common_goal = goal_counts.idxmax()
#         member_count = goal_counts.max()

#         insights.append(
#             f"The most common fitness goal is {most_common_goal} ({member_count} members)."
#         )

#     return insights



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