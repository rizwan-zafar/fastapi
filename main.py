# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/countries")
def get_countries():
    countries = [
        "United States", "Canada", "Australia", "United Kingdom", "India",
        "Germany", "France", "Japan", "China", "Brazil", "Pakistan", "Bangladesh",
        "Saudi Arabia", "UAE", "Russia", "South Africa", "Mexico", "Italy",
        "Spain", "Turkey", "Indonesia", "Argentina"
    ]
     # Convert to list of objects
    country_list = [{"name": country} for country in countries]
    return {"countries": country_list}
