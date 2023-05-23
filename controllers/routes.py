from flask import render_template, redirect, url_for, request


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/pancs", methods=["GET", "POST"])
    def pancs():
        return render_template("pancs.html")

    @app.route("/pancs/")
    @app.route("/pancs/<string:id>")
    def panc(id=None):
        if id is None or len(id) == 0:
            return redirect(url_for("pancs"))
        # if request.args.get("fav"):
        # futuramente vai definir o valor de fav
        return render_template("panc.html")
