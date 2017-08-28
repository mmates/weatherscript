import requests
import json


city = input("Enter the city name to know Weather: ")
url= "http://api.openweathermap.org/data/2.5/weather?q="+city+",uk&appid=55976b2324330fb52de6bdfa9b6530fc"

data = requests.get(url)
read = data.json()


name = read['name']
country = read['sys']['country']
temperatureK = read['main']['temp'] - 273.15
temperatureC = round(temperatureK, 2)
humidity = read['main']['humidity']
pressure = read['main']['pressure']
wind = read['wind']['speed']
description = read['weather'][0]['description']


print("\nCity: {}" .format(read['name']))
print("Country: {}" .format(read['sys']['country']))
print("Temperature: {} C" .format(temperatureC))
print("Humidity: {}" .format(read['main']['humidity']))
print("Pressure: {}" .format(read['main']['pressure']))
print("Wind speed: {}" .format(read['wind']['speed']))
print("Description: {}" .format(read['weather'][0]['description']))

weather_book = {}
weather_book['lua_integration'] = {
    'city': name,
    'country': country,
    'temperature': temperatureC,
    'humidity': humidity,
    'pressure': pressure,
    'wind_speed': wind,
    'description': description
}

json_data = json.dumps(weather_book)
with open ("/Users/Sando/Desktop/weatherscript/weather_book.json", "w") as f:  #you can change source for .json
    f.write(json_data)