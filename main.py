import requests
import sys
import matplotlib.pyplot as plt

'''
Inputs:
latitude: float
longitude: float
category: string
'''

# Create a variable which represents the degree sign
degree_sign = u"\N{DEGREE SIGN}"

# To control that the user enters the correct amount of arguments
if (len(sys.argv) > 4):
    print('You have entered too many arguments.')
    sys.exit()

elif (len(sys.argv) < 2):
    print(' You have entered too few arguments.')
    sys.exit()

# Inputs for the code to run
latitude = sys.argv[1] # Input parameters for the user to write in latitude and longitude
longitude = sys.argv[2] 
category = sys.argv[3] # Input parameter to decide which category to display

# Extract information from the API
resp = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={float(latitude)}&longitude={float(longitude)}&hourly={category}')

# Json parsing
y_values = resp.json()['hourly'][f'{category}'] # Extracts the y-values of the weather data
metric = resp.json()['hourly_units'][f'{category}'] # Extracts the metric of the weather data

# Plotting of the graph
plt.plot(y_values)
plt.ylabel(metric)
plt.title(f'{category} at {latitude}{degree_sign}N {longitude}{degree_sign}E')
plt.show()