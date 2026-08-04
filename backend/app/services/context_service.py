
def build_business_context(profile, health, insights, kpis):
    """
    build a concise business context for Gemini.
    """

    context = f"""
    Business Dataset Summary

    Rows: {profile['rows']}
    Columns: {profile['columns_count']}
    Health Score: {health['score']}%

    Missing Values: {profile['missing_values']}
    Duplicate Rows: {profile['duplicate_rows']}

    Key Performance Indicators:
"""

    for kpi in kpis:
        context += f"- {kpi['title']}: {kpi['value']}\n"

    context += "\nBusiness Insights:\n"

    for insight in insights:
        context +=f'- {insight}\n'

    return context

