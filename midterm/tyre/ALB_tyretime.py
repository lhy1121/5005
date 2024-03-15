import pandas as pd
import numpy as np
from datetime import datetime

alb_r = pd.read_csv('ALB_R.csv')
time = alb_r[['PitInTime','PitOutTime']]
res = []
for i in range(len(time['PitInTime'])):
    if type(time['PitInTime'][i]) == str:
        s1 = time['PitInTime'][i]
        s2 = time['PitOutTime'][i+1]
        t1 = s1.split(' ')
        t1 = t1[2].split('.')
        point1 = '0.' + t1[1]
        t1 = t1[0]
        t2 = s2.split(' ')
        t2 = t2[2].split('.')
        point2 = '0.'+ t2[1]
        d1 = float(point2) - float(point1)
        t2 = t2[0]
        time_format = "%H:%M:%S"
        time1 = datetime.strptime(t1, time_format)
        time2 = datetime.strptime(t2, time_format)
        d2 = time2 - time1
        time_string = str(d2)
        time_arr = time_string.split(":")
        result = float(time_arr[2]) + d1
        res.append(result)
        print(result)
