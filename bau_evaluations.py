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



path = r'X:\Cb\20 198 Baugrund Haspelstrasse Niederhasli\Berechnungen\kennwerte.xlsx'# r'/home/cb/Dokumente/GitHub/baupy/kennwerte_streichholzstrasse.txt'


container = bp.kennwerte(path)
container.calc_thickness()
container.calc_av_raumgewicht()
container.calc_Me()
container.save_kennwerte()
#container.calc_slope(5,3)
