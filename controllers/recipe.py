import io
import cv2
import base64
import numpy as np
from PIL import Image
from flask import session
from bson import ObjectId


class Recipe:
    def get_more_liked(db, userId):
        recipes = list(db["receita"].find().sort("likes", -1).limit(6))
        user = db["usuario"].find_one({"_id": ObjectId(userId)})
        for item in recipes:
            item["is_liked"] = str(item["_id"]) in user["likes"] if userId is not None else False
        return recipes

    def get_all(db, userId):
        recipes = list(db["receita"].find().sort("likes", -1))
        if userId is not None:
            user = db["usuario"].find_one({"_id": ObjectId(userId)})
            for item in recipes:
                item["is_favorite"] = str(item["_id"]) in user["salvos"]
                item["is_liked"] = str(item["_id"]) in user["likes"]
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
            user = db["usuario"].find_one({"_id": ObjectId(userId)})
            for item in recipes:
                item["is_favorite"] = str(item["_id"]) in user["salvos"]
                item["is_liked"] = str(item["_id"]) in user["likes"]
        return recipes

    def get_recipe(db, id, userId):
        user = db["usuario"].find_one({"_id": ObjectId(userId)})
        recipe = db["receita"].find_one({"_id": ObjectId(id)})
        recipe["is_favorite"] = str(recipe["_id"]) in user["salvos"] if userId is not None else False
        recipe["is_liked"] = str(recipe["_id"]) in user["likes"] if userId is not None else False
        recipe["author"] = str(recipe["_id"]) in user["receitas"] if userId is not None else False
        return recipe

    def add_like(db, id):
        likes = db["receita"].find_one({"_id": ObjectId(id)}).get("likes")
        db["receita"].update_one({"_id": ObjectId(id)}, {"$set": {"likes": likes + 1}})

    def remove_like(db, id):
        likes = db["receita"].find_one({"_id": ObjectId(id)}).get("likes")
        db["receita"].update_one({"_id": ObjectId(id)}, {"$set": {"likes": likes - 1}})

    def create(db, data, files):
        img_pil = Image.open(io.BytesIO(files["recipe-img"].read()))
        image = np.array(img_pil)
        img_height, img_width = image.shape[0], image.shape[1]
        img_matrix = cv2.getRotationMatrix2D((img_width / 2, img_height / 2), int(data.get("recipe-img_angle")), 1.0)
        img_rotated = cv2.warpAffine(image, img_matrix, (img_width, img_height))
        img_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
        _, img_base64 = cv2.imencode("." + img_pil.format.lower(), img_rgb)
        img_base64 = "data:image/" + img_pil.format.lower() + ";base64," + base64.b64encode(img_base64).decode("utf-8")

        recipe = db["receita"].insert_one(
            {
                "nome": data.get("recipe-name"),
                "descricao": data.get("recipe-description"),
                "likes": 0,
                "pancs": data.getlist("recipe-pancs[]"),
                "ingredientes": data.getlist("recipe-ingredients[]"),
                "preparo": data.getlist("recipe-prepare[]"),
                "imagem": img_base64,
            }
        )
        return str(recipe.inserted_id)

    def edit(db, id, data, files):
        if files["recipe-img"]:
            img_pil = Image.open(io.BytesIO(files["recipe-img"].read()))
        else:
            img_bytes = base64.b64decode(data.get("recipe-img_base64").split(",")[-1])
            img_pil = Image.open(io.BytesIO(img_bytes))

        image = np.array(img_pil)
        img_height, img_width = image.shape[0], image.shape[1]
        img_matrix = cv2.getRotationMatrix2D((img_width / 2, img_height / 2), int(data.get("recipe-img_angle")), 1.0)
        img_rotated = cv2.warpAffine(image, img_matrix, (img_width, img_height))
        img_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
        _, img_base64 = cv2.imencode("." + img_pil.format.lower(), img_rgb)
        img_base64 = "data:image/" + img_pil.format.lower() + ";base64," + base64.b64encode(img_base64).decode("utf-8")

        db["receita"].update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "nome": data.get("recipe-name"),
                    "descricao": data.get("recipe-description"),
                    "pancs": data.getlist("recipe-pancs[]"),
                    "ingredientes": data.getlist("recipe-ingredients[]"),
                    "preparo": data.getlist("recipe-prepare[]"),
                    "imagem": img_base64,
                }
            },
        )

    def delete(db, id):
        if "userId" in session:
            db["receita"].delete_one({"_id": ObjectId(id)})
