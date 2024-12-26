# Importing the requests library to handle HTTP requests
import requests


# Main function to get weather information
def get_weather(city_name, api_key):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Args:
        city_name (str): Name of the city to get weather information for.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        None
    """
    # Base URL of the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Defining parameters to send to the API
    params = {
        "q": city_name,  # Name of the city
        "appid": api_key,  # API key for authentication
        "units": "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit
    }

    try:
        # Sending a GET request to the API
        response = requests.get(base_url, params=params)

        # If the response status code is 200, the request was successful
        if response.status_code == 200:
            # Convert the response to JSON format (a dictionary)
            data = response.json()

            # Extracting useful information from the JSON data
            city = data.get("name")
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            # Printing the weather details
            print(f"\nWeather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Humidity: {humidity}%")
        else:
            # If the city is not found or there's another issue, show an error message
            print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
    except Exception as e:
        # Handling exceptions such as network errors
        print(f"An error occurred: {e}")


# Main part of the program
if __name__ == "__main__":
    # Asking the user for the city name
    city = input("Enter the city name: ")

    # Replace 'your_api_key' with your actual API key
    api_key = "your_api_key_here"

    # Calling the function to fetch weather data
    get_weather(city, api_key)
