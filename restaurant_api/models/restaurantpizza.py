from .dbconfig import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    
    restaurant = db.relationship('Restaurant', backref='restaurant_pizzas')
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')

def __repr__(self):
    return f'RestaurantPizza{self.price}, {self.restaurant_id}, {self.pizza_id}'

# class RestaurantPizza(db.Model):
#     rest_id = db.Column(db.ForeignKey('restaurants.id'), primary_key=True)
#     pizza_id = db.Column(db.ForeignKey('pizzas.id'), primary_key=True)

#     rest = db.relationship("Restaurant", backref="associated_restaurants")
#     pizza = db.relationship("Pizza", backref="associated_pizzas")
