def generate_suggestions(profile, kpis, insights):

    suggestions = []

    columns = [col.lower() for col in profile["columns"]]
    

    if 'revenue' in columns:
        suggestions.append(
            "Which category generate the highest revenue?"
        )

        suggestions.append(
            "How can revenue be improved?"
        )

    if "sales" in columns:
        suggestions.append(
            "Which region has the highest sales?"
        )

        suggestions.append(
            "Show the best performing products."
        )

    if 'churn' in columns:
        suggestions.append(
            "Why is churn high?"
        )

        suggestions.append(
            'How can we reduce churn'
        )

    if "membership_type" in columns:
        suggestions.append(
            "Which membership type is most popular?"
        )

    if "satisfaction_score" in columns:
        suggestions.append(
            "How can customer satisfaction be improved?"
        )

    if "weight_loss_kg" in columns:
        suggestions.append(
            'Which members achieved the highest weight loss?'
        )

    suggestions.append(
        "Give me a business summary."
    )

    suggestions.append(
        "What are the top KPIs?"
    )

    suggestions.append(
        "Give me business recommendations."
    )

    suggestions = list(dict.fromkeys(suggestions))


    return suggestions[:8]