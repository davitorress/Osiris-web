import io
import cv2
import base64
import numpy as np
from PIL import Image
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
        panc = db["panc"].find_one({"_id": ObjectId(id)})
        if userId:
            favorites = db["usuario"].find_one({"_id": ObjectId(userId)}).get("favoritos")
            panc["is_favorite"] = str(panc["_id"]) in favorites
        else:
            panc["is_favorite"] = False

        return panc

    def create(db, data, files):
        img_pil = Image.open(io.BytesIO(files["panc-img"].read()))
        image = np.array(img_pil)
        img_height, img_width = image.shape[0], image.shape[1]
        img_matrix = cv2.getRotationMatrix2D((img_width / 2, img_height / 2), int(data.get("panc-img_angle")), 1.0)
        img_rotated = cv2.warpAffine(image, img_matrix, (img_width, img_height))
        img_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
        _, img_base64 = cv2.imencode("." + img_pil.format.lower(), img_rgb)
        img_base64 = "data:image/" + img_pil.format.lower() + ";base64," + base64.b64encode(img_base64).decode("utf-8")

        db["panc"].insert_one(
            {
                "nome": data.get("panc-name"),
                "descricao": data.get("panc-description"),
                "beneficios": data.get("panc-benefits"),
                "cultivo": data.getlist("panc-farm[]"),
                "imagem": img_base64,
            }
        )

    def edit(db, id, data, files):
        if files["panc-img"]:
            img_pil = Image.open(io.BytesIO(files["panc-img"].read()))
        else:
            img_bytes = base64.b64decode(data.get("panc-img_base64").split(",")[-1])
            img_pil = Image.open(io.BytesIO(img_bytes))

        image = np.array(img_pil)
        img_height, img_width = image.shape[0], image.shape[1]
        img_matrix = cv2.getRotationMatrix2D((img_width / 2, img_height / 2), int(data.get("panc-img_angle")), 1.0)
        img_rotated = cv2.warpAffine(image, img_matrix, (img_width, img_height))
        img_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
        _, img_base64 = cv2.imencode("." + img_pil.format.lower(), img_rgb)
        img_base64 = "data:image/" + img_pil.format.lower() + ";base64," + base64.b64encode(img_base64).decode("utf-8")

        db["panc"].update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "nome": data.get("panc-name"),
                    "descricao": data.get("panc-description"),
                    "beneficios": data.get("panc-benefits"),
                    "cultivo": data.getlist("panc-farm[]"),
                    "imagem": img_base64,
                }
            },
        )

    def delete(db, id):
        db["panc"].delete_one({"_id": ObjectId(id)})
