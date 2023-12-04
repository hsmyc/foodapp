from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from getName import getName
app = FastAPI()


app.mount("/frontend/static",
          StaticFiles(directory="../../frontend/static"), name="frontend")

templates = Jinja2Templates(directory="../../frontend/templates")

name = getName('mualla')
print(name)


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/osman')
def read_root(request: Request):
    return {'message': name['message']}


@app.get('/food')
def read_root(request: Request):
    return templates.TemplateResponse("food.html", {"request": request})
