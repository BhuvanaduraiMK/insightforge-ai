import pandas as pd
import re

def add_kpi(kpis, title, value):
        kpis.append({
            "title": title,
            "value": value
        })

def format_title(column):
     """
     Convert database column names into readable titles.
     """
     column = column.replace("_"," ")
     column = re.sub(r'([a-z])([A-Z])',r'\1\2', column)

     column = column.replace("BMI", "BMI")
     column = column.replace("API", "API")
     column = column.replace("SQL", "SQL")
     column = column.replace("CSV", "CSV")

     column = column.replace('kg',"(kg)")
     column = column.replace('cm', "(cm)")
    

     title = column.title()
     title = title.replace("Bmi", "BMI")
     title = title.replace("(Kg)", "(kg)")
     title = title.replace("(Cm)", "(cm)")
     return title

    

def format_value(column, value):
    """
    format KPI value for better readability
    """

    if column == "MonthlyFee":
         return f'₹{value:,.0f}'

    if "kg" in column.lower():
        return f"{value:.2f} kg"

    if "cm" in column.lower():
        return f"{value:.2f} cm"

    if column == "Churned":
        return f"{value * 100:.1f}%"
        

    return value

def generate_kpis(df:pd.DataFrame):
    """
    Generate automatic KPIs from the dataset
    """

    kpis = []

    total_records = len(df)

    add_kpi(kpis,"Total records", total_records)

    total_columns = len(df.columns)

    add_kpi(kpis,"Total columns",total_columns)

    missing_values = int(df.isnull().sum().sum())

    add_kpi(kpis,"Missing value", missing_values)

    duplicate_rows = int(df.duplicated().sum())

    add_kpi(kpis,"Duplicate Rows", duplicate_rows)

    numeric_columns = df.select_dtypes(include = ["number"]).columns

    for column in numeric_columns:
        display_name = format_title(column)

        average = float(round(df[column].mean(),2))

        if column == "Churned":
             add_kpi(kpis,f'Churn Rate', format_value(column, average))
             continue

        minimum = df[column].min().item()
        maximum = df[column].max().item()
        median = float(round(df[column].median(),2))

        add_kpi(kpis,f"Average {display_name}", format_value(column, average))
        add_kpi(kpis,f"Minimum {display_name}", format_value(column, minimum))
        add_kpi(kpis,f'Maximum {display_name}', format_value(column, maximum))
        add_kpi(kpis,f"Median {display_name}", format_value(column, median))

    return kpis