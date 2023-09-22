import yfinance as yf
import pandas as pd


def get_data(symbols):
    """
    Function to get financial quotes from API
    symbols - List with names of currencies (['EURUSD=X', 'GBPUSD=X'])
    :return:
    """
    quotes_data = yf.download(  # download Df with historical data
        tickers=symbols,
        period="max",
        interval="1m",
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None)

    quotes_data_list = []
    for symbol in symbols:
        current_df = quotes_data[symbol].copy()
        current_df = current_df.reset_index()
        current_df = current_df[['Datetime', 'Close']]
        current_df['Datetime'] = current_df['Datetime'].astype(str)
        quotes_data_list.append(current_df)
    return quotes_data_list

# symbol = 'EURUSD=X'
# quotes_data = get_data(symbol)
# quotes_data.to_excel('qd.xlsx')