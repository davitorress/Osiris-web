from flask import render_template, redirect, url_for, request, session

from models import schemas
from controllers.user import User
from controllers.panc import Panc
from controllers.recipe import Recipe


def init_app(app, con):
    @app.route("/")
    def index():
        userId = None
        if "userId" in session:
            userId = session["userId"]
        pancs = Panc.get_highlight(con)
        recipes = Recipe.get_more_liked(con)
        return render_template("index.html", userId=userId, pancs=pancs, recipes=recipes)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if "userId" in session:
            return redirect("/")
        if request.method == "POST":
            userId = User.login(con, request.form.get("email"), request.form.get("pass"))
            if userId:
                session["userId"] = userId
                return redirect("/")
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.pop("userId", None)
        return redirect("/")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if "userId" in session:
            return redirect("/")
        if request.method == "POST":
            userId = User.register(con, request.form.get("name"), request.form.get("email"), request.form.get("pass"))
            if userId:
                session["userId"] = userId
                return redirect("/")
        return render_template("register.html")

    @app.route("/pancs", methods=["GET", "POST"])
    def pancs():
        userId = None
        if "userId" in session:
            userId = session["userId"]
        pancs = Panc.get_all(con)
        if request.method == "POST":
            search = Panc.get_search(con, request.form.get("search-panc"))
            return render_template("pancs.html", userId=userId, pancs=pancs, search=search)
        return render_template("pancs.html", userId=userId, pancs=pancs)

    @app.route("/pancs/")
    @app.route("/pancs/<string:id>")
    def panc(id=None):
        if id is None or len(id) == 0:
            return redirect(url_for("pancs"))
        userId = None
        if "userId" in session:
            userId = session["userId"]
        if request.args.get("fav") is not None and userId is not None:
            User.set_panc_favorite(con, userId, id, request.args.get("fav"))
        panc = Panc.get_panc(con, id, userId)
        return render_template("panc.html", userId=userId, panc=panc)

    @app.route("/receitas", methods=["GET", "POST"])
    def receitas():
        userId = None
        if "userId" in session:
            userId = session["userId"]
        recipes = Recipe.get_all(con)
        if request.method == "POST":
            search = Recipe.get_search(con, request.form.get("search-recipe"))
            return render_template("receitas.html", userId=userId, recipes=recipes, search=search)
        return render_template("receitas.html", userId=userId, recipes=recipes)

    @app.route("/receitas/")
    @app.route("/receitas/<string:id>")
    def receita(id=None):
        if id is None or len(id) == 0:
            return redirect(url_for("receitas"))
        userId = None
        if "userId" in session:
            userId = session["userId"]
        recipe = Recipe.get_recipe(con, id, userId)
        return render_template("receita.html", userId=userId, recipe=recipe)

    @app.route("/receitas/criar", methods=["GET", "POST"])
    def receita_criar():
        return render_template("criar-receita.html")

    @app.route("/perfil")
    def perfil():
        if "userId" in session:
            return render_template("perfil.html")
        return redirect(url_for("login"))

    @app.route("/perfil/editar", methods=["GET", "POST"])
    def perfil_editar():
        if "userId" in session:
            return render_template("editar-perfil.html")
        return redirect(url_for("login"))
