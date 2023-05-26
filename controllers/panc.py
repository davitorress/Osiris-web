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

    def get_panc(db, id, userId):
        favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("favoritos")
        panc = db["panc"].find_one({"_id": ObjectId(id)})
        panc["is_favorite"] = str(panc["_id"]) in favorites
        return panc
