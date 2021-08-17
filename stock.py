import sqlite3
import time
import yfinance as yf

#Grab ticker information for each stock 
def get_ticker_price(self, ticker):
    stock = yf.Ticker(ticker)
    return stock.info['currentPrice']