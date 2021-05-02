from app import db 
from flask import Blueprint, request, jsonify
from app.models.planet import Planet

solar_system_bp = Blueprint("solar_system", __name__)
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"], strict_slashes = False)
def planet():
    request_body = request.get_json()

    new_planet = Planet(name = request_body["name"], 
    description = request_body["description"], 
    size = request_body["size"])

    db.session.add(new_planet)
    db.session.commit()

    return (f"planet {new_planet.name} has been created.", 201)


# @solar_system_bp.route("/solar-system", methods=["GET"])
# def endpoint_name():
#     ss_response_body = "Welcome to the Solar System!"
#     return ss_response_body