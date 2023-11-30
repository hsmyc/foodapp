from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

client = MongoClient("mongodb://localhost:27017/")
db = client["FoodApp"]
collection = db["Cities"]
city = collection.find_one({"NY": "New York"})

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")


@app.get("/backend")
def read_backend():
    return FileResponse("frontend/backend.html")
