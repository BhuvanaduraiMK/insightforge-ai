import pandas as pd


def calculate_health_score(df: pd.DataFrame):
    """
    Calculate dataset health score.
    """
    
    score = 100

    missing_values = int(
                df.isnull().sum().sum()
        )

    if missing_values == 0:
        pass
    elif missing_values >= 1 and missing_values <= 10:
        score -=5
    elif missing_values >= 11 and missing_values <= 50:
        score -=10
    else:
        score -=20

    duplicate_rows = int(
        df.duplicated().sum()
        )


    if duplicate_rows == 0:
        pass
    elif duplicate_rows >= 1 and duplicate_rows <= 10:
        score -=5
    else:
        score -=10

    rows = df.shape[0] # or rows = len(df)

    if rows < 1:
        score = 0

    if score >= 90:
        status = "Excellent"
    elif score >= 75:
        status = "Good"
    elif score >= 50:
        status = "Fair"
    else:
        status = "Needs cleaning"

        
    return {
        "score" : score,
        "status" : status
    }