# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:20:23 2020

@author: Cb
"""

import numpy as np
import pandas as pd
class baupy():
    
   
    
    def __init__(self, path):
        
        self.path = path
        self.values = np.load(path)
        
    # def calc_Me(self):
    #     for 
        
        