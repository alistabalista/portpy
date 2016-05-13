import pandas as pd


class Backtest(object):
    def __init__(self, positions, prices, end_date='None'):
        assert isinstance(positions, pd.DataFrame), 'Positions should be DFs'
        assert isinstance(prices, pd.DataFrame), 'Prices should be DFs'
        self.positions = positions
        # fiyat serisindeki endeksi pozisyondakine esitliyorum
        prices = prices.loc[positions.index]
        prices.fillna(method='pad', inplace=True)
        self.prices = prices
        self.start_date = pd.to_datetime(prices.index.min(), dayfirst=True)
        self.end_date = pd.to_datetime(prices.index.max(), dayfirst=True)

    def calc_ret(self, start_date=None):
        if start_date is None:
            start_date = self.start_date
        returns = self.prices[start_date:].pct_change()
        returns = returns.shift(-1)
        port_return = returns * positions
        return port_return.mean(axis=1)

    def calc_cum_ret(self, start_date=None, index_data=None,
                     index_resample='W-FRI'):
        port_return = self.calc_ret(start_date)
        if index_data is not None:
            index_data = index_data.resample(index_resample, how='last')
            index_data = index_data.loc[self.positions.index]
            index_returns = index_data[start_date:].pct_change()
            index_returns = index_returns.shift(-1)
            port_return = port_return.subtract(index_returns)
        port_return = port_return.dropna()
        index = (1 + port_return).cumprod()
        index.values[0] = 1
        return index

    # def calc_index_cum_ret(self, index_data, start_date=None):
    #     if start_date is None:
    #         start_date = self.start_date
    #     index_data = index_data.loc[self.positions.index]
    #     returns = index_data[start_date:].pct_change()
    #     returns = returns.shift(-1)
    #     index = (1 + returns).cumprod()
    #     index.values[0] = 1
    #     return index

if __name__ == "__main__":

    # mevduat karsilastirmasi

    # import numpy as np
    # import calculation_tools as ct
    # rates = pd.read_csv('data/mevduat_faiz.csv',
    #                     index_col=0, parse_dates=True, dayfirst=True)
    # stock = pd.read_csv('data/uzun_endeks.csv', index_col=0,
    #                     parse_dates=True, dayfirst=True)
    # stock = stock.loc[~ (stock == 0).all(axis=1)]
    # stock.dropna
    # di = {'deposit': np.random.uniform(0, 1, len(rates.index))}
    # positions = pd.DataFrame(di, index=rates.index)
    # positions['stock'] = pd.Series(1 - positions['deposit'],
    #                                index=positions.index)
    # depo_returns = {'depo_returns':
    #                 ct.calc_depo_return(1, rates['1m'], 7) / 100}
    # returns = pd.DataFrame(depo_returns, index=rates.index)
    # returns = returns.merge(stock, left_index=True, right_index=True)
    # returns['XU100'] = returns['XU100'].pct_change()
    # exported = ((1 + returns['20160101':]).cumprod())
    # exported.to_excel('data/exported.xlsx')
    #

    import momport as mp

    prices = pd.read_excel('data/data.xlsx', 'stock', index_col=0)
    endeks = pd.read_excel('data/data.xlsx', 'index', index_col=0)
    endeks = endeks['XU030']
    positions_avg = mp.calc_mom(prices, 1, 0, resample_method='mean')
    positions = mp.calc_mom(prices, 1, 0)
    momentum = Backtest(positions, prices)
    momentum_avg = Backtest(positions_avg, prices)
    port_returns = pd.DataFrame(momentum.calc_cum_ret('2015-01-01'))
    port_returns_avg = pd.DataFrame(momentum_avg.calc_cum_ret('2015-01-01'))
    port_returns.plot()
    port_returns_avg.plot()
    
    # port_returns_hedged = pd.DataFrame(momentum.calc_cum_ret('2015-01-01',endeks))
    # temp = port_returns.merge(port_returns_hedged,left_index=True,right_index=True)

  
