# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:52:10 2021

@author: Rohan Jacob
"""

# #!pip install pywebio
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *

import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('file_reg_2.pkl', 'rb'))
data=pd.read_csv('D:\\MD_df.csv')
dp=pd.DataFrame(data=data,columns=['Cause of death','cause_num'])
df2 = dp.drop_duplicates(subset=['Cause of death','cause_num'])
df1=df2.sort_values(by='cause_num', ascending=True)

#pd.set_option("display.max_rows", None, "display.max_columns", None)
app = Flask(__name__)


def predict():
    Year = input("income_bucket：", type=NUMBER)
    Present_Price = input("Population", type=NUMBER)
    k=select("Select disease", df1['Cause of death'])
    c=df1['cause_num'][df1['Cause of death'] ==k ].values[0]
    prediction = model.predict([[Year,Present_Price,c]])
    output = round(prediction[0],0)
  
    put_text('No of Deaths:',output)
    
app.add_url_rule('/tool', 'webio_view', webio_view(predict),
                     methods=['GET', 'POST', 'OPTIONS'])
app.run(host='localhost', port=80)

#visit http://localhost/tool