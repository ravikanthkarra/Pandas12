import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df1 = employee.groupby('managerId').size().reset_index(name='cnt')
    df1 = df1[(df1['cnt'] > 4)]
    result = employee[employee['id'].isin(df1['managerId'])]

    return result[['name']]

