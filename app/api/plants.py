from flask import Blueprint, request, Response
from ..models import Plant, User
from ..auth import api_auth
from app import db
from uuid import uuid4
import json

plant_api = Blueprint('plant_api', __name__)


@plant_api.route('/')
@api_auth
def plant_status(user):
    user = User.query.filter_by(id=user.id).first()
    if user is None:
        return Response("User not found", status=404)

    all_plants = [(plant.id, plant.name, plant.type) for plant in Plant.query.filter_by(owner=user.id).all()]
    return all_plants


@plant_api.route("/new")
@api_auth
def new_plant(user):
    plant_name = request.json["plant_name"]
    plant_type = request.json["plant_type"]
    with open("default_plants.json") as file:
        data = json.load(file)
    if plant_type not in data:
        return Response("plant_type is invalid", status=400)
    currentType = data[plant_type]
    db.session.add(Plant(id=str(uuid4()), name=plant_name, type=plant_type, sunlight=currentType["sunlight"],
                         water=currentType["water"], owner=user.id))
    db.session.commit()
    return request.json


@plant_api.route("/update", methods=["POST"])
@api_auth
def tick(user):
    updated_plant = request.json
    to_update = Plant.query.filter_by().all()
    to_update.name = updated_plant["name"]
    to_update.type = updated_plant["type"]
    to_update.sunlight = updated_plant["sunlight"]
    to_update.water = updated_plant["water"]
    to_update.notes = updated_plant["notes"]
    to_update.vibes = updated_plant["vibes"]
    to_update.species = updated_plant["species"]
    db.session.commit()
    return str(to_update.id)


