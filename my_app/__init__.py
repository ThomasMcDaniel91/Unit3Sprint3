from flask import Flask

from my_app.models import db, migrate
from my_app.routes.home_routes import home_routes
from my_app.routes.tweet_routes import tweet_routes
from my_app.routes.twitter_routes import twitter_routes

DATABASE_URI = "sqlite:///C:\\Users\Thomas\\LambdaSchool\\Unit3Sprint3\\Unit3Sprint3\\web_app_99.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(twitter_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)