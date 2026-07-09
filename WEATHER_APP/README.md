# Weather App

## Project Overview
This project is a simple command-line Weather Application built using Python. It fetches real-time weather information for any city using the OpenWeatherMap API. The user enters the name of a city, and the application retrieves the current weather data in JSON format from the API.

## Files

### weather.py
This is the main Python file that contains the complete program logic. It accepts the city name from the user, sends a request to the OpenWeatherMap API, retrieves the weather data, and displays the response.

## Features
- Get real-time weather information
- Search weather by city name
- Uses OpenWeatherMap API
- Displays weather data in JSON format
- Simple command-line interface

## Technologies
- Python
- Requests Library
- OpenWeatherMap API

## Workflow
- Ask the user to enter a city name
- Create the API request URL
- Send an HTTP GET request using the `requests` library
- Receive the API response
- Convert the response into JSON format
- Display the weather information

## Python Concepts Used
- Variables
- User Input (`input()`)
- API Integration
- HTTP Requests (`requests`)
- JSON Handling
- String Formatting (f-strings)

## Output
The program retrieves the current weather details of the specified city from the OpenWeatherMap API and displays the response in JSON format. The data may include temperature, humidity, weather conditions, wind speed, and other weather-related information.

## Author

**Mansi Tomar**
