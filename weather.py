import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url).json()
    
    if "main" in response:
        return {
            "temperature": response["main"]["temp"],
            "humidity": response["main"]["humidity"],
            "advice": "Irrigate crops if temperature is high."
        }
    else:
        return {"error": "City not found"}