# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:20:23 2020

@author: Cb
"""

import numpy as np
import pandas as pd

class kennwerte():
    
    def __init__(self, path):
        
        self.path = path
        self.values = pd.read_excel(path)#, sheetname=None)
        self.Raumgewicht = self.values.Raumgewicht 
        self.Mächtigkeit = self.values.Mächtigkeit
        try: self.Ve = self.values.Ve
        except: pass
        try: self.We = self.values.We
        except: pass
        self.Material = self.values.Material
        try: self.thickness = self.values.Thickness 
        except: pass
        self.Kohäsion = self.values.Kohäsion
        self.Reibungswinkel = self.values.Reibungswinkel
        
    
    def calc_thickness(self):
        no_layers = len(self.values.Raumgewicht)

        thickness = np.zeros(no_layers)
        thickness[0] = self.values.Mächtigkeit[0]
        
        for i in range(1,no_layers):
            thickness[i] = self.Mächtigkeit[i] + thickness[i-1]
        self.thickness = thickness
    
    def calc_av_raumgewicht(self):
        
        try: self.thickness
        except: self.calc_thickness()
        
        thickness = self.thickness
        no_layers = len(self.values.Raumgewicht)
        av_raumgewicht = np.zeros(no_layers)
        av_raumgewicht[0] = self.values.Raumgewicht[0]
        
        for i in range(1,no_layers):
            av_raumgewicht[i] = (self.Raumgewicht[i]*self.Mächtigkeit[i] + av_raumgewicht[i-1]*thickness[i-1])/thickness[i]
        self.av_raumgewicht = av_raumgewicht
        
    def calc_Me(self):
        
        try: self.av_raumgewicht
        except: self.calc_av_raumgewicht()
        
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
        
        to_save = pd.DataFrame()
        to_save.loc[:,'Material'] = self.Material
        to_save.loc[:,'Mächtigkeit'] = self.Mächtigkeit
        to_save.loc[:, 'Thickness'] = self.thickness
        to_save.loc[:,'Raumgewicht'] = self.Raumgewicht
        to_save.loc[:,'Reibungswinkel'] = self.Reibungswinkel
        to_save.loc[:,'Kohäsion'] = self.Kohäsion
        to_save.loc[:,'Me_min'] = self.Me_min
        to_save.loc[:,'Me_max'] = self.Me_max
        to_save.to_excel('kennwerte.xlsx')
        
    def calc_slope(self, hmax):#, gw_level):
        
        sicherheit = 1.2
        
        h = np.arange(0, int(hmax), 0.5)
        
        thick_int = np.arange(0,np.max(self.thickness),0.5)
        thickness = np.zeros(len(self.thickness)+1)
        thickness[1::] = self.thickness
        
        rg = np.zeros(len(thick_int))
        mat = np.zeros(len(thick_int))
        co = np.zeros(len(thick_int))
        av_rg = np.zeros(len(thick_int))
        phi = np.zeros(len(thick_int))
        c=0
        for k in np.arange(len(self.thickness)):
            for i in np.arange(c,len(thick_int)):
                if thick_int[i] < self.thickness[k]:
                    rg[c] = self.Raumgewicht[k]
                    co[c] = self.Kohäsion[k]
                    phi[c] = self.Reibungswinkel[k]
                    # if thick_int[i]> gw_level:
                    #     rg[c] = rg[c] - 10
                    c = c+1
        print(rg)
        av_rg = np.zeros(len(thick_int))
        for i in range(1,len(thick_int)):
            av_rg[i] = np.mean(rg[0:i]) 
        
        phi = np.radians(phi)
        
        phi2 = np.arctan(np.tan(phi)*(np.tan(phi)/sicherheit))
        
        c2 = co/sicherheit
        
        h1 = av_rg*thick_int
        
        N = av_rg*h1/c2
        
        
        
        
        
        
        