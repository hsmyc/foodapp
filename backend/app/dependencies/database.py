from pymongo import MongoClient
from bson.objectid import ObjectId

dbclient = MongoClient("mongodb://localhost:27017/")
db = dbclient["FoodApp"]
collectionhalal = db["halalfood"]
collectionvegan = db["veganfood"]
