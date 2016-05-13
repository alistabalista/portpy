import pandas as pd
# TODO: tatil gunlerinde ne yaptigina bak 


def calc_mom(price, lookback, lag, cutoff=6, resample='W-FRI',
             resample_method='last'):
    price = price.resample(resample, how=resample_method)
    mom_ret = price.shift(lag).pct_change(lookback)
    ranks = mom_ret.rank(axis=1, ascending=False)
    print(ranks)
    if cutoff == 'all':
        positions = ranks[ranks < ranks.mean(axis='index')]
    else:
        positions = ranks[ranks < cutoff]
    positions[positions.notnull()] = 1
    return positions


if __name__ == "__main__":
    # son_price = pd.read_csv('C:/Users/ag2270/Dropbox/projeler/trading/data/ornek_price.csv',index_col = 0, parse_dates = True)
    # xu030 = pd.read_csv('C:/Users/ag2270/Dropbox/projeler/trading/data/ornek_endeks.csv',index_col = 0, parse_dates = True)
    prices = pd.read_excel('data/data.xlsx', 'stock', index_col=0)
    positions = calc_mom(prices, 1, 0)
    positions2 = calc_mom(prices, 1, 0, resample_method='mean')
    #positions.to_excel('data/temp_positions.xlsx')
    