import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Access rows to 3 exluding 3. other solution employees.iloc[:3, :] which returns rows 0:3 all columns 
    return employees[:3]
    