from pydantic import BaseModel


class Food(BaseModel):
    name: str
    price: float
    isVegan: bool
    isHalal: bool
    isVegetarian: bool
    isGlutenFree: bool
    isPescatarian: bool
