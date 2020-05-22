from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.twitter_routes import twitter_routes

DATABASE_URI = "sqlite:///C:\\users\\Thomas\\LambdaSchool\\Unit3Sprint3\\Unit3Sprint3\\web_app_99.db"

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

#registering the home_routes blueprint object so the app knows about it existing
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)

    return app

if __name__ == "__main__":
# initializing our app and using the run method on it
    my_app = create_app()
    my_app.run(debug=True)