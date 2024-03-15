import pandas as pd

alb_r = pd.read_csv('ALB_R.csv')
speeds = ['Stint','SpeedI1','SpeedI2','SpeedFL','SpeedST']
speed_data = alb_r[speeds]
res = pd.DataFrame(columns=speeds)
for i in range(1,4):
    speed_data_tyre = speed_data[speed_data['Stint'] == i]
    avg_tyre_speed = speed_data_tyre.mean(axis = 0,skipna = True)
    res = res._append(avg_tyre_speed,ignore_index=True)
print(res)