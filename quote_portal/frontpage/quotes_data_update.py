import yfinance as yf


def get_data(symbol):
    """
    Function to get financial quotes from API
    :return:
    """
    quotes_data = yf.download(  # download Df with historical data
        tickers=symbol,
        period="max",
        interval="1m",
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None)
    quotes_data = quotes_data.reset_index()
    quotes_data = quotes_data[['Datetime', 'Close']]
    quotes_data['Datetime'] = quotes_data['Datetime'].astype(str)
    return quotes_data

# symbol = 'EURUSD=X'
# quotes_data = get_data(symbol)
# quotes_data.to_excel('qd.xlsx')