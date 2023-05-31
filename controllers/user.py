from flask import session
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

    def set_recipe_favorite(db, id, recipeId, fav):
        if eval(fav):
            favorited = db["usuario"].find_one({"_id": ObjectId(id), "salvos": recipeId})
            if not favorited:
                db["usuario"].update_one({"_id": ObjectId(id)}, {"$push": {"salvos": recipeId}})
        else:
            db["usuario"].update_one({"_id": ObjectId(id)}, {"$pull": {"salvos": recipeId}})

    def new_recipe(db, id, recipeId):
        db["usuario"].update_one({"_id": ObjectId(id)}, {"$push": {"receitas": recipeId}})

    def remove_recipe(db, recipeId):
        if "userId" in session:
            db["usuario"].update_one({"_id": ObjectId(session["userId"])}, {"$pull": {"receitas": recipeId}})

    def get_info(db):
        user = dict(db["usuario"].find_one({"_id": ObjectId(session["userId"])}))

        for index, p in enumerate(user["favoritos"]):
            panc = db["panc"].find_one({"_id": ObjectId(p)})
            user["favoritos"][index] = panc
        for index, s in enumerate(user["salvos"]):
            recipe = db["receita"].find_one({"_id": ObjectId(s)})
            user["salvos"][index] = recipe
        for index, r in enumerate(user["receitas"]):
            recipe = db["receita"].find_one({"_id": ObjectId(r)})
            user["receitas"][index] = recipe

        return user

    def edit(db, data, files):
        if data.get("new-pass"):
            db["usuario"].update_one(
                {"_id": ObjectId(session["userId"])},
                {
                    "$set": {
                        "nome": data.get("name"),
                        "email": data.get("email"),
                        "senha": bcrypt.hashpw(data.get("new-pass").encode("utf-8"), bcrypt.gensalt()),
                        "imagem": data.get("img_base64"),
                    }
                },
            )
        else:
            db["usuario"].update_one(
                {"_id": ObjectId(session["userId"])},
                {
                    "$set": {
                        "nome": data.get("name"),
                        "email": data.get("email"),
                        "imagem": data.get("img_base64"),
                    }
                },
            )
