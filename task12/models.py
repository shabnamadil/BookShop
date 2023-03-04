from extensions import db, login_manager

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Userman.query.get(user_id)

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(40), unique = True)
    author = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.Text())
    image_url = db.Column(db.String(250),)
    in_stock = db.Column(db.Boolean(), nullable = False)
    genre = db.Column(db.String(40), nullable = False)
    language = db.Column(db.String(40), nullable = False)
    publisher = db.Column(db.String(60))
    genre_id = db.Column(db.Integer(), db.ForeignKey('genre.id'))
    comments = db.relationship('Comment', backref = 'comment')

    def __repr__(self) :
        return self.title
    
    def __init__(self, title, author, price, description, image_url, in_stock, genre, language, publisher, genre_id):
        self.title = title 
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.in_stock = in_stock
        self.genre = genre 
        self.language = language
        self.publisher = publisher
        self.genre_id = genre_id

    def save(self):
        db.session.add(self)
        db.session.commit()

class Genre(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    genre = db.Column(db.String(40), nullable = False)
    book = db.relationship('Book', backref = 'genre2')

    def __repr__(self) :
        return self.genre

    def __init__(self, genre):
        self.genre = genre  
       
    def save(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    comments = db.Column(db.Text())
    date= db.Column(db.DateTime())
    book_id = db.Column(db.Integer(), db.ForeignKey('book.id'))

    def __repr__(self) :
        return self.username

    def __init__(self, username, email, comments, date):
        self.username = username
        self.email = email
        self.comments = comments
        self.date = date

    def save(self):
        db.session.add(self)
        db.session.commit()



class Userman(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    username = db.Column(db.String(40), unique = True, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(255), nullable = False)

    def __repr__(self) :
        return self.name
    
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()


    
    
    