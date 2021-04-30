from app import db 
from flask import Blueprint
from flask import request


solar_system_bp = Blueprint("solar_system", __name__)
planets_bp = Blueprint("", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def planet():
    request_body = request.get_json()

    new_planet = Planet(name = request_body["name"], 
    description = request_body["description"], 
    size = request_body["size"])

    db.session.add(new_planet)
    db.commit()

    return (f"planet #{new_planet.name} has been created.", 201)


@solar_system_bp.route("/solar-system", methods=["GET"])
def endpoint_name():
    ss_response_body = "Welcome to the Solar System!"
    return ss_response_body