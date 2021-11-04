from datetime import datetime
import random
import string

from flask import Blueprint, flash
from flask import render_template, redirect, url_for, request
from flask_login import login_required

from .models import Customer, db
from .forms import LineupForm, SearchForm

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
                    flash("You are already in the line.")
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



@lineup_bp.route("/serve")
@login_required
def served():
    customers = Customer.query.\
            filter_by(status=0).\
            order_by(Customer.id.asc()).all()

    served_customer = None

    customer_id = request.args.get("customer_id")
    
    if customer_id != None:
        try:
            customer_id = int(customer_id)
        except:
            return redirect(url_for("main_bp.dashboard"))

        for customer in customers:
            if customer_id == customer.get_id():
                served_customer = customer
    else:
        if len(customers) != 0:
            served_customer = customers.pop(0)

    if served_customer != None:
        served_customer.change_status(1)
        db.session.commit()

    return redirect(url_for("main_bp.dashboard"))


@lineup_bp.route("/served")
@login_required
def history():
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.\
                filter_by(status=1).\
                order_by(Customer.c_time.desc()).paginate(page=page, per_page=3)
    

    return render_template("served.jinja2", 
                            title = "DEMO", 
                            customers=customers,
                            form=SearchForm())

@lineup_bp.route("/search", methods=["POST"])
@login_required
def search():
    page = request.args.get('page', 1, type=int)
    form = SearchForm()

    record = Customer.query.filter(
        Customer.email.ilike(f"%{form.search.data}%")).paginate(page=page, per_page=3)
    
    record = None if len(record.items) == 0 else record

    return render_template("served.jinja2", 
                        title = "DEMO",
                        customers=record,
                        form = form)