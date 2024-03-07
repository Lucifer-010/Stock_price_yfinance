import yfinance as yf


def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        return current_price
    except Exception as e:
        #print(f"Error fetching forex price: {e}")
        return (0.00)

def get_forex_price(symbol):
    try:
        forex_pair = yf.Ticker(symbol)
        current_price = forex_pair.history(period='1d')['Close'].iloc[-1]
        return current_price
    except Exception as e:
        #print(f"Error fetching forex price: {e}")
        return (0.00) 
