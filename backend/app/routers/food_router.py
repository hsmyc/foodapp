from fastapi import APIRouter, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from models.food import Food
from dependencies.database import collectionhalal, collectionvegan, collectionvegetarian, collectionglutenfree
router = APIRouter()
templates = Jinja2Templates(directory="../../frontend/templates")


@router.get('/foodsearch')
def read_food(request: Request):
    return templates.TemplateResponse("foodsearch.html", {"request": request})


@router.get('/createfood')
def create_food(request: Request):
    return templates.TemplateResponse("createfood.html", {"request": request})


@router.post('/food')
def create_food(food: Food):
    food_data = jsonable_encoder(food)
    inserted = False
    if food_data['isHalal']:
        result = collectionhalal.insert_one(food_data)
        inserted = True
    if food_data['isVegan']:
        result = collectionvegan.insert_one(food_data)
        inserted = True
    if food_data['isVegetarian']:
        result = collectionvegetarian.insert_one(food_data)
        inserted = True
    if food_data['isGlutenFree']:
        result = collectionglutenfree.insert_one(food_data)
        inserted = True
    if not inserted:
        raise HTTPException(
            status_code=400, detail="Food must be either halal, vegan, vegetarian or gluten free")
    return {"message": "Food successfully added", "id": str(result.inserted_id)}
