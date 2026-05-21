from langchain.tools import tool

@tool
def weather_tool(city: str) -> str:
    """
    Get weather information for a city.
    """

    fake_weather = {
        "delhi": "35°C, Sunny",
        "mumbai": "30°C, Humid",
        "london": "15°C, Cloudy"
    }

    weather = fake_weather.get(
        city.lower(),
        "Weather data unavailable"
    )

    return f"Weather in {city}: {weather}"