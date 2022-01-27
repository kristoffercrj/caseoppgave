# Caseoppgave
This is a script that extracts weather data from the Open-Meteo API and plots it as a graph.

## Prerequisites
To run the code, you need to install the following python packages:

```
requests
argparse
matplotlib
```
You can install these packages by running

```
pip install -r requirements.txt
```

Or by manually installing them with `pip install`

## Open-Meteo API
The code uses data from the Open-Meteo API. A link to their API can be found here: https://open-meteo.com/en/docs.

## How to use the program
You need to run the code directly from the command-line interface (CLI). It can be run by typing:

```
python main.py [latitude] [longitude] [category] --current_weather 1
```

`[latitude]` is a float value between -90 and 90 \
`[longitude]` is a float value between -180 and 180 \
`[category]` is a string that selects which weather data to display. The supported categories from the API are shown in the table underneath.
`--current_weather 1` is an optional argument and provides printout of the current weather to your terminal. 

| Category | Description |
| --- | --- |
| temperature_2m | Air temperature at 2 meters above ground |
| windspeed_10m | Wind speed at 10 meters above ground |
| windspeed_80m | Wind speed at 80 meters above ground |
| windspeed_120m | Wind speed at 120 meters above ground |
| windspeed_180m | Wind speed at 180 meters above ground |
| winddirection_10m | Wind direction at 10 meters above ground |
| winddirection_80m | Wind direction at 80 meters above ground |
| winddirection_120m | Wind direction at 120 meters above ground |
| winddirection_180m | Wind direction at 180 meters above ground |
| windgusts_10m | Wind gusts at 10 meters above ground |
| soil_temperature_0cm | Temperature in the soil at 0 cm |
| soil_temperature_6cm | Temperature in the soil at 6 cm  |
| soil_temperature_18cm | Temperature in the soil at 18 cm  |
| soil_temperature_24cm | Temperature in the soil at 24 cm  |

You can also get information by running `python main.py -h` or `python main.py --help` in your command line. \
More detailed information can be found in the documentation of the API: https://open-meteo.com/en/docs.

## Examples
Some examples to show how to use the code:

Output of `python main.py 25.2 10 temperature_2m`:
```
You have entered the following coordinates: (25.2N, 10.0E)
Selected category for weather data: temperature_2m
Generating weather data for temperature_2m at coordinates (25.2N, 10.0E)...

Finishing generating after 8.613 ms!
Plotting data...
Success!
```

<p align = "center">
<img width = "500" height = "400" src = "images/temperature_2m.png">
</p>

Output of `python main.py 3.2 4.5 windspeed_10m`:
<p align = "center">
<img width = "500" height = "400" src = "images/windspeed_10m.png">
</p>

An example of running `python main.py 25.2 10 temperature_2m --current_weather 1` will show something like this:

```
You have entered the following coordinates: (25.2N, 10.0E)
Selected category for weather data: temperature_2m
Generating weather data for temperature_2m at coordinates (25.2N, 10.0E)...

CURRENT WEATHER FOR (25.2N, 10.0E):
Current time: 2022-01-27T09:00
Current temperature: 8.9 °C
Current windspeed: 13.5 km/h
Current wind direction: 135° 

Finishing generating after 8.613 ms!
Plotting data...
Success!
```


