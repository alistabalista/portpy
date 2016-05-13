import getdata
import pandas as pd
import momport as mp
# stock_list = pd.read_excel("data/exsrk2015.xls", header=0)
# stock_list = stock_list[stock_list['INDEX'].notnull()]
# stock_list = stock_list['TICKER']
# son_data = getdata.DataGetter(stock_list, '01.01.2016')
# prices = son_data.get_px()
# prices.to_excel('data/monday_data.xlsx')
prices = pd.read_excel('data/monday_data.xlsx', header=0, index_col=0)
positions = mp.calc_mom(prices, 1, 0)
positions2 = mp.calc_mom(prices, 1, 0, resample_method='mean')
positions = positions['2016-05-06':].dropna(axis=1)
positions2 = positions2['2016-05-06':].dropna(axis=1)
print(positions, positions2)
