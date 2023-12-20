from pymongo import MongoClient

dbclient = MongoClient("mongodb://localhost:27017/")
db = dbclient["FoodApp"]
collectionhalal = db["halalfood"]
collectionvegan = db["veganfood"]
collectionvegetarian = db["vegetarianfood"]
collectionglutenfree = db["glutenfreefood"]
collectionpescatarian = db["pescatarianfood"]
