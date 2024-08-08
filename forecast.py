import requests
import re

api_key_regex = re.compile(r'^[a-f0-9]{32}$')  # 32 hexadecimal characters
city_regex = re.compile(r'^[a-zA-Z0-9\s]+$')  # alphanumeric alphabets and also contain spaces
humidity_regex = re.compile(r'^(100|[1-9]?[0-9])$') # 0-100
wind_speed_regex = re.compile(r'^\d+(\.\d+)?$')  # check positive float value
temperature_regex = re.compile(r'^\d+(\.\d+)?$') # check float)
weather_condition_regex = re.compile(r'^[a-zA-Z0-9\s]+$') #  alphanumeric alphabets and also contain spaces

def get_weather_data(city):
    try:
        api_key = 'c6df13aac9d45459b2f3e9026e3b2dea'
        if not api_key_regex.match(api_key):
            print('Invalid API key format.')
            return

        if not city_regex.match(city):
            print'Invalid City name format.')
            return

        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(api_url)
        response.raise_for_status() 
        weather_data = response.json()

        humidity = weather_data['main']['humidity']
        if not humidity_regex.match(str(humidity)):
            print('Invalid humidity value received from the API.')
            return

        wind_speed = weather_data['wind']['speed']
        if not wind_speed_regex.match(str(wind_speed)):
            print('Invalid wind speed value received from the API.')
            return

        temperature = weather_data['main']['temp']
        if not temperature_regex.match(str(temperature)):
            print('Invalid temperature value received from the API.')
            return

        weather_condition = weather_data['weather'][0]['description']
        if not weather_condition_regex.match(weather_condition):
            print('Invalid weather condition value received from the API.')
            return

        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Weather Condition: {weather_condition}')
    except Exception as error:
        print(f'Failed to retrieve weather data. Error: {error}')

city_to_scrape = 'Lahore'
get_weather_data(city_to_scrape)










