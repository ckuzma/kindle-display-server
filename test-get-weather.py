import json
import requests
import datetime

"""
API REQUEST TESTS
"""

WEATHER_API_KEY = ""
WEATHER_LAT = "39.1648" # Bloomington, IN
WEATHER_LON = "-86.5262" # Bloomington, IN
WEATHER_URL = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=" + WEATHER_LAT + "&lon=" + WEATHER_LON + "&appid=" + WEATHER_API_KEY

# response = requests.get(WEATHER_URL)
# response = json.loads(response.text)
# print(json.dumps(response, indent=2))


"""
RESPONSE PARSING TESTS
"""

example_response = {
	"cod": "200",
	"message": 0.0179,
	"cnt": 96,
	"list": [{
		"dt": 1596632400,
		"main": {
			"temp": 289.16,
			"feels_like": 288.41,
			"temp_min": 289.16,
			"temp_max": 289.16,
			"pressure": 1013,
			"sea_level": 1013,
			"grnd_level": 1010,
			"humidity": 78,
			"temp_kf": 0
		},
		"weather": [{
			"id": 804,
			"main": "Clouds",
			"description": "overcast clouds",
			"icon": "04n"
		}],
		"clouds": {
			"all": 100
		},
		"wind": {
			"speed": 2.03,
			"deg": 252,
			"gust": 5.46
		},
		"visibility": 10000,
		"pop": 0.04,
		"sys": {
			"pod": "n"
		},
		"dt_txt": "2020-08-05 13:00:00"
	}],
	"city": {
		"id": 2643743,
		"name": "London",
		"coord": {
			"lat": 51.5085,
			"lon": -0.1258
		},
		"country": "GB",
		"timezone": 0,
		"sunrise": 1568958164,
		"sunset": 1569002733
	}
}
                     

                  
def convertKelvinToFahrenheit(kelvin_temp):
    """
    Converts kelvin_temp to Fahrenheit to the hundredth
    decimal place.
    """
    return format((kelvin_temp - 273.15) * 1.800 + 32, '.2f')

def convertUnixToTime(unix_timestamp):
    return datetime.datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d @ %H:%M:%S UTC')

def extractUsefulWeatherItems(openweather_response):
    return {
        'city': openweather_response['city']['name'],
        'sunrise': convertUnixToTime(openweather_response['city']['sunrise']),
        'sunset': convertUnixToTime(openweather_response['city']['sunset']),
        'current_temp': convertKelvinToFahrenheit(openweather_response['list'][0]['main']['temp']),
        'current_conditions': openweather_response['list'][0]['weather'][0]['description'],
        'daily_max': convertKelvinToFahrenheit(openweather_response['list'][0]['main']['temp_max']),
        'daily_min': convertKelvinToFahrenheit(openweather_response['list'][0]['main']['temp_min'])
    }

example_useful_weather = extractUsefulWeatherItems(example_response)
print(example_useful_weather)