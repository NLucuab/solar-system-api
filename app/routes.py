from app import db 
from flask import Blueprint, request, jsonify
from app.models.planet import Planet

solar_system_bp = Blueprint("solar_system", __name__)
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/<planet_id>", methods = ["GET"], strict_slashes = False)
def get_single_planet(planet_id):
    # searches for the planet with the provided id
    planet = Planet.query.get(planet_id)

    if planet:
        return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size
            }, 200 

    return {
        "message": f"Planet with id {planet_id} was not found",
        "success": False
    }, 404
    
@planets_bp.route("", methods=["POST", "GET"], strict_slashes = False)
def planet():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size
            })
        
        return jsonify(planets_response), 200

    else:    
        request_body = request.get_json()

        new_planet = Planet(name = request_body["name"], 
        description = request_body["description"], 
        size = request_body["size"])

        db.session.add(new_planet)
        db.session.commit()

        return {
            "success": True,
            "message": f"planet {new_planet.name} has been created."}, 201


# @solar_system_bp.route("/solar-system", methods=["GET"])
# def endpoint_name():
#     ss_response_body = "Welcome to the Solar System!"
#     return ss_response_body