# pcost.py
#
# Exercise 1.27


import sys
import csv
def portfolio_cost(filename):
    with open (filename) as f:
        rows = csv.reader(f)
        cost = 0
        for row in rows:
            try:
                #row=line.split(',')
                cost = cost+int(row[1]) *float(row[2])
            except ValueError:
                print("warning, invalid literal")
            print(row)
        return(cost)

if len(sys.argv)==2:
    filename= sys.argv[1]
else:
    filename='practical-python/Work/Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)