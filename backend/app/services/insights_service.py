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
            f"Average monthly fee is {average_monthly_fee:.2f}"
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
        most_popular = df["MembershipType"].value_counts().idxmax()
        count = df["MembershipType"].value_counts().max()

        insights.append(
            f"The most popular membership type is {most_popular} ({count} members)."
        )  

    return insights