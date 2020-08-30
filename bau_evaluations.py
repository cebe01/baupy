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
        self.values = pd.read_csv(path, sep='\t')
        self.Raumgewicht = self.values.Raumgewicht
        self.Mächtigkeit = self.values.Mächtigkeit
        self.Ve = self.values.Ve
        self.We = self.values.We
        
        
    def av_raumgewicht(self):
        
        no_layers = len(self.values.Raumgewicht)
        av_raumgewicht = np.zeros(no_layers)
        thickness = np.zeros(no_layers)
        thickness[0] = self.values.Mächtigkeit[0]
        av_raumgewicht[0] = self.values.Raumgewicht[0]
        
        for i in range(1,no_layers):
            thickness[i] = self.Mächtigkeit[i] + thickness[i-1]
            av_raumgewicht[i] = (self.Raumgewicht[i]*self.Mächtigkeit[i] + av_raumgewicht[i-1]*thickness[i-1])/thickness[i]
        self.thickness = thickness
        self.av_raumgewicht = av_raumgewicht
        
    def Me(self):
        
        sigma_atm = 100
        Ve = self.Ve
        We = self.We
        thickness = self.thickness
        av_raumgewicht = self.av_raumgewicht
        Me_max = Ve*sigma_atm*(av_raumgewicht*thickness/sigma_atm)**We/1000
        thick_min = np.zeros(len(thickness))
        thick_min[1::] = thickness[0:-1]
        Me_min = Ve*sigma_atm*(av_raumgewicht*thick_min/sigma_atm)**We/1000
        self.Me_max = Me_max
        self.Me_min = Me_min
        
    def save_kennwerte(self):
        
        to_save = pd.DataFrame(self.values)
        to_save.loc[:,'Me_min'] = self.Me_min
        to_save.loc[:,'Me_max'] = self.Me_max
        to_save.to_excel('kennwerte.xlsx')
        
        
        

#%%



path = r'/home/cb/Dokumente/GitHub/baupy/kennwerte_streichholzstrasse.txt'


container = baupy(path)
container.av_raumgewicht()
container.Me()
container.save_kennwerte()
