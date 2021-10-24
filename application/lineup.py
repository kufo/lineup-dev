from datetime import datetime
import random
import string

from flask import Blueprint
from flask import render_template, redirect, url_for

from .models import Customer, db
from .forms import LineupForm

lineup_bp = Blueprint(
    "lineup_bp", __name__, template_folder = "templates", static_folder = "static"
)

@lineup_bp.route("/lineup", methods = ["GET", "POST"])
def lineup():

    form = LineupForm()
    if form.validate_on_submit():
        existing_customer = Customer.query.filter_by(email=form.email.data).all()
        check_status = True

        if len(existing_customer) > 0:
            for waiting_customer in existing_customer:
                if waiting_customer.status == 0:
                    # flash("You are already in the line.")
                    check_status = False
                    break

        if check_status:
            letters = string.ascii_lowercase
            skey = ''.join(random.choice(letters) for i in range(6))
            new_customer = Customer(
                s_time = datetime.now(),
                email = form.email.data, 
                phone = form.phone.data, 
                status = 0,
                skey = skey)

            db.session.add(new_customer)
            db.session.commit()

        return redirect(url_for("lineup_bp.lineup"))

    customers = Customer.query.filter_by(status=0).order_by(Customer.id).all()
    waitnum = len(customers)
    nextnum = (customers[0].id if waitnum != 0 else 0)

    return render_template("lineup.jinja2", 
                            title = "DEMO", 
                            form = form, 
                            next_num = nextnum, 
                            waitnum = waitnum)