from flask import Blueprint

solar_system_bp = Blueprint("solar_system", __name__)

@solar_system_bp.route("/solar-system", methods=["GET"])
def endpoint_name():
    ss_response_body = "Welcome to the Solar System!"
    return ss_response_body