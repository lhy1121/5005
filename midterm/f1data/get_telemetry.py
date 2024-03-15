import fastf1
import csv

session = fastf1.get_session(2024, '2024 Bahrain Race', 'R')
session.load(telemetry = True)
data = session.weather_data
print(data)
data.to_csv("Weather.csv",columns = data.columns,index = True,header = True)