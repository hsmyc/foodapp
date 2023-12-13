from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import food_router
app = FastAPI()
app.mount("/frontend/static",
          StaticFiles(directory="../../frontend/static"), name="frontend")
app.include_router(food_router.router)
templates = Jinja2Templates(directory="../../frontend/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/foodsearch")
def read_food_search(request: Request):
    return templates.TemplateResponse("foodsearch.html", {"request": request})

