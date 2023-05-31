from flask import render_template, redirect, url_for, request, session

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
                session["userId"] = str(userId)
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
                session["userId"] = str(userId)
                return redirect("/")
        return render_template("register.html")

    @app.route("/pancs", methods=["GET", "POST"])
    def pancs():
        userId = None
        if "userId" in session:
            userId = session["userId"]
        pancs = Panc.get_all(con, userId)
        if request.method == "POST":
            search = Panc.get_search(con, userId, request.form.get("search-panc"))
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
        recipes = Recipe.get_all(con, userId)
        if request.method == "POST":
            search = Recipe.get_search(con, userId, request.form.get("search-recipe"))
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
        if request.args.get("save") is not None and userId is not None:
            User.set_recipe_favorite(con, userId, id, request.args.get("save"))
        if request.args.get("like") is not None and userId is not None:
            Recipe.add_like(con, id)
        recipe = Recipe.get_recipe(con, id, userId)
        return render_template("receita.html", userId=userId, recipe=recipe)

    @app.route("/receitas/criar", methods=["GET", "POST"])
    def receita_criar():
        userId = None
        if "userId" in session:
            userId = session["userId"]
        if request.method == "POST":
            recipe = Recipe.create(con, request.form, request.files)
            if userId is not None:
                User.new_recipe(con, userId, recipe)
            return redirect("/receitas/" + recipe)
        pancs = Panc.get_all_names(con)
        return render_template("criar-receita.html", userId=userId, pancs=pancs)

    @app.route("/receitas/<string:id>/editar", methods=["GET", "POST"])
    def receita_editar(id=None):
        userId = None
        if "userId" in session:
            userId = session["userId"]
        if id is None or len(id) == 0 or userId is None:
            return redirect(url_for("receitas"))
        pancs = Panc.get_all_names(con)
        recipe = Recipe.get_recipe(con, id, userId)
        if not recipe["author"]:
            return redirect(url_for("receitas"))
        if request.method == "POST":
            Recipe.edit(con, id, request.form, request.files)
            return redirect("/receitas/" + id)
        return render_template("criar-receita.html", userId=userId, pancs=pancs, recipe=recipe)

    @app.route("/perfil")
    def perfil():
        if "userId" in session:
            user = User.get_info(con)
            return render_template("perfil.html", userId=session["userId"], user=user)
        return redirect(url_for("login"))

    @app.route("/perfil/editar", methods=["GET", "POST"])
    def perfil_editar():
        if "userId" in session:
            if request.method == "POST":
                User.edit(con, request.form, request.files)
                return redirect(url_for("perfil"))
            user = User.get_info(con)
            return render_template("editar-perfil.html", user=user)
        return redirect(url_for("login"))

    @app.route("/api/panc/fav", methods=["POST"])
    def panc_fav():
        if "userId" in session:
            User.set_panc_favorite(con, session["userId"], request.get_json()["id"], str(request.get_json()["fav"]))
        return "success"

    @app.route("/api/recipe/fav", methods=["POST"])
    def recipe_fav():
        if "userId" in session:
            User.set_recipe_favorite(con, session["userId"], request.get_json()["id"], str(request.get_json()["fav"]))
        return "success"

    @app.route("/api/recipe/like", methods=["POST"])
    def recipe_like():
        if "userId" in session:
            Recipe.add_like(con, request.get_json()["id"])
        return "success"
