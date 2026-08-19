import pandas as pd


def generate_insights(df: pd.DataFrame) -> list:
    """
    Generate simple business insights from a dataset.
    """

    insights = []

    # Dataset size
    insights.append(
        f"Dataset contains {len(df)} records."
    )

    if "Age" in df.columns:
        avg_age = round(df["Age"].mean(), 2)

        insights.append(
            f"Average member age is {avg_age} years."
        )

    if "MonthlyFee" in df.columns:
        average_monthly_fee = df["MonthlyFee"].mean()

        insights.append(
            f"Average monthly fee is ₹{average_monthly_fee:,.2f}."
        )

    if "SatisfactionScore" in df.columns:
            average_Satisfaction_score = df["SatisfactionScore"].mean()
    
            insights.append(
                f"Average satisfaction score is {average_Satisfaction_score:.2f}"
            )

    if "WeightLoss_kg" in df.columns:
                average_weight_loss = df["WeightLoss_kg"].mean()
        
                insights.append(
                    f"Average weight loss is {average_weight_loss:.2f} kg"
                )

    if "Churned" in df.columns:
                    average_churn_rate = df["Churned"].mean()*100
            
                    insights.append(
                        f"Average churn rate is {average_churn_rate:.2f}"
                    )       

    if "MembershipType" in df.columns:
        membership_counts = df["MembershipType"].value_counts()

        most_popular = membership_counts.idxmax()
        count = membership_counts.max()

        insights.append(
            f"The most popular membership type is {most_popular} ({count} members)."
        )  

    if "WorkoutType" in df.columns:
        workout_counts = df["WorkoutType"].value_counts()

        most_common_workout = workout_counts.idxmax()
        most_common_count = workout_counts.max()

        insights.append(
            f"The most common workout type is {most_common_workout} ({most_common_count} members)."
        )

    if "Goal" in df.columns:
            goal_counts = df["Goal"].value_counts()
    
            most_common_goal = goal_counts.idxmax()
            most_common_count = goal_counts.max()
    
            insights.append(
                f"The most common goal is {most_common_goal} ({most_common_count} members)."
            )

    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()

        insights.append(
            f"Female members: {gender_counts.get('Female', 0)}, "
            f"Male members: {gender_counts.get('Male', 0)}."
        )

    if "SessionsPerWeek" in df.columns:
        average_sessions = df["SessionsPerWeek"].mean()

        insights.append(
            f"Members attend an average of {average_sessions:.2f} sessions per week."
        )

    if "City" in df.columns:
        city_counts = df["City"].value_counts()

        top_city = city_counts.idxmax()
        member_count = city_counts.max()

        insights.append(
            f"The city with the most members is {top_city} ({member_count} members)."
        )

    if "MonthlyFee" in df.columns:
        total_revenue = df["MonthlyFee"].sum()

        insights.append(
            f"Estimated total monthly revenue is ₹{total_revenue:,.2f}."
        )

    if "Churned" in df.columns:
        churn_rate = df["Churned"].mean() * 100

        insights.append(
            f"Average churn rate is {churn_rate:.2f}%."
        )

    if "MembershipType" in df.columns:
        membership_counts = df["MembershipType"].value_counts()

        most_popular = membership_counts.idxmax()
        member_count = membership_counts.max()

        insights.append(
            f"The most popular membership type is {most_popular} ({member_count} members)."
        )

    if "WorkoutType" in df.columns:
        workout_counts = df["WorkoutType"].value_counts()

        most_common_workout = workout_counts.idxmax()
        member_count = workout_counts.max()

        insights.append(
            f"The most common workout type is {most_common_workout} ({member_count} members)."
        )

    if "Goal" in df.columns:
        goal_counts = df["Goal"].value_counts()

        most_common_goal = goal_counts.idxmax()
        member_count = goal_counts.max()

        insights.append(
            f"The most common fitness goal is {most_common_goal} ({member_count} members)."
        )

    return insights