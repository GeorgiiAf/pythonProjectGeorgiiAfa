import requests

API_KEY = "ea160710d29362e47dabb6650ab0a046"

# Function to get weather data by coordinates
def get_weather(lat, lon):
    # Construct the weather URL with coordinates and API key
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    # Send a GET request to the API
    response = requests.get(weather_url)
    # Parse the JSON response
    weather_data = response.json()
    return weather_data

# Function to get coordinates by city name
def get_coordinates(city_name):
    # Construct the geolocation URL with the city name and API key
    geolocation_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    # Send a GET request to the API
    response = requests.get(geolocation_url)
    # Parse the JSON response
    location_data = response.json()
    return location_data


city_name = input('Enter the city name: ')
# Get the coordinates by city name
location_data = get_coordinates(city_name)

try:
    # Check if location data is available
    if location_data:
        # Extract latitude and longitude from location data
        lat = location_data[0]['lat']
        lon = location_data[0]['lon']
        # Get weather data by coordinates
        weather_data = get_weather(lat, lon)

        # Check if weather data is available
        if 'weather' in weather_data and 'main' in weather_data:
            # Extract weather description and temperature
            weather_description = weather_data['weather'][0]['description']
            temperature_celsius = weather_data['main']['temp']

            # Display weather information
            print(f"\nWeather in {city_name}:")
            print("----------------------------")
            print("Weather description:", weather_description)
            print("Temperature:", round(temperature_celsius, 2), "°C")
        else:
            print("Weather data not found.")
    else:
        print("City not found. Please check the spelling and try again.")
except KeyError:
    print("Error: Location information not found.")
