import bcrypt


class Admin:
    def login(db, data):
        admin = db["admin"].find_one({"email": data.get("email")})
        if admin:
            hashed_password = admin.get("senha").decode("utf-8")
            if bcrypt.checkpw(data.get("password").encode("utf-8"), hashed_password.encode("utf-8")):
                return admin["_id"]
        return False

    def register(db, data):
        admin = db["admin"].find_one({"email": data.get("email")})
        if not admin:
            hashed_password = bcrypt.hashpw(data.get("password").encode("utf-8"), bcrypt.gensalt())
            admin = db["admin"].insert_one(
                {
                    "email": data.get("email"),
                    "senha": hashed_password,
                }
            )
            return admin.inserted_id
        return False
