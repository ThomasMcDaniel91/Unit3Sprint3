from flask import Blueprint

#creating an instance of the Blueprint object named home_routes
home_routes = Blueprint("home_routes", __name__)

#decorating the home_routes object with new routes 
@home_routes.route("/")
def index():
    return "Hello from the other side!"

@home_routes.route("/about")
def about():
    return "This is some about me stuff that's still TODO"