import fastf1
import csv

session = fastf1.get_session(2024, '2024 Bahrain Race', 'R')
session.load(telemetry = True)
data = session.laps
alb = data[data['DriverNumber'] == '23']
sar = data[data['DriverNumber'] == '2']
alb.to_csv("ALB_R.csv",columns = alb.columns,index = True,header = True)
sar.to_csv("SAR_R.csv",columns = sar.columns,index = True,header = True)

