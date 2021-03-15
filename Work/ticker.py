#ticker.py

from follow import follow
import csv
import report
import tableformat
import time

def convert_types(rows,types):
    for row in rows:
        yield [func(val) for func,val in zip(types,row)]

def make_dicts(rows,headers):
    for row in rows:
        yield dict(zip(headers,row))

def select_columns(rows,indices):
    for row in rows:
        yield [row[index] for index in indices]

def filter_symbols(rows,names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    rows = convert_types(rows,[str,float,float])
    rows = make_dicts(rows,['name','price','change'])
    return rows

def ticker(portfile, stockfile, fmt):

    portfolio= report.read_portfolio(portfile) 
    rows = parse_stock_data(follow(stockfile))
    rows = filter_symbols(rows,portfolio)
   
   #table formatter
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name','price','change'])

    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)

