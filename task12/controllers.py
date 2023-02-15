from flask import render_template

from app import app
from models import Book, Genre

@app.route("/")
def render():
    book = Book.query.all()
    genre = Genre.query.all()
    return render_template('index.html', Books = book, Genres = genre)

@app.route("/book/<int:id>")
def book_render(id):
    book = Book.query.filter_by(id=id).first()
    book2 = Book.query.all()
    genre = Genre.query.all()
    return render_template('book.html', book=book, Books2 = book2, Genres = genre)

@app.route("/genre/book/<int:id>")
def book_render_2(id):
    book = Book.query.filter_by(id=id).first()
    book2 = Book.query.all()
    genre = Genre.query.all()
    return render_template('book.html', book=book, Books2 = book2, Genres = genre)

@app.route("/genre/<string:genre>")
def genre_render(genre):
    book2 = Genre.query.filter_by(genre = genre).first().book
    genre = Genre.query.all()
    return render_template('product.html', Books2 = book2, Genres2 = genre)


