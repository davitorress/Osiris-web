from flask import request, jsonify
from models.connection import connect
from bson import ObjectId


class Recipe:
    def get_more_liked(db):
        collection = db["receita"]
        recipes = collection.find().sort("likes", -1).limit(6)
        return recipes

    def get_all(db):
        collection = db["receita"]
        recipes = collection.find().sort("likes", -1)
        return recipes

    def get_search(db, search):
        collection = db["receita"]
        recipes = collection.find(
            {
                "$or": [
                    {"nome": {"$regex": search, "$options": "i"}},
                    {"pancs": {"$elemMatch": {"$regex": search, "$options": "i"}}},
                ]
            }
        ).sort("likes", -1)
        return recipes

    def get_recipe(db, id, userId):
        favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("salvos")
        recipe = db["receita"].find_one({"_id": ObjectId(id)})
        recipe["is_favorite"] = recipe["_id"] in favorites
        return recipe
