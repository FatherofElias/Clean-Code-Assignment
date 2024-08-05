# This modular class is responsible for parsing the weather data


class DataParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def parse_detailed_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        air_quality = data["air_quality"]
        wind_direction = data["wind_direction"]
        return (f"Detailed Weather in {city}:\n"
                f"Temperature: {temperature} degrees\n"
                f"Condition: {condition}\n"
                f"Humidity: {humidity}%\n"
                f"Air Quality: {air_quality}\n"
                f"Wind Direction: {wind_direction}\n")