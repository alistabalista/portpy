import numpy as np
import pandas as pd


def calc_return():
    pass


def calc_depo_return(volume, ytm=0, maturity=0, fx_rate=1):
    return volume*ytm/365*maturity*fx_rate



def calc_histvol(price):
    returns = price.pct_change()  # not using log returns
    return np.sqrt(252*returns.var())


def calc_series_histvol(series, window=22):
    vols = pd.Series(None, index=series.index)
    for endeks in range(window, len(series)):
        vol = calc_histvol(series[endeks-window:    endeks])
        vols.iloc[endeks] = vol.values
    return vols
if __name__ == "__main__":
    # stock_index = pd.read_excel('data/test_index.xls','Sheet1',index_col=0)
    # vols = calc_series_histvol(stock_index)
    import Quandl
    trl = Quandl.get("BOE/XUDLBK75", authtoken="Vbxts9YuGDArmJJbie4e",
                     trim_start='01.01.2016')
    trl_vols = calc_series_histvol(trl)
    pln = Quandl.get("BOE/XUDLBK49", authtoken="Vbxts9YuGDArmJJbie4e",
                     trim_start='01.01.2016')
    pln_vols = calc_series_histvol(pln)
    (trl_vols-pln_vols).plot()
