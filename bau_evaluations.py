# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:27:21 2020

@author: Cb
"""

import numpy as np
import pandas as pd
import baupy as bp
#
        

#%%



path = '/home/cb/Dokumente/GitHub/baupy/kennwerte.xlsx'# r'/home/cb/Dokumente/GitHub/baupy/kennwerte_streichholzstrasse.txt'


container = bp.kennwerte(path)
#container.av_raumgewicht()
container.calc_Me()
container.save_kennwerte()
