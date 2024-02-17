from flask import Blueprint
from ..models import Plant

plant_api = Blueprint('plant_api', __name__)

@plant_api.route('/')
def plant_status():
    plants = Plant.query.all()
    all_plants = [ (plant.id, plant.name, plant.type) for plant in plants ]
    return all_plants