# Caseoppgave

## Prerequisistes
To run the code, you need to install the following python packages:

```
requests
matplotlib
```
You can install these packages by running

```
pip install -r requirements.txt
```

## Open-Meteo API
The code uses data from the Open-Meteo API. A link to their API can be found here: https://open-meteo.com/en/docs.

## How to use the program
You need to run the code directly from the command-line interface (CLI). It can be run by typing:

```
python main.py [latitude] [longitude] [category]
```

`[latitude]` is a float value between -90 and 90 degrees.
`[longitude]` is a float value between -180 and 180 degrees.
`[category]` is a string that selects which weather data to display. Currently the program only supports:

```
temperature_2m - Air temperature at 2 meters above ground
windspeed_10m - Wind speed at 10 meters above ground
windspeed_80m - Wind speed at 80 meters above ground
windspeed_120m - Wind speed at 120 meters above ground
windspeed_180m - Wind speed at 180 meters above ground
winddirection_10m - Wind direction at 10 meters above ground
winddirection_80m - Wind direction at 80 meters above ground
winddirection_120m - Wind direction at 120 meters above ground
winddirection_180m - Wind direction at 180 meters above ground
windgusts_10m - Wind gusts at 10 meters above ground
```
More detailed information can be found in the documentation of the API: https://open-meteo.com/en/docs.

An example of how it can be run with different inputs:
```
python main.py 3.2 4.5 windspeed_10m
python main.py 25.2 10 temperature_2m
python main.py 24 24 windgusts_10m
```
