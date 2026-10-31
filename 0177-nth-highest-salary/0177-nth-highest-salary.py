import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N <= 0 or len(salaries) < N:
        result = None
    else:
        result = salaries.iloc[N - 1]

    return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [result]})