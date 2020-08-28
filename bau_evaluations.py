# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:27:21 2020

@author: Cb
"""

import numpy as np
import pandas as pd
# baupy

#%%

class baupy():
    
    def __init__(self, path):
        
        self.path = path
        self.values = pd.read_csv(path, sep=';')
        self.Raumgewicht = self.values.Raumgewicht
        self.Mächtigkeit = self.values.Mächtigkeit
        
    def av_raumgewicht(self):
        
        no_layers = len(self.values.Raumgewicht)
        av_raumgewicht = np.zeros(no_layers)
        thickness = np.zeros(no_layers)
        thickness[0] = self.values.Mächtigkeit[0]
        av_raumgewicht = self.values.Raumgewicht[0]
        for i in range(1,no_layers):
            print(i)
            thickness[i] = self.Mächtigkeit[i] + thickness[i-1]
            av_raumgewicht[i] = (self.Raumgewicht[i]*self.Mächtigkeit[i] + av_raumgewicht[i-1]*thickness[i-1])*thickness[i]
        self.thickness = thickness
        self.av_raumgewicht = av_raumgewicht
        
        

#%%



path = r'C:\Users\CB.MAGMA\Documents\GitHub\baupy\kennwerte_streichholzstrasse.csv'


container = baupy(path)
container.av_raumgewicht()
