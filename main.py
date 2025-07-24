# main.py
from fastapi import FastAPI
import httpx
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/countries")
async def get_countries():
    url = "https://restcountries.com/v3.1/independent?status=true"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    # Extract only the "common" country names
    countries = [{"name": country["name"]["common"]} for country in data if "name" in country and "common" in country["name"]]

    return {"countries": countries}
