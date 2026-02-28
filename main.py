from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# -------------------------
# 1️⃣ AI Assistant
# -------------------------
@app.get("/ask/{question}")
def ask_question(question: str):
    question = question.lower()

    if "rice" in question:
        return {"answer": "Rice grows well in warm and wet climate."}
    elif "wheat" in question:
        return {"answer": "Wheat grows well in cool climate."}
    elif "fertilizer" in question:
        return {"answer": "Use nitrogen-based fertilizers for better growth."}
    else:
        return {"answer": "Please ask farming related questions."}


# -------------------------
# 2️⃣ Weather (No API)
# -------------------------
@app.get("/weather/{city}")
def get_weather(city: str):
    city = city.capitalize()

    return {
        "city": city,
        "temperature": random.randint(25, 40),
        "humidity": random.randint(50, 80),
        "description": random.choice(
            ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Humid"]
        )
    }


# -------------------------
# 3️⃣ Pesticide Suggestion
# -------------------------
@app.get("/pesticide/{crop}")
def pesticide(crop: str):
    crop = crop.lower()

    if crop in ["rice", "paddy"]:
        return {"solution": "Use Carbofuran for rice stem borer."}
    elif crop == "cotton":
        return {"solution": "Use Neem oil spray for cotton pests."}
    elif crop == "tomato":
        return {"solution": "Use Imidacloprid for whiteflies."}
    else:
        return {"solution": "No pesticide data available."}


# -------------------------
# 4️⃣ Crop Recommendation
# -------------------------
@app.get("/crop/{soil}")
def crop_recommendation(soil: str):
    soil = soil.lower()

    if soil in ["black", "black soil"]:
        return {"crop": "Cotton, Soybean"}
    elif soil in ["red", "red soil"]:
        return {"crop": "Groundnut, Millets"}
    elif soil in ["alluvial", "alluvial soil"]:
        return {"crop": "Rice, Wheat"}
    else:
        return {"crop": "No data available"}
