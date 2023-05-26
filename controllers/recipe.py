from flask import request, jsonify
from models.connection import connect
from bson import ObjectId


class Recipe:
    def get_more_liked(db):
        collection = db["receita"]
        recipes = collection.find().sort("likes", -1).limit(6)
        return recipes
