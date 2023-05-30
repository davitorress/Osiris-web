from bson import ObjectId


class Panc:
    def get_highlight(db):
        pancs = db["panc"].find().limit(6)
        return pancs

    def get_all(db, userId):
        pancs = list(db["panc"].find())
        if userId is not None:
            favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("favoritos")
            for item in pancs:
                item["is_favorite"] = str(item["_id"]) in favorites
        return pancs

    def get_all_names(db):
        pancs = [doc.get("nome") for doc in db["panc"].find().sort("nome", 1)]
        return pancs

    def get_search(db, userId, search):
        pancs = list(db["panc"].find({"nome": {"$regex": search, "$options": "i"}}))
        if userId is not None:
            favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("favoritos")
            for item in pancs:
                item["is_favorite"] = str(item["_id"]) in favorites
        return pancs

    def get_panc(db, id, userId):
        favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("favoritos")
        panc = db["panc"].find_one({"_id": ObjectId(id)})
        panc["is_favorite"] = str(panc["_id"]) in favorites
        return panc
