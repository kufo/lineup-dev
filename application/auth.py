from datetime import datetime

from flask import Blueprint, url_for, redirect, render_template, request
from flask_login import login_user, current_user, login_required, logout_user

from . import login_manager
from .models import User, db
from .forms import SignupForm, LoginForm


auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main_bp.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main_bp.dashboard"))

        return redirect(url_for('auth_bp.login'))

    return render_template("login.jinja2", title = "DEMO", form = form)


@auth_bp.route("/sign_up", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(email = form.email.data, created_on=datetime.now()) 
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main_bp.dashboard'))

    return render_template("signup.jinja2", title = "DEMO", form = form)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)

    return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))