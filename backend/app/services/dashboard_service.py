def generate_dashboard(insights, health, correlations, outliers, histogram, bar_charts, boxplots, profile):
    """
    build dashboard response
    """

    dashboard = {
        "summary_cards" : {
            "rows": profile['rows'],
            "columns": profile['columns_count'],
            "health_score": health['score'],
            "missing_values":profile['missing_values'],
            "duplicate_rows":profile['duplicate_rows'],
            "memory_usage_kb":profile['memory_usage_kb']

        },
        "business_insights":insights,
        "health" : health,
        "correlations":correlations,
        "outliers": outliers,
        "charts":{
            "histogram": histogram,
            "bar_chart": bar_charts,
            "boxplots":boxplots
        }
    }

    return dashboard