from flask import request, jsonify
from models.connection import connect
from bson import ObjectId


class Recipe:
    def get_more_liked(db):
        recipes = db["receita"].find().sort("likes", -1).limit(6)
        return recipes

    def get_all(db, userId):
        recipes = list(db["receita"].find().sort("likes", -1))
        if userId is not None:
            favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("salvos")
            for item in recipes:
                item["is_favorite"] = str(item["_id"]) in favorites
        return recipes

    def get_search(db, userId, search):
        recipes = list(
            db["receita"]
            .find(
                {
                    "$or": [
                        {"nome": {"$regex": search, "$options": "i"}},
                        {"pancs": {"$elemMatch": {"$regex": search, "$options": "i"}}},
                    ]
                }
            )
            .sort("likes", -1)
        )
        if userId is not None:
            favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("salvos")
            for item in recipes:
                item["is_favorite"] = str(item["_id"]) in favorites
        return recipes

    def get_recipe(db, id, userId):
        favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("salvos")
        recipe = db["receita"].find_one({"_id": ObjectId(id)})
        recipe["is_favorite"] = str(recipe["_id"]) in favorites
        return recipe

    def add_like(db, id):
        likes = db["receita"].find_one({"_id": ObjectId(id)}).get("likes")
        db["receita"].update_one({"_id": ObjectId(id)}, {"$set": {"likes": likes + 1}})
