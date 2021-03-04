# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
def read_portfolio(filename):
    '''computes the total cost (shares*price) of a portfolio file'''
    portfolio=[]

    with open(filename,'rt') as f:
        rows=csv.reader(f)
        headers= next(rows)
        for row in rows:
            holding ={'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            #holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''reads current prices of stocks'''
    prices={}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                pass
    return prices
#price =read_prices('practical-python/Work/Data/prices.csv')
#print (price)

def gains(portfoliof, pricef):  #exercise 2.7
    portfolio= read_portfolio(portfoliof)
    prices = read_prices(pricef)
    profit=0.0
    current_val=0.0
    for stock in portfolio:
        current_val+= stock['price']*stock['shares']
        profit+= (prices[stock['name']]-stock['price'])*stock['shares']
    return profit, current_val

def make_report(portfolio, prices):
    data = []
    for stock in portfolio:
        current =prices[stock['name']] 
        change = current-stock['price']
        data.append((stock['name'],stock['shares'],current,change))
    return data

#read csvs
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

#get report data
data = make_report(portfolio,prices)


#print report
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-'*10+' ')*len(headers))

for name, shares, price, change in data:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')