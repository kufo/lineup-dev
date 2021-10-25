from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint("main_bp", __name__, 
                    template_folder="templates", 
                    static_folder="static")

@main_bp.route("/")
def hello():
    return render_template("index.jinja2", title="DEMO")


@main_bp.route("/hello")
@login_required
def hi():
    return "Hi"
