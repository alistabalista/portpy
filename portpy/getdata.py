import pandas as pd
import datetime
import Quandl
# TODO imkden stock listelerini update edecek birsey de yazmak gerek


class DataGetter():
    def __init__(self, ticker_list, start_date,
                 end_date=datetime.datetime.now()):
        self.ticker_list = ticker_list
        self.start_date = start_date
        self.end_date = end_date
        assert not isinstance(self.ticker_list, str)

    def get_px(self, price_type='Close', price_frequency='daily'):
        # stocklarin iterable birsey gelmesi gerek
        px_all = pd.DataFrame()
        for stock in self.ticker_list:
            try:
                px = Quandl.get("GOOG/IST_%s" % stock,
                                collapse=price_frequency,
                                trim_start=self.start_date,
                                trim_end=self.end_date,
                                authtoken="Vbxts9YuGDArmJJbie4e")
                px = px[price_type]
                px.name = stock
                px_all = pd.concat([px_all, px], axis=1)
            except Quandl.Quandl.DatasetNotFound:
                print(stock)
                continue
        # px_all.columns=self.ticker_list
        return px_all

    def get_index(self, index='XU030', price_type='Close',
                  price_frequency='daily'):
        px = Quandl.get("GOOG/INDEXIST_%s" % index,
                        collapse=price_frequency, trim_start=self.start_date,
                        trim_end=self.end_date,
                        authtoken="Vbxts9YuGDArmJJbie4e")
        return px[price_type]
if __name__ == "__main__":
    import time
    t0 = time.time()
    # stock_list = pd.read_excel("C:/Users/Ali Gokhan/Dropbox/
    # projeler/trading/data/ornek_kisa_liste.xls", header=0)
    stock_list = pd.read_excel("data/exsrk2015.xls", header=0)
    # bu sekilde tum endeski cekiyorum
    stock_list = stock_list[stock_list['INDEX'].notnull()]
    stock_list = stock_list['TICKER']
    son_data = DataGetter(stock_list, '01.01.2011')
    # prices = son_data.get_px()
    stock_index = son_data.get_index(index='XU030')
    #prices.to_excel('data/XU100_2014.xlsx')
    stock_index.to_frame(name='XU030').to_excel('ENDEKS_XU030_2014.xlsx', sheet_name='Sheet1')
    print(time.time()-t0)
