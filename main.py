from fastapi import FastAPI
from weather import get_weather
from schemes import get_scheme_info

app = FastAPI()

@app.get("/")
def home():
    return {"message": "KrishiSahay AI is running"}

@app.get("/weather/{city}")
def weather(city: str):
    return get_weather(city)

@app.get("/scheme/{scheme_name}")
def scheme(scheme_name: str):
    return get_scheme_info(scheme_name)