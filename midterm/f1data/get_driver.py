import fastf1
import csv
import pandas as pd

session = fastf1.get_session(2024, '2024 Bahrain Race', 'R')
session.load(telemetry = True)
car_dict = session.car_data
ALB_car = car_dict['23']
ALB_car.to_csv("ALB_car.csv",columns = ALB_car.columns,index = True,header = True)
SAR_car = car_dict['2']
SAR_car.to_csv("SAR_car.csv",columns = SAR_car.columns,index = True,header = True)