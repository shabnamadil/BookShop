from extensions import db

from app import app



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
    book = db.relationship('Book', backref = 'janr')

    def __repr__(self) :
        return self.genre

    def __init__(self, genre):
        self.genre = genre  
       
    def save(self):
        db.session.add(self)
        db.session.commit()