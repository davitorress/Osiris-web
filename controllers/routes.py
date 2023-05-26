from flask import render_template, redirect, url_for, request
from controllers.panc import Panc
from controllers.recipe import Recipe


def init_app(app, con):
    @app.route("/")
    def index():
        pancs = Panc.get_highlight(con)
        recipes = Recipe.get_more_liked(con)
        return render_template("index.html", pancs=pancs, recipes=recipes)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        return redirect(url_for("/"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        return render_template("register.html")

    @app.route("/pancs", methods=["GET", "POST"])
    def pancs():
        pancs = Panc.get_all(con)
        if request.method == "POST":
            search = Panc.get_search(con, request.form.get("search-panc"))
            return render_template("pancs.html", pancs=pancs, search=search)
        return render_template("pancs.html", pancs=pancs)

    @app.route("/pancs/")
    @app.route("/pancs/<string:id>")
    def panc(id=None):
        if id is None or len(id) == 0:
            return redirect(url_for("pancs"))
        # if request.args.get("fav"):
        # futuramente vai definir o valor de fav
        return render_template("panc.html")

    @app.route("/receitas", methods=["GET", "POST"])
    def receitas():
        return render_template("receitas.html")

    @app.route("/receitas/")
    @app.route("/receitas/<string:id>")
    def receita(id=None):
        if id is None or len(id) == 0:
            return redirect(url_for("receitas"))
        return render_template("receita.html")

    @app.route("/receitas/criar", methods=["GET", "POST"])
    def receita_criar():
        return render_template("criar-receita.html")

    @app.route("/perfil")
    def perfil():
        return render_template("perfil.html")

    @app.route("/perfil/editar", methods=["GET", "POST"])
    def perfil_editar():
        return render_template("editar-perfil.html")
