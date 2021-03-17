# pcost.py
#
# Exercise 1.27

from .report import read_portfolio
import csv
def portfolio_cost(filename):
    # with open (filename) as f:
    #     rows = csv.reader(f)
    #     header = next(rows)
    #     cost = 0
    #     for i,row in enumerate(rows,start =1):
    #         record =dict(zip(header,row))
    #         try:
    #             cost = cost+int(record['shares']) *float(record['price'])
    #         except ValueError:
    #             print(f"Row {i}: Couldn't convert: {row}")    
            
    #     return(cost)
    portfolio= read_portfolio(filename)
    return sum(s.shares*s.price for s in portfolio)

def main(argv):
    if len(args) !=2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename= argv[1]
    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__=='__main__':
    import sys
    main(sys.argv)