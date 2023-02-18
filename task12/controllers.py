from flask import render_template, request, redirect, url_for, flash

from app import app
from models import Book, Genre, Comment
from forms import Review
from datetime import datetime

@app.route("/")
def render():
    book = Book.query.all()
    genre = Genre.query.all()
    return render_template('index.html', Books = book, Genres = genre)

@app.route("/book/<int:id>", methods = ['GET', 'POST'])
def book_render(id):
    book = Book.query.filter_by(id=id).first()
    book2 = Book.query.all()
    genre = Genre.query.all()
    commentmain = Comment.query.all()
    form = Review()
    if request.method == 'POST':
        form = Review(request.form)
        print(request.form)
        if form.validate_on_submit():
            comment3 = Comment(
                username = form.name.data,
                email = form.email.data, 
                comments = form.comments.data, 
                date = datetime.today()
            )
            comment3.book_id = id
            comment3.save()
            flash('Form uğurla göndərildi!') 
        return redirect(url_for('render'))
    
    return render_template('book.html', book=book, Books2 = book2, Genres = genre, form = form, commentmain = commentmain)

@app.route("/genre/book/<int:id>",  methods = ['GET', 'POST'])
def book_render_2(id):
    book = Book.query.filter_by(id=id).first()
    book2 = Book.query.all()
    genre = Genre.query.all()
    commentmain = Comment.query.all()
    form = Review()
    print(form)
    if request.method == 'POST':
        form = Review(request.form)
        if form.validate_on_submit():
            comment3 = Comment(
                username = form.name.data,
                email = form.email.data, 
                comments = form.comments.data, 
                date = datetime.today()
            )
            comment3.book_id = id
            comment3.save()
            flash('Form uğurla göndərildi!') 
        return redirect(url_for('render'))
    return render_template('book.html', book=book, Books2 = book2, Genres = genre, form = form, commentmain = commentmain)

@app.route("/genre/<string:genre>")
def genre_render(genre):
    book2 = Genre.query.filter_by(genre = genre).first().book
    genre = Genre.query.all()
    return render_template('product.html', Books2 = book2, Genres2 = genre)


