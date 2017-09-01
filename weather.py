import os
import requests
import json

FILE_PATH = "/Users/Sando/Desktop/weatherscript/weather_book.json"  #you can change source for .json

re_next = True
while re_next:

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
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            weather_book = json.load(file)

    weather_book['weather_data'] = {
        'city': name,
        'country': country,
        'temperature': temperatureC,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind,
        'description': description
    }

    json_data = json.dumps(weather_book)
    with open(FILE_PATH, "w") as file:
        file.write(json_data)

    re_open = True
    while re_open:
        answer = input("\nRun again ? y / n: ")
        if (answer == "y" or answer == "Y"):
            re_open = False
        elif ( answer == "n" or answer == "N"):
            re_open = False
            re_next = False
        else:
            pass

input("")








