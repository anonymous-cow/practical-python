# pcost.py
#
# Exercise 1.27


import csv
def portfolio_cost(filename):
    with open (filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        cost = 0
        for i,row in enumerate(rows,start =1):
            try:
                #row=line.split(',')
                cost = cost+int(row[1]) *float(row[2])
            except ValueError:
                print(f"Row {i}: Couldn't convert: {row}")    
            
        return(cost)



filename='Data/missing.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)