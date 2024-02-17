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

    plants = Plant.query.filter_by(owner=user.id).all()
    all_plants = [(plant.id, plant.name, plant.type) for plant in plants]
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
