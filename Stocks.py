# -*- coding: utf-8 -*-


#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#from Project import loadDatasets
from functions import *


#target = 'CLASSIFICATION'
target = 'REGRESSION'



lags = range(2,3)
print 'Maximum time lag applied', max(lags)
print ''

for maxdelta in range(3,5):
    
    datasets = loadDatasets('/home/aditya/DMPA Project/StocksProject-master/longdatasets')
    #print datasets

    delta = range(2,maxdelta)
    print 'Delta days accounted: ', max(delta)
    
    for dataset in datasets:
        columns = dataset.columns    
        adjclose = columns[-2]
        returns = columns[-1]
        for n in delta:
            addFeatures(dataset, adjclose, returns, n)
        dataset = dataset.iloc[max(delta):,:] # computation of returns and moving means introduces NaN which are nor removed
    
    finance = mergeDataframes(datasets, 6, target)
    
    print 'Size of data frame: ', finance.shape
    print 'Number of NaN after merging: ', count_missing(finance)
    
    finance = finance.interpolate(method='time')
    print 'Number of NaN after time interpolation: ', finance.shape[0]*finance.shape[1] - finance.count().sum()

    finance = finance.fillna(finance.mean())
    print 'Number of NaN after mean interpolation: ', (finance.shape[0]*finance.shape[1] - finance.count().sum())    
    #print finance
    back = -1
    finance.Return_SP500 = finance.Return_SP500.shift(back)
    
    finance = applyTimeLag(finance, lags, delta, back,target)
    
    #print 'Number of NaN after temporal shifting: ', count_missing(finance)
    
    print 'Size of data frame after feature creation: ', finance.shape   
    
    if target == 'CLASSIFICATION':
        performClassification(finance, 0.8)
        print ''
    
    elif target == 'REGRESSION':
        performRegression(finance, 0.8)
        print ''


    

