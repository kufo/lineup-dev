from flask import Blueprint, render_template

main_bp = Blueprint("main_bp", __name__, 
                    template_folder="templates", 
                    static_folder="static")

@main_bp.route("/")
def hello():
    return render_template("index.jinja2", title="DEMO")
