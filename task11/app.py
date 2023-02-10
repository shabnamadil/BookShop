from flask import Flask, render_template


app = Flask(__name__)

Category = ['3D KITAB', 'Akademik', 'Bədii', 'Bizness', 'Detektiv' ]

Books = {
    1 : {
        'name' : 'Book 1',
        'price' : '$56',
        'images' : 'book1.jpeg',
        'Web_ID': 1234,
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    2 : {
        'name' : 'Book 2',
        'price' : '$23',
        'images' : 'book2.jpeg',
        'Web_id': 5678,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    3 : {
        'name' : 'Book 3',
        'price' : '$33',
        'images' : 'book3.jpeg',
        'Web_id': 9101112,
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    4 : {
        'name' : 'Book 4',
        'price' : '$55',
        'images' : 'book4.jpeg',
        'Web_id': 13141516,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    5 : {
        'name' : 'Book 5',
        'price' : '$12',
        'images' : 'book5.jpeg',
        'Web_id': 17181920,
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    6 : {
        'name' : 'Book 6',
        'price' : '$23',
        'images' : 'book6.jpeg',
        'Web_id': 21222324,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        }
  
}


Recommended_1 = {
    1 : {
        'name' : 'Book 7',
        'price' : '$77',
        'images' : 'book7.jpeg',
        'Web_id': 25262728,
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    2 : {
        'name' : 'Book 8',
        'price' : '$74',
        'images' : 'book8.jpeg',
        'Web_id':29303132,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    3 : {
        'name' : 'Book 9',
        'price' : '$27',
        'images' : 'book9.jpeg',
        'Web_id': 33343536,
        'Availability' : 'In Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...'
        }
}

Recommended_2 = {
    1 : {
        'name' : 'Book 10',
        'price' : '$53',
        'images' : 'book10.jpeg',
        'Web_id': 37383940,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        },
    2 : {
        'name' : 'Book 11',
        'price' : '$75',
        'images' : 'book8.jpeg',
         'Web_id': 41424344,
         'Availability' : 'In Stock',
         'Condition' : 'New',
         'Brand' : 'E-SHOPPER',
         'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
         'Review' : 'My opinion about this book'
        },
    3 : {
        'name' : 'Book 12',
        'price' : '$16',
        'images' : 'book9.jpeg',
        'Web_id': 45464748,
        'Availability' : 'Out of Stock',
        'Condition' : 'New',
        'Brand' : 'E-SHOPPER',
        'Description' : 'Oxumaq, oxumaq, yenə də oxumaq...',
        'Review' : 'My opinion about this book'
        }
}

@app.route("/")
def index():

    return render_template("index.html", Category = Category, Books = Books, Recommended_1 = Recommended_1, Recommended_2 = Recommended_2)

@app.route("/<int:id>/")
def index_cart(id):
    return render_template("book.html", Category = Category, Books = Books[id], Recommended_1 = Recommended_1, Recommended_2 = Recommended_2)


@app.route("/rec/<int:id>/")
def index_cart_recommended(id):
    return render_template("book.html", Category = Category, Books = Recommended_1[id], Recommended_1 = Recommended_1, Recommended_2 = Recommended_2)

@app.route("/rec_2/<int:id>/")
def index_cart_recommended2(id):
    return render_template("book.html", Category = Category, Books = Recommended_2[id], Recommended_1 = Recommended_1, Recommended_2 = Recommended_2)

@app.route("/product")
def product():
    return render_template("product.html", Category = Category, Books = Books)


@app.route("/product/<int:id>")
def product_detail(id):
    return render_template("book.html", Category = Category, Books = Books[id], Recommended_1 = Recommended_1, Recommended_2 = Recommended_2)