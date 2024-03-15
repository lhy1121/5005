import fastf1
import csv

session = fastf1.get_session(2024, '2024 Bahrain Race', 'R')
session.load(telemetry = True)
ALB_pos = session.pos_data['23']
SAR_pos = session.pos_data['2']
ALB_pos.to_csv("ALB_pos.csv",columns = ALB_pos.columns,index = True,header = True)
SAR_pos.to_csv("SAR_pos.csv",columns = SAR_pos.columns,index = True,header = True)