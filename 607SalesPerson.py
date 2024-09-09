import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    comp_id = company[(company['name'] == 'RED')]
    non_red_orders = orders.merge(comp_id, on = 'com_id', how = 'inner')
    # print(non_red_orders)
    sales_id = sales_person[~sales_person['sales_id'].isin(non_red_orders['sales_id'])]
    # print(sales_id)
    return sales_id[['name']]