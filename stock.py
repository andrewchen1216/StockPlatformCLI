import sqlite3
import time
import hashlib
import yfinance as yf

#Grab ticker information for each stock 
def get_ticker_price(self, ticker):
    stock = yf.Ticker(ticker)
    return stock.info['currentPrice']

"""Need to fix these functions"""
    
  

def create_database():
    con = sqlite3.connect("/Users/andrew/Documents/Personal Project/StockPlatform/stock.db")
    return con

def create_table_account(con,name):
    cur = con.cursor()
    cur.execute('''CREATE TABLE To_the_moon
               (ticker,purchase_price,date)''')
    con.commit()

def create_table_stocks(con,id):
    pass

def create_table_trades(con,id):
    pass

def insert_data_users(self, datalist):
        #datalist = [ticker,price,date]
    self.cur.execute("INSERT INTO To_the_moon VALUES {ticker},{price},{date})".format(ticker = datalist[0],price = datalist[1],date= datalist[2]))
    self.con.commit()

def insert_data_accounts():
    pass

def insert_data_trades():
    pass

def insert_data_stocks():
    pass
        
def remove_data_account():
    pass

def remove_data_stocks():
    pass


def retrieve_data(self):
    for row in self.cur.execute('SELECT * FROM To_the_moon ORDER BY purchase_price'):
        print(row)
        
def find_all_tables(self):
    res = self.con.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for name in res.fetchall():
            print(name[0])

def close_database(self):
    self.con.close()