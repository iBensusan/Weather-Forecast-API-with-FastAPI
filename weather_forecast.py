from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Sample weather conditions for simulation
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]

# Function to generate random weather data for 3 days
def generate_weather_forecast():
    forecast = []
    for day in range(1, 4):
        forecast.append({
            "day": f"Day {day}",
            "temperature_c": randint(-10, 35),  # Random temperature between -10 and 35°C
            "condition": choice(weather_conditions)  # Randomly choose a weather condition
        })
    return forecast

# Endpoint to get the 3-day weather forecast for a city
@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    """
    Get a 3-day weather forecast for a specific city.
    """
    forecast_data = generate_weather_forecast()
    return {"city": city_name, "forecasts": forecast_data}

# Endpoint to get the weather forecast for a specific day in the 3-day period
@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    """
    Get the forecast for a specific day in the 3-day range.
    """
    if day < 1 or day > 3:
        return {"error": "Invalid day. Please enter a day between 1 and 3."}
    
    forecast_data = generate_weather_forecast()
    specific_day_forecast = forecast_data[day - 1]
    return {"city": city_name, "forecast": specific_day_forecast}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("weather_api:app", host="127.0.0.1", port=8000, reload=True)
