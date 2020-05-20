from flask import Blueprint, jsonify, request, render_template, flash, redirect
from my_app.models import Tweet, db
tweet_routes = Blueprint("tweet_routes", __name__)

#@tweet_routes.route("/tweets.json")
# def list_tweets():
#     tweets = [
#         {"id": 1, "twitter_handle": "tweet 1"},
#         {"id": 2, "twitter_handle": "tweet 2"},
#         {"id": 3, "twitter_handle": "tweet 3"},
#     ]
#    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    # tweets = [
    #     {"id": 1, "title": "tweet 1"},
    #     {"id": 2, "title": "tweet 2"},
    #     {"id": 3, "title": "tweet 3"},
    # ]
    tweet_records = Tweet.query.all()
    print(tweet_records)
    
    
    return render_template("tweets.html", message="Here's some tweets", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    new_tweet = Tweet(tweet=request.form["Tweet.tweet"], twitter_handle=request.form["twitter_handle"])
    db.session.add(new_tweet)
    db.session.commit()
    #return jsonify({
        # "message": "tweet CREATED OK (TODO)",
        # "tweet": dict(request.form)
    #})
    #flash(f"tweet '{new_tweet.title}' created successfully!", "success")
    return redirect("/tweets")