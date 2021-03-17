# report.py
#
# Exercise 2.4
from .fileparse import parse_csv
import csv
from .stock import Stock
from .portfolio import Portfolio

from . import tableformat
def read_portfolio(filename,**opts):
    with open(filename) as lines:
        return Portfolio.from_csv(lines,**opts)
    '''computes the total cost (shares*price) of a portfolio file'''
    # with open (filename) as lines:
    #     portdict= parse_csv(lines, select=['name','shares','price'], types=[str, int, float],**opts)
    #     portfolio=[ Stock(**d) for d in portdict]
    #     return Portfolio(portfolio)
    #portfolio=[]

    #with open(filename,'rt') as f:
     #   rows=csv.reader(f)
      #  headers= next(rows)
       # for row in rows:
        #    record = dict(zip(headers,row))
         #   holding ={'name':record['name'], 'shares':int(record['shares']), 'price':float(record['price'])}
          #  #holding = (row[0], int(row[1]), float(row[2]))
           # portfolio.append(holding)
    
    #return portfolio

def read_prices(filename):
    '''reads current prices of stocks'''
    #prices={}
    #with open(filename, 'rt') as f:
    #    rows = csv.reader(f)
    #    for row in rows:
    #        try:
    #            prices[row[0]]=float(row[1])
    #        except IndexError:
    #            pass

    #return prices
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))
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
    for s in portfolio:
        current =prices[s.name] 
        change = current-s.price
        data.append((s.name,s.shares,current,change))
    return data

def print_report(data,formatter):
    #print report
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    #print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    #print(('-'*10+' ')*len(headers))

    for name, shares, price, change in data:
        #price = '$'+str(f'{price:0.2f}')
        #print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
        rowdata=[name, str(shares),f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)



def portfolio_report(portfile, pricefile,fmt='txt'):
    #read csvs
    portfolio = read_portfolio(portfile)
    prices = read_prices(pricefile)

    #get report data
    data = make_report(portfolio,prices)

    #print report:
    formatter = tableformat.create_formatter(fmt)
    print_report(data,formatter)


def main(args):
    if len(args)!=4 :
        raise SystemExit(f'Usage {args[0]} portfile price file')
    #import logging
    # logging.basicConfig(
    #     filename='app.log',
    #     filemode='w',
    #     level= logging.WARNING,
    # )
    portfolio_report(args[1], args[2], args[3])

if __name__== '__main__':
    import sys
    main(sys.argv)
