import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

filename = 'Eminence IN Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows, humidity, direction, avg_wind, prcp, weather = [], [], [], [], [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%m-%d-%Y')
        try:
            high = (row[1])
            low = (row[2])
            humid = (row[3])
            wind_speed = (row[4])
            direct = (row[5])
            PRCP = (row[6])
            weathering = (row[7])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            humidity.append(humid)
            avg_wind.append(wind_speed)
            direction.append(direct)
            prcp.append(PRCP)
            weather.append(weathering)


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
weather = ['Overcast', 'Partly Sunny', 'Passing Clouds', 'Scattered Clouds', 'Light Rain', 'Thunder Shower', 'Sunny']
amount = [5, 25, 5, 15, 2, 1, 2]
ax.pie(amount, labels=weather, autopct='%1.2f%%')

plt.show()
