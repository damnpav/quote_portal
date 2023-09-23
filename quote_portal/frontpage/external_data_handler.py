import pandas as pd


file_path = '/Users/dp_user/PycharmProjects/quote_portal/quote_portal/external_data/book_products.xlsx'


def prepare_data():
    """
    Function to handle external excel file
    :return:
    """
    df = pd.read_excel(file_path)
    table_data = df.to_dict(orient='records')
    return table_data
