from flask import request, jsonify
from models.connection import connect
from bson import ObjectId


class Panc:
    def get_highlight(db):
        collection = db["panc"]
        pancs = collection.find().limit(6)
        return pancs

    def get_all(db):
        collection = db["panc"]
        pancs = collection.find()
        return pancs

    def get_search(db, search):
        collection = db["panc"]
        pancs = collection.find({"nome": {"$regex": search, "$options": "i"}})
        return pancs
