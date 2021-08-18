import sqlite3
import time
import yfinance as yf

#Grab ticker information for each stock 
def get_ticker_price(self, ticker):
    stock = yf.Ticker(ticker)
    return stock.info['currentPrice']

"""Need to fix these functions"""


#Be able to create to tables in sqlite3
def __init__(self):
    self.con = sqlite3.connect("/Users/andrew/Documents/Personal Project/StockPlatform/stock.db")
    self.cur = self.con.cursor()
    
    #Two tables
    """
        1 table where we hold 50-10+
            To_the_moon(ticker, purchase price, date)
        1 table where we buy and sell 50-10 
            Index_fund(ticker,been_purchased)
                ticker_idtable(purchase, selling, date_purchase,date_sell,profit)
                
        1 table where we buy and sell 10 and lower stocks 
            Penny_stocks(ticker,been_purchased)
                table(purchase, selling, date_purchase,date_sell,profit)

        All stocks will be based on insider trading news 
    """
def create_database(self):
    self.con = sqlite3.connect("/Users/andrew/Documents/Personal Project/StockBot/stock.db")
    self.cur = self.con.cursor()

def create_table(self):
    self.cur.execute('''CREATE TABLE To_the_moon
               (ticker,purchase_price,date)''')
    self.con.commit()

def insert_data(self, datalist):
        #datalist = [ticker,price,date]
    self.cur.execute("INSERT INTO To_the_moon VALUES {ticker},{price},{date})".format(ticker = datalist[0],price = datalist[1],date= datalist[2]))
    self.con.commit()
        
    
def retrieve_data(self):
    for row in self.cur.execute('SELECT * FROM To_the_moon ORDER BY purchase_price'):
        print(row)
        
def find_all_tables(self):
    res = self.con.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for name in res.fetchall():
            print(name[0])

def close_database(self):
    self.con.close()