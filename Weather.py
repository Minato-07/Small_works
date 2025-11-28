from http.client import responses

import requests

def get_weather(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        current_weather = data['current']
        print(f"Weather in {city}:")
        print(f"Temperature: {current_weather['temp_c']}°C")
        print(f"Condition: {current_weather['condition']['text']}")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Wind Speed: {current_weather['wind_kph']}kph")
    else:
        print(f"Error: {data['error']['message']}")

def weather_app():
    city = input("Enter the city name: ")
    api_key = "28a2eaf83aa64b1487a151459252811"
    get_weather(city, api_key)

weather_app()