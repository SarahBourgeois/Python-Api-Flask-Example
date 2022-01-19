from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    category = db.Column(db.String())
    price = db.Column(db.Integer())

    def __init__(self, title, description, category, price):
        self.title = title
        self.description = description
        self.category = category
        self.price = price

    def __repr__(self):
        return f"<Product {self.title}>"
