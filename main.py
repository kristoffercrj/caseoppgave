import requests
import argparse
import matplotlib.pyplot as plt

'''
Inputs:
latitude: float
longitude: float
category: string
'''

# Create a variable which represents the degree sign
degree_sign = u"\N{DEGREE SIGN}"

# Create parser
parser = argparse.ArgumentParser()
parser.add_argument("latitude", type = float, help = "Specify the desired north coordinate you want to get weather data from. This is a float value between -90 and 90.")
parser.add_argument("longitude", type = float, help = "Specify the desired east coordinate you want to get weather data from. This is a float value between -180 and 180")
parser.add_argument("category", type = str, help = "Choose between the following categories: \n temperature_2m")

args = parser.parse_args()

# Positional inputs that the user needs to add for the code to run
latitude = args.latitude # Input parameters for the user to write in latitude and longitude
longitude = args.longitude 
category = args.category # Input parameter to decide which category to display

print(f'You have entered the coordinates: ({latitude}N, {longitude}E) \
\nSelected category for weather data: {category}')

# Extract information from the API
resp = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={float(latitude)}&longitude={float(longitude)}&hourly={category}')

# Json parsing
generation_time = resp.json()['generationtime_ms'] # Extracts the time spent generating the weather data
y_values = resp.json()['hourly'][f'{category}'] # Extracts the y-values of the weather data
metric = resp.json()['hourly_units'][f'{category}'] # Extracts the metric of the weather data

print(f'Generating weather data for {category} at coordinates ({latitude}N, {longitude}E) ...')
print(f'Finishing generating after {round(generation_time, 4)} ms!')
print(f'Plotting data...')

# Plotting of the graph
plt.plot(y_values)
plt.ylabel(metric)
plt.xlim([0, 167])
plt.xlabel('hours')
plt.title(f'{category} at {latitude}{degree_sign}N {longitude}{degree_sign}E')
print(f'Success!')
plt.show()
