from flask import Blueprint, render_template
from flask_login import login_required


from .models import Customer


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


@main_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    customers = Customer.query.filter_by(status=0).all()
    return render_template(
        "dashboard.jinja2", 
        title = "DEMO", 
        customers=customers, waitnum=len(customers))