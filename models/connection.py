from flask_pymongo import PyMongo


def connect(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/Osiris"
    mongo = PyMongo(app)
    return mongo.db
