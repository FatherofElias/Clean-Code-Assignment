# this module has a userinterface class that handles user interface
# it also includes the main function of the program

from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_detailed_weather_data(data)

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            weather_report = self.parser.parse_weather_data(data)
            return weather_report

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                print("Thank you for using the Weather Forecast Application. Goodbye!")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()