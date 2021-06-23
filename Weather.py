import requests
import os
from datetime import datetime


user_api = "644408c7bd238782dd8d49a00f797d54"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#to save as a text file
with open('weather.txt','w') as f:
    f.write("-------------------------------------------------------------\n")
    f.write ("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
    f.write ("-------------------------------------------------------------\n")
    f.write ("Current temperature is: {:.2f} deg C\n".format(temp_city))
    f.write ("Current weather desc  : {}\n".format(weather_desc))
    f.write ("Current Humidity      : {} %\n".format(hmdt))
    f.write ("Current wind speed    : {} kmph\n".format(wind_spd))