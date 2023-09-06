import requests
# Get your own OpenWeather API by creating a free account at "https://openweathermap.org/"
# API Keys are required to make API Requests to the OpenWeather API.
API_KEY = "49fc8dbe79a58a9c34a6f8eb2dc65042"
MY_LAT = 19.194550
MY_LON = 73.190819
is_raining = False

rain_param = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily,alerts',
    'appid': API_KEY,
}

rain_response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=rain_param)

# If the requests.get() function generates 401 Errors, look into whether the onecall version 2.8 is still
# accessible to free OpenWeather Accounts.
rain_response.raise_for_status()

rain_data = rain_response.json()

rain_data_hourly = rain_data['hourly']

for hourly_index in range(0, 12):
    if rain_data_hourly[hourly_index]['weather'][0]['id'] < 700:
        is_raining = True
        print("Bring Umbrella")
        break

if is_raining is False:
    print("Don't bring Umbrella.")

