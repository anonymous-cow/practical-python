#stock.py

#exercise 4.1

class Stock():
    def __init__(self,name, shares, price):
        self.name=name
        self.shares=shares
        self.price=price
    def sell(self,stocks):
        self.shares=self.shares-stocks
    def cost(self):
        return self.shares*self.price
    def __repr__(self):
        return (f'Stock({self.name}, {self.shares}, {self.price})')
