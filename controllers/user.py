from bson import ObjectId
import bcrypt


class User:
    def login(db, email, password):
        user = db["usuario"].find_one({"email": email})
        if user:
            hashed_password = user.get("senha").decode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
                return user["_id"]
        return False

    def register(db, name, email, password):
        collection = db["usuario"]
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        userId = collection.insert_one(
            {
                "nome": name,
                "email": email,
                "senha": hashed_password,
                "favoritos": [],
                "salvos": [],
                "receitas": [],
                "imagem": "",
            }
        )
        return userId.inserted_id

    def set_panc_favorite(db, id, pancId, fav):
        if eval(fav):
            favorited = db["usuario"].find_one({"_id": ObjectId(id), "favoritos": pancId})
            if not favorited:
                db["usuario"].update_one({"_id": ObjectId(id)}, {"$push": {"favoritos": pancId}})
        else:
            db["usuario"].update_one({"_id": ObjectId(id)}, {"$pull": {"favoritos": pancId}})
