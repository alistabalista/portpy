import pandas as pd


class Cash:

    def __init__(self, volume=0, currency='TRY', buy_price=1, sell_price=1):
        self.currency = currency
        self.volume = volume
        self.buy_price = buy_price  # buy & sell price represent FX rates
        self.sell_price = sell_price


class TimeDeposit(Cash):

    def __init__(self, volume=0, currency='TRY',
                 buy_price=1, sell_price=1, maturity=0, ytm=0):
        super().__init__(currency, volume, buy_price, sell_price)
        # buy & sell price represent FX rates
        self.maturity = maturity
        self.ytm = ytm

    def simple_return(self):
        return self.volume*self.ytm/365*self.maturity


class Equity(Cash):

    def __init__(self, Ticker, volume=0, buy_price=0, sell_price=0):
        super().__init__(volume, buy_price, sell_price)
        self.buy_price = buy_price
        self.sell_price = sell_price

if __name__ == "__main__":
	deneme = TimeDeposit('TRY',100,1,1,365,.10)
	print(deneme.ytm)
	print(deneme.simple_return())