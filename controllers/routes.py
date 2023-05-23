from flask import render_template


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/pancs", methods=["GET", "POST"])
    def pancs():
        return render_template("pancs.html")
