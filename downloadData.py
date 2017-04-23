# -*- coding: utf-8 -*-

import pandas as pd
import quandl
import datetime
#import pandas.io.data
from pandas_datareader import data, wb
start = datetime.datetime(1990, 1, 1)
end = datetime.datetime(2016, 8, 31)
path = '/home/aditya/DMPA Project/StocksProject-master/datasets/'


## APPLE 
out =  data.get_data_yahoo('AA', start, end)

out.columns.values[-1] = 'AdjClose'
out.columns = out.columns + '_Out'
out['Return_Out'] = out['AdjClose_Out'].pct_change()

out.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/alcoa.csv')


## S&P - 500 ^GSPC Yahoo Finance
sp =  data.get_data_yahoo('^GSPC', start, end)

sp.columns.values[-1] = 'AdjClose'
sp.columns = sp.columns + '_SP500'
sp['Return_SP500'] = sp['AdjClose_SP500'].pct_change()

sp.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/sp.csv')

#plt.plot(sp['AdjClose_SP500'])
#plt.legend(('Dividend Adjusted Close Price S&P-500',))
#plt.show()


## Nasdaq Composite ^IXIC Yahoo Finance
nasdaq =  data.get_data_yahoo('^IXIC', start, end)

nasdaq.columns.values[-1] = 'AdjClose'
nasdaq.columns = nasdaq.columns + '_Nasdaq'
nasdaq['Return_Nasdaq'] = nasdaq['AdjClose_Nasdaq'].pct_change()

nasdaq.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/nasdaq.csv')

## Dow Jones Industrial Average (YFinance - Quandl)
djia =  quandl.get("YAHOO/INDEX_DJI", trim_start='1990-01-01', trim_end='2014-08-31', authtoken="mCDHcSdN9mQ_Hubid1Uq")

djia.columns.values[-1] = 'AdjClose'
djia.columns = djia.columns + '_Djia'
djia['Return_Djia'] = djia['AdjClose_Djia'].pct_change()

djia.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/djia.csv')

## 5 Years US Treasury YTM ^FVX Yahoo Finance
treasury =  data.get_data_yahoo('^FVX', start, end)

treasury.columns.values[-1] = 'AdjClose'
treasury.columns = treasury.columns + '_Treasury'
treasury['Return_Treasury'] = treasury['AdjClose_Treasury'].pct_change()

treasury.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/treasury.csv')

## Hong Kong Hang Seng ^HSI Yahoo Finance
hkong =  data.get_data_yahoo('^HSI', start, end)

hkong.columns.values[-1] = 'AdjClose'
hkong.columns = hkong.columns + '_HKong'
hkong['Return_HKong'] = hkong['AdjClose_HKong'].pct_change()

hkong.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/hkong.csv')

## Frankfurt DAX ^GDAXI Yahoo Finance
frankfurt =  data.get_data_yahoo('^GDAXI', start, end)
#frankfurt.tail()

frankfurt.columns.values[-1] = 'AdjClose'
frankfurt.columns = frankfurt.columns + '_Frankfurt'
frankfurt['Return_Frankfurt'] = frankfurt['AdjClose_Frankfurt'].pct_change()

frankfurt.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/frankfurt.csv')

## Paris CAC 40 ^FCHI Yahoo Finance
paris =  data.get_data_yahoo('^FCHI', start, end)

paris.columns.values[-1] = 'AdjClose'
paris.columns = paris.columns + '_Paris'
paris['Return_Paris'] = paris['AdjClose_Paris'].pct_change()

paris.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/paris.csv')

## Tokyo Nikkei-225 ^N225 Yahoo Finance
nikkei =  data.get_data_yahoo('^N225', start, end)

nikkei.columns.values[-1] = 'AdjClose'
nikkei.columns = nikkei.columns + '_Nikkei'
nikkei['Return_Nikkei'] = nikkei['AdjClose_Nikkei'].pct_change()

nikkei.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/nikkei.csv')

## London FTSE-100 ^FTSE Yahoo Finance 
london = data.get_data_yahoo('^FTSE', start, end)

london.columns.values[-1] = 'AdjClose'
london.columns = london.columns + '_London'
london['Return_London'] = london['AdjClose_London'].pct_change()

london.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/london.csv')

## Australia ASX-200 ^AXJO Yahoo Finance
australia = data.get_data_yahoo('^AXJO', start, end)

australia.columns.values[-1] = 'AdjClose'
australia.columns = australia.columns + '_Australia'
australia['Return_Australia'] = australia['AdjClose_Australia'].pct_change()

australia.to_csv('/home/aditya/DMPA Project/StocksProject-master/datasets/australia.csv')

########### RAW MATERIALS AND CURRENCIES
### Oil Price US Department for Energy (Quandl)
#oil =  Quandl.get("DOE/RWTC", trim_start='2008-01-01', trim_end='2014-08-15', authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#oil.columns = oil.columns + '_Oil'
#oil['Delta_Oil'] = oil['Value_Oil'].pct_change()
#
### Gold Price (Bundesbank - Quandl)
#gold = Quandl.get("BUNDESBANK/BBK01_WT5511", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#gold.columns = gold.columns + '_Gold'
#gold['Delta_Gold'] = gold['Value_Gold'].pct_change()
#
### Dollar in Euros Rate Exchange
#euro = Quandl.get("QUANDL/EURUSD", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#euro.columns = euro.columns + '_Euro'
#euro['Delta_Euro'] = euro['Rate_Euro'].pct_change()
#
### Dollar in Japanese Yen Rate Exchange
#yen = Quandl.get("QUANDL/USDJPY", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#yen.columns = yen.columns + '_Yen'
#yen['Delta_Yen'] = yen['Rate_Yen'].pct_change()
#
### Dollar in Australian Dollars Rate Exchange
#aud = Quandl.get("QUANDL/USDAUD", trim_start="2008-01-01", trim_end="2014-08-15", authtoken="mCDHcSdN9mQ_Hubid1Uq")
#
#aud.columns = aud.columns + '_Aud'
#aud['Delta_Aud'] = aud['Rate_Aud'].pct_change()
