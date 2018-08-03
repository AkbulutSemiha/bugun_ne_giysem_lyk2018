import logging
from classes.coordinates import Coordinates
from classes.weather import Weather
from classes.suggestions import Suggestions


class NeGiysem():
    weather_api_key="92bb6add0822613f2ca9dd20116528a8"
    coordinates_api_key="a5966744b2c34ab0d19f2cf74c440dd6"
    city=""
    coordinates=""
    
    def __init__(self):
        self.menu()

    def menu(self):
        print("""
        1- With Instant Location
        2- With City Name
        """)

        option = input("Choose one of them : ")

        if option.isnumeric():
            option = int(option)

            if option == 1:
                coord = self.get_coordinates(self.coordinates_api_key)
                self.get_weather_forecast(coord)

            else:
                name = self.get_city_name()
                self.get_weather_forecast(name)

        else:
            print("Wrong Entry")
            self.menu()
       
    #get coordinates
    def get_coordinates(self,coordinates_api_key):
        coordinates =Coordinates(coordinates_api_key)
        coordinates = coordinates.give_my_coordinates()
        if coordinates:
           return coordinates
        else:
           self.get_city_name()
    
    
    #ask city name
    def get_city_name(self):
        city=input("Please enter the city name for weather forecast")
        self.city=city
      
    
    #get weather forecast
    def get_weather_forecast(self,coordinates=None):
        weather = Weather(self.weather_api_key)
        self.coordinates=coordinates
        if self.coordinates:
            return weather.get_forecast_by_coordinates(self.coordinates)
        else:
            return weather.get_forecast_by_name(self.city)
           
        

    def get_suggestions(self,degrees,precipitation):
        suggestions = Suggestions(degrees,precipitation)
        return suggestions

    
app = NeGiysem()
#get coordinates
coordinates = app.get_coordinates(app.coordinates_api_key)

#get weather forecast
data=app.get_weather_forecast(coordinates)
print(data)
suggestion = Suggestions("Cloudy","-5")
#get weather main
suggestion.create()

#get temp
#minus 273.15
#get suggestions

