from flask import Blueprint
from flask import request


solar_system_bp = Blueprint("solar_system", __name__)
planets_bp = Blueprint("", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def planet():
    request_body = request.get_json()

@solar_system_bp.route("/solar-system", methods=["GET"])
def endpoint_name():
    ss_response_body = "Welcome to the Solar System!"
    return ss_response_body