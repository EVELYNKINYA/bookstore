from .dbconfig import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', backref='restaurants')

    def __repr__(self):   
        return f'Restaurant{self.name}, {self.address}'