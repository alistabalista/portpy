import datetime
from datetime import date
import pandas as pd
import numpy as np

class Portfolio(object):
#TODO TUM STRATEJI PORTFOLIOLARINI BIRARADA GOSTERECEK BIRSEY YAZ
#TODO: risk free rate'i de koy   

    def __init__(self,positions,prices,end_date='None'):
        self.positions = positions
        #fiyat serisindeki endeksi pozisyondakine esitliyorum
        prices = prices.loc[positions.index]
        prices.fillna(method='pad',inplace=True)
        self.prices = prices
        #self.stock_index = pd.DataFrame(0,index = positions.index, \
        #columns = ['EMPTY'])
        self.start_date = pd.to_datetime(prices.index.min(),dayfirst=True)
        self.end_date = pd.to_datetime(prices.index.max(),dayfirst=True)
    def calc_returns(self):
        returns = self.prices.pct_change()
        returns = returns.shift(-1)
        port_return = returns*positions
        return port_return.sum(axis=1)
    def calc_cum_returns(self,hedge_ratio=0,stock_index='EMPTY'):
        prices=self.prices.join(stock_index)
        self.positions['Close'] = pd.Series(-1*hedge_ratio,index=positions.index)
        returns = prices.pct_change()
        returns = returns.shift(-1)
        port_return = returns*self.positions
        port_return = port_return.iloc[:,:-1].mean(axis=1)-port_return.iloc[:,-1]
        index = (1 + port_return).cumprod()
        index.values[0] = 1
        return index

if __name__ == "__main__":
    import momport as mom
    prices = pd.read_excel('data/test_data.xls','Sheet1',index_col=0)
    stock_index = pd.read_excel('data/test_index.xls','Sheet1',index_col=0)
    positions = mom.calc_mom (prices,1,0)
    portfolio = Portfolio(positions,prices)
    cum_ret=portfolio.calc_cum_returns(stock_index=stock_index,hedge_ratio = 1)
    positions2 = mom.calc_reversion(prices,1,0)
    portfolio2 = Portfolio(positions2,prices)
    cum_ret2=portfolio2.calc_cum_returns(stock_index=stock_index,hedge_ratio = 1)
    cum_ret.plot()
    cum_ret2.plot()
    #stock_index.plot()

    #cum_ret=portfolio.calc_cum_returns(stock_index=stock_index,hedge_ratio = 1)
    #cum_ret.plot()    
    
    