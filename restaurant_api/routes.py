from flask import Flask, jsonify, request, abort
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurantpizza import RestaurantPizza
from models.dbconfig import db
from flask_cors import CORS

# Define the Flask application
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    # Route to get all restaurants
    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        return jsonify([{
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        } for restaurant in restaurants])

    # Route to get a specific restaurant by ID
    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            pizzas = Pizza.query.join(RestaurantPizza).filter(RestaurantPizza.restaurant_id == id).all()
            pizzas_data = [{
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.description
            } for pizza in pizzas]
            return jsonify({
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas_data
            })
        else:
            abort(404, jsonify({'error': 'Restaurant not found'}))

    # Route to delete a restaurant by ID
    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            # Delete associated restaurant_pizzas
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            abort(404, jsonify({'error': 'Restaurant not found'}))

    # Route to get all pizzas
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas(): 
        pizzas = Pizza.query.all()
        return jsonify([{
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.description
        } for pizza in pizzas])

    # Route to create a new restaurant_pizza
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
    #def create_restaurant_pizza():
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not price or not pizza_id or not restaurant_id:
            abort(400, jsonify({'errors': ['price', 'pizza_id', 'restaurant_id']}))

        # Check if pizza and restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        if not pizza:
            abort(400, jsonify({'error': 'Pizza not found'}))
        if not restaurant:
            abort(400, jsonify({'error': 'Restaurant not found'}))

        # Create a new RestaurantPizza instance
        new_restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.description
        })

    return app