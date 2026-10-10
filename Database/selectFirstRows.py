# LeetCode 2879 - Display the First Three Rows (Easy)
#
# Given a pandas DataFrame employees with columns employee_id, name, department
# and salary, return a DataFrame containing only its first three rows, with all
# columns kept.
#
# Example: a 6-row employees table  ->  rows 0, 1 and 2 of that table

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Access rows to 3 exluding 3. other solution employees.iloc[:3, :] which returns rows 0:3 all columns 
    return employees[:3]
    