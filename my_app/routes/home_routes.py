from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    
    return "Hello World!"

@home_routes.route("/about")
def about():
    return "About me"