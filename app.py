from flask import Flask
from models import connection
from controllers import routes

app = Flask(__name__, template_folder="views", static_folder="views/assets")
app.secret_key = "123456"

db = connection.connect(app)
routes.init_app(app, db)

if __name__ == "__main__":
    app.run(debug=True)
