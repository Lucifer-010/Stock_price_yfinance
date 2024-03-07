<h1>Yfinance: Python Library for Financial Data</h1>

<p>Yfinance is a Python library that provides convenient access to financial market data from various sources, including:</p>

<ul>
  <li>Yahoo Finance</li>
  <li>FRED (Federal Reserve Economic Data)</li>
  <li>Quandl</li>
  <li>Morningstar</li>
</ul>

<p>It offers a user-friendly interface for downloading historical and real-time stock quotes, cryptocurrency data, economic indicators, and more.</p>

<h2>Installation</h2>

<p>Yfinance can be installed using pip:</p>

<pre>pip install yfinance</pre>

<h2>Basic Usage</h2>

```python
import yfinance as yf

# Download historical stock data for Apple
aapl = yf.download("AAPL", period="1d")

# Print the closing price
print(aapl["Close"])
