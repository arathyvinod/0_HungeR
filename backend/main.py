from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key

@app.get("/planting-tips")
def get_planting_tips(crop: str = "general"):
    tips = {
        "rice": "Ensure proper puddling of soil and maintain 5cm water level.",
        "wheat": "Sow seeds at a depth of 5 cm and apply basal fertilizer.",
        "tomato": "Use raised beds and provide staking for plants.",
        "general": "Prepare soil well and ensure timely watering."
    }
    return {"tip": tips.get(crop.lower(), tips["general"])}

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url).json()
    if response.get("main"):
        temp_c = response["main"]["temp"] - 273.15
        weather_desc = response["weather"][0]["description"]
        return {"temperature": f"{temp_c:.2f}°C", "description": weather_desc}
    return {"error": "City not found"}

@app.get("/crop-suggestion")
def crop_suggestion(season: str = "kharif"):
    crops = {
        "kharif": "Rice, Maize, Cotton",
        "rabi": "Wheat, Barley, Mustard",
        "zaid": "Watermelon, Muskmelon"
    }
    return {"suggested_crops": crops.get(season.lower(), "Rice, Wheat")}
