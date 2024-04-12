import os
from app import create_app
from models.dbconfig import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurantpizza import RestaurantPizza

def insert_sample_records():
    app = create_app()
    app.app_context().push()
    db.create_all()

    # Sample restaurants
    restaurant1 = Restaurant(name='Corner Pizzeria', address='First St. 1')
    restaurant2 = Restaurant(name='Tamu Pizza Place', address='Second Av. 2')

    # Save sample restaurants
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.commit()

    # Sample pizzas
    pizza1 = Pizza(name='Margherita', description='Tomato sauce, mozzarella cheese, fresh basil')
    pizza2 = Pizza(name='Pepperoni', description='Tomato sauce, mozzarella cheese, pepperoni slices')

    # Save sample pizzas
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

    # Associate pizzas with restaurants
    RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=12.99)
    RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id, price=13.99)
    RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza1.id, price=13.99)
    RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=14.99)

    db.session.commit()

if __name__ == "__main__":
    # Insert sample records into the database
    insert_sample_records()

    print("Sample records inserted.")