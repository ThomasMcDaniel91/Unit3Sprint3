from flask import Blueprint, jsonify, request, render_template, Flask, redirect

from web_app.models import Book, db

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    #converts our dictionary into a json object to be read by our app
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 1, "title": "Book 1"},
    # ]
    book_records = Book.query.all()
    print(book_records)
    return render_template("books.html", message="Here's some books", books=book_records)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():

    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    return redirect("/books")
    # print("FORM DATA:", dict(request.form))
    # return jsonify({
    #     "message": "Book created OK",
    #     "book": dict(request.form)
    # })