from flask import render_template, request, redirect, url_for, flash

from app import app
from models import Book, Genre, Comment, Userman
from forms import Review, RegisterForm, LoginForm
from datetime import datetime
from werkzeug.security import  generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

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


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form1 = RegisterForm()
    form2 = LoginForm()
    if request.method == 'POST':
        form1 = RegisterForm(request.form)
        form2 = LoginForm(request.form)
        if form1.validate_on_submit():
            
            use = Userman(
                name = form1.name.data,
                username = form1.username.data,
                email = form1.email.data, 
                password = generate_password_hash(form1.password.data)
            )
            use.save() 
            return redirect (url_for('login'))
        if form2.validate_on_submit():
            logged_user = Userman.query.filter_by(username=form2.username.data).first()
            if logged_user and logged_user.check_password(form2.password.data):
                login_user(logged_user)
            return redirect (url_for('login'))
    return render_template ('login.html' , form1 = form1, form2 = form2)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
