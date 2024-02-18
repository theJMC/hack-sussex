from flask import Blueprint, render_template, request, abort
from sqlalchemy.sql.functions import user

from .auth import page_auth
from .models import User, Plant

main = Blueprint('main', __name__)

context = {}


def is_logged_in():
    user = User.query.filter_by(id=request.cookies.get("userID")).first()
    if user is None:
        return False
    else:
        return True


@main.route('/')
def index():
    context["loggedIn"] = is_logged_in()
    context["currentPage"] = "home"
    return render_template("index.html", **context)


@main.route('/profile')
@page_auth
def profile_page(user):
    context["loggedIn"] = is_logged_in()
    context["currentPage"] = "profile"
    context["user"] = {"name": user.name, "email": user.email}
    return render_template("profile.html", **context)

@main.route("/myplants")
@page_auth
def myplants_page(user):
    context["loggedIn"] = is_logged_in()
    context["currentPage"] = "myplants"
    context["user"] = {"name": user.name, "overall_status": user.overall_status}
    context["plants"] = Plant.query.filter_by(owner=user.id).all()
    return render_template("myplants.html", **context)

@main.route('/plant/')
@page_auth
def plants_page(user):
    context["loggedIn"] = is_logged_in()
    context["currentPage"] = "plants"
    context["user"] = {"name": user.name}
    plant_id = request.args.get("plant_id")
    plant = Plant.query.filter_by(id=plant_id).first()
    if plant is None:
        return abort(404)
    if plant.owner != user.id:
        return abort(401)
    context["plant"] = plant
    return render_template("plant.html", **context)

@main.route('/new_plant')
@page_auth
def new_plant_page(user):
    context["loggedIn"] = is_logged_in()
    context["currentPage"] = ""
    context["user"] = {"name": user.name}
    return render_template("new_plant.html", **context)