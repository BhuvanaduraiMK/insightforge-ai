import re
import pandas as pd


def normalize_column_name(column:str):
    """
    convert database  column names into readable names.
    """

    column = column.replace("_"," ")
    column = re.sub(r'([a-z])([A-Z])',r'\1 \2', column)

    return column.lower()



def answer_question(df:pd.DataFrame, question: str):
    """
    Answer a question based on the dataset
    """
    question = question.lower()
    print("Question received:", question)
    
    numeric_columns = df.select_dtypes(include=["number"]).columns
    
    question_words = set(question.split())
    if "average" in question:
        for column in numeric_columns:
            search_name = normalize_column_name(column)            
            search_words = set(search_name.split())

            if search_words.issubset(question_words):
                average = round(df[column].mean(), 2)
                return f"The average {search_name} is {average}"

    elif "minimum" in question:
        for column in numeric_columns:
            search_name = normalize_column_name(column)
            search_words = set(search_name.split())

            if search_words.issubset(question_words):
                minimum = df[column].min()
                if "monthly fee" in search_name:
                    return f"The minimum {search_name} is ₹{minimum:,.0f}"
                return f"The minimum {search_name} is {minimum}"

    elif "maximum" in question:
        for column in numeric_columns:
            search_name = normalize_column_name(column)
            search_words = set(search_name.split())

            if search_words.issubset(question_words):
                maximum = df[column].max()
                if "monthly fee" in search_name:
                    return f"The maximum {search_name} is ₹{maximum:,.0f}"
                return f"The maximum {search_name} is {maximum}"

    elif "median" in question:
        for column in numeric_columns:
            search_name = normalize_column_name(column)
            search_words = set(search_name.split())

            if search_words.issubset(question_words):
                _median = round(df[column].median(),0)
                if "monthly fee" in search_name:
                    return f"The median {search_name} is ₹{_median:,.0f}"
                return f"The median {search_name} is {_median}"

    elif "total records" in question:
        total_records,columns = df.shape
        return f'The total number of records is {total_records}.' 

    elif "missing values" in question:
        missing_values = int(df.isnull().sum().sum())
        return f"There are {missing_values} missing values in the dataset"
    elif "duplicate rows" in question:
        duplicated_rows = int(df.duplicated().sum())
        return f'There are {duplicated_rows} duplicate rows in the dataset'
        

    return "Sorry, I don't understand the question."

