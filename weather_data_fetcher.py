#This class is responsible for fetching weather data.


class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "new york": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York", "air_quality": "Good", "wind_direction": "NW"},
            "london": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London", "air_quality": "Moderate", "wind_direction": "SW"},
            "tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo", "air_quality": "Unhealthy", "wind_direction": "E"}
        }
        return weather_data.get(city.lower(), {})