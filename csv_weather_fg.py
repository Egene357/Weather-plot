#Diagram comparing air temperature in the desert of Death Valley and in Sitka.

import csv
from datetime import datetime
from matplotlib import pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    """Get the highs and lows from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try: #error checking code to handle exceptions that may occur while parsing datasets
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Get weather data for Sitka.
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=5, low_index=6)
# Plot Sitka weather data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='orange', alpha=0.5)
ax.plot(dates, lows, c='yellow', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for Death Valley.
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=4, low_index=5)
# Add Death Valley data to current plot.
plt.style.use('seaborn')
ax.plot(dates, highs, c='red', alpha=0.5) #alpha - color level
ax.plot(dates, lows, c='orange', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.15) #fill_between() передается список dates для значений x и две серии значений y highs и lows. 
#facecolor - fill area color


# Format plot.
title = "Daily high and low temperatures - 2018"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()

