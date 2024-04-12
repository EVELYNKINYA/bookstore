from .dbconfig import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    ingredients = db.Column(db.String(255))
    
    def __repr__(self):
        return f'Pizza{self.name}, {self.description}, {self.price}, {self.ingredients}'