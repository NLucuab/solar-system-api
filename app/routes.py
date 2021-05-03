from app import db 
from flask import Blueprint, request, jsonify
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"], strict_slashes=False)
def planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        size=request_body["size"])
    db.session.add(new_planet)
    db.session.commit()

    return {
        "success": True,
        "message": f"Planet {new_planet.name} successfully created"
        }, 201

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def planets_index():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_json())
    
    return jsonify(planets_response), 200

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

@planets_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def get_single_planet(planet_id):
    # searches for the planet with the provided id
    if not is_int(planet_id):
        return{
            "message": f"ID {planet_id} must be an integer",
            "success": False
        }, 400

    planet = Planet.query.get(planet_id)

    if planet:
        return planet.to_json(), 200
    
    return {
        "message": f"Planet with ID {planet_id} was not found",
        "success": False
    }, 404

@planets_bp.route("/<planet_id>", methods=["PUT"], strict_slashes=False)
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)

    form_data = request.get_json()

    planet.name = form_data["name"]
    planet.description = form_data["description"]
    planet.size = form_data["size"]

    db.session.commit()

    return {
        "success": True,
        "message": f"Planet {planet_id} successfully updated."
    }