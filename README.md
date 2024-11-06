# Weather Forecast API with FastAPI

A real-world level project designed to build a RESTful API using FastAPI. This API simulates a simple weather forecast service, allowing users to request a weather forecast for a specified city over a 3-day period and retrieve specific day forecasts within this period.

## Features

- **3-Day Forecast Retrieval**: Users can get the weather forecast for a city over a 3-day period.
- **Daily Forecast Query**: Allows users to query the forecast for a specific day within the 3-day range.
- **High-Performance Framework**: Built with FastAPI for fast and reliable API performance.
- **Simulated Data**: Generates random weather conditions for demonstration purposes.

## Requirements

- Python 3.6 or above
- `fastapi`
- `uvicorn`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/username/weather-forecast-api-fastapi.git
    cd weather-forecast-api-fastapi
    ```

2. Install the required libraries:
    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1. Run the API using `uvicorn`:
    ```bash
    uvicorn weather_api:app --reload
    ```

2. Access the API endpoints:
    - Get a 3-day weather forecast for a city:
      ```
      http://127.0.0.1:8000/forecast/{city_name}
      ```
    - Get the weather forecast for a specific day within the 3-day period:
      ```
      http://127.0.0.1:8000/forecast/{city_name}/{day}
      ```

## Example Workflow

1. Query the 3-day forecast for a city:
    ```
    http://127.0.0.1:8000/forecast/London
    ```

    Response:
    ```json
    {
      "city": "London",
      "forecasts": [
        {"day": "Day 1", "temperature_c": 8, "condition": "Rainy"},
        {"day": "Day 2", "temperature_c": 34, "condition": "Cloudy"},
        {"day": "Day 3", "temperature_c": 25, "condition": "Sunny"}
      ]
    }
    ```

2. Query the forecast for a specific day:
    ```
    http://127.0.0.1:8000/forecast/London/2
    ```

    Response:
    ```json
    {
      "city": "London",
      "forecast": {"day": "Day 2", "temperature_c": 34, "condition": "Cloudy"}
    }
    ```

## Files

- `weather_api.py`: The main FastAPI script that runs the API and simulates the weather forecast service.
- `README.md`: Project description and usage guide.

## License

This project is licensed under the MIT License.
