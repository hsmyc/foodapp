from fastapi import FastAPI, Request
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
client = MongoClient("mongodb://localhost:27017/")
db = client["FoodApp"]
collection = db["Cities"]
city = collection.find_one({"NY": "New York"})

app = FastAPI()
app.mount("/frontend/static",
          StaticFiles(directory="../../frontend/static"), name="frontend")

templates = Jinja2Templates(directory="../../frontend/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "city": city})


@app.get('/osman')
def read_root(request: Request):
    return {'message': 'Burası Osmanin sayfası'}
