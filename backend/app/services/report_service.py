def generate_report(profile, health, insights, kpis):
    """
    generate business report
    """
    report = []

    report.append("="*50)
    report.append("InsightsForge AI")
    report.append("Business Analysis Report")
    report.append("="*50)
    report.append("")

    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 50)

    report.append(
        f"The uploaded dataset contains "
        f"{profile['rows']} records and "
        f"{profile['columns_count']} columns."
    )

    report.append(
        f"The overall data quality score is "
        f"{health['score']}%."
    )

    report.append(
        f"The dataset contains "
        f"{profile['missing_values']} missing values "
        f"and {profile['duplicate_rows']} duplicate rows."
    )

    report.append("")

    report.append("DATASET SUMMARY")
    report.append("-"*50)
    report.append(f"Rows           : {profile['rows']}")
    report.append(f'Columns        : {profile["columns_count"]}')
    report.append(f'Health Score   : {health["score"]}%')
    report.append(f'Missing Values : {profile["missing_values"]}')
    report.append(f'Duplicate Rows : {profile["duplicate_rows"]}')
    report.append("")


    report.append("BUSINESS INSIGHTS")
    report.append("-"*50)

    seen = set()

    for insight in insights:

        if insight not in seen:
            report.append(f"• {insight}")
            seen.add(insight)

    report.append("")

    report.append("KEY PERFORMANCE INDICATORS (KPIS)")
    report.append("-"*50)

    for kpi in kpis[:12]:
        report.append(f"{kpi['title']} : {kpi['value']}")

    report.append("")
    report.append("=" * 50)
    report.append("End of Report")
    report.append("=" * 50)

    return "\n".join(report)
    

# def generate_report(
#     profile,
#     health,
#     insights,
#     kpis
# ):
#     """
#     Generate a simple business analysis report.
#     """

#     report = []

#     # ==========================
#     # Report Title
#     # ==========================
#     report.append("=" * 50)
#     report.append("BUSINESS ANALYSIS REPORT")
#     report.append("=" * 50)
#     report.append("")

#     # ==========================
#     # Dataset Summary
#     # ==========================
#     report.append("DATASET SUMMARY")
#     report.append("-" * 50)
#     report.append(f"Rows           : {profile['rows']}")
#     report.append(f"Columns        : {profile['columns_count']}")
#     report.append(f"Health Score   : {health['score']}%")
#     report.append(f"Missing Values : {profile['missing_values']}")
#     report.append(f"Duplicate Rows : {profile['duplicate_rows']}")
#     report.append("")

#     # ==========================
#     # Business Insights
#     # ==========================
#     report.append("BUSINESS INSIGHTS")
#     report.append("-" * 50)

#     for insight in insights:
#         report.append(f"• {insight}")

#     report.append("")

#     # ==========================
#     # Key Performance Indicators
#     # ==========================
#     report.append("KEY PERFORMANCE INDICATORS")
#     report.append("-" * 50)

#     for kpi in kpis[:10]:
#         report.append(f"{kpi['title']} : {kpi['value']}")

#     report.append("")
#     report.append("=" * 50)
#     report.append("End of Report")
#     report.append("=" * 50)

#     return "\n".join(report)