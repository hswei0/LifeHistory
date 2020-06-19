# -*- coding: utf-8 -*-
"""
社會變遷生命史資料串連
Created on Fri Jun 19 14:45:18 2020
@author: hsuwei
"""

import os
import re
from pathlib import Path
import pandas as pd
import pyreadstat

os.chdir('C:/Users/user/Desktop/LifeHistory')

# input

df96, meta96 = pyreadstat.read_sav('./data/1996/tscs1996q2.sav',
                                   apply_value_formats=False,
                                   formats_as_category=False
                                   )

















# output
pyreadstat.write_sav(aa,
                     "data1xxxx.sav",
                     column_labels=var_lt, # 標籤
                     variable_value_labels=val_dict,
                     compress=True
                     )