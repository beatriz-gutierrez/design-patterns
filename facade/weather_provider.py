import random

class OpenWeatherMapProvider:
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/forcast?q={},{}"

    def get_forecast(self, city:str, country:str) -> str:
        # url = self.url.format(city, country) # then get temperature
        # Simulating a call to a weather service and returning temperature
        temperature = random.uniform(-10, 30)
        return f"OpenWeatherMap: {temperature: .2f}°C in {city}, {country}"
    

class AnothterWeatherProvider:

    def get_forecast(self, city:str, country:str) -> str:
        temperature = random.uniform(0, 35)
        return f"OpenWeatherMap: {temperature: .2f}°C in {city}, {country}"
    

class WeatherFacade:
    
    def get_forecast(self, city:str, country: str) -> str:
        if city in (["Stockholm", "Solna"]) and country in (["Sweden"]):
            weather_data = OpenWeatherMapProvider().get_forecast(city=city, country=country)
        else:
            weather_data = AnothterWeatherProvider().get_forecast(city=city, country=country)
        return weather_data
    

if __name__ == "__main__":

    weather_facade = WeatherFacade()

    print(weather_facade.get_forecast("Stockholm", "Sweden"))
    print(weather_facade.get_forecast("Madrid", "Spain"))

