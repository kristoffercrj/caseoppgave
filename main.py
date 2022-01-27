import requests
import argparse
import matplotlib.pyplot as plt

# Create a variable which represents the degree sign
degree_sign = u"\N{DEGREE SIGN}"

# Create parser for user inputs when runnning the code
parser = argparse.ArgumentParser()

# Add positional inputs for the user
parser.add_argument("latitude", type = float, help = "Specify the desired north coordinate you want to get weather data from. This is a float value between -90 and 90.")
parser.add_argument("longitude", type = float, help = "Specify the desired east coordinate you want to get weather data from. This is a float value between -180 and 180")
parser.add_argument("category", type = str, help = "Choose the category of weather data you want to display. The different inputs for categories can be found in the README.")
parser.add_argument("--current_weather", help = "Prints out information about the current weather")

args = parser.parse_args()

# Positional inputs that the user needs to add for the code to run
latitude = args.latitude # Input parameters for the user to write in latitude and longitude
longitude = args.longitude 
category = args.category # Input parameter to decide which category to display

print(f'You have entered the following coordinates: ({latitude}N, {longitude}E) \
\nSelected category for weather data: {category}')

# Extract information from the API
resp = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={float(latitude)}&longitude={float(longitude)}&hourly={category}&current_weather=true')

# Json parsing
generation_time = resp.json()['generationtime_ms'] # Extracts the time spent generating the weather data
y_values = resp.json()[f'hourly'][f'{category}'] # Extracts the y-values of the weather data
metric = resp.json()['hourly_units'][f'{category}'] # Extracts the metric of the weather data

# Some prints for information
print(f'Generating weather data for {category} at coordinates ({latitude}N, {longitude}E)... \n')

# Prints information about the current weather if specified
if args.current_weather:
    current_temp = resp.json()['current_weather']['temperature']
    time = resp.json()['current_weather']['time']
    windspeed = resp.json()['current_weather']['windspeed']
    winddirection = resp.json()['current_weather']['winddirection']

    print(f'CURRENT WEATHER FOR ({latitude}N, {longitude}E):')
    print(f'Current time: {time}')
    print(f'Current temperature: {current_temp} {degree_sign}C ')
    print(f'Current windspeed: {windspeed} km/h')
    print(f'Current wind direction: {winddirection}{degree_sign}')

print(f'\nFinishing generating after {round(generation_time, 4)} ms!')
print(f'Plotting data...')

# Plotting of the graph
plt.plot(y_values)
plt.ylabel(metric)
plt.xlim([0, 167]) # Temporary x-axis. One plot shows 168 hours of weather data
plt.xlabel('hours')
plt.title(f'{category} at {latitude}{degree_sign}N {longitude}{degree_sign}E')
print(f'Success!')
plt.show()
