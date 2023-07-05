from flask import Flask, jsonify, request
import pickle
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_menu():
    try:
        with open('menu.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Save menu to file
def save_menu(menu):
    with open('menu.pickle', 'wb') as f:
        pickle.dump(menu, f)

# Load orders from file
def load_orders():
    try:
        with open('orders.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Save orders to file
def save_orders(orders):
    with open('orders.pickle', 'wb') as f:
        pickle.dump(orders, f)

# GET all dishes in the menu
@app.route('/menu', methods=['GET'])
def get_menu():
    menu = load_menu()
    return jsonify(menu)

# GET a specific dish by ID
@app.route('/menu/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        return jsonify(dish)
    else:
        return jsonify({'message': 'Dish not found'}), 404

# POST a new dish to the menu
@app.route('/menu', methods=['POST'])
def add_dish():
    menu = load_menu()
    new_dish = {
        'id': menu[-1]['id'] + 1 if menu else 1,
        'name': request.json['name'],
        'description': request.json['description'],
        'price': request.json['price'],
        'available': True
    }
    menu.append(new_dish)
    save_menu(menu)
    return jsonify(new_dish), 201

# PUT (update) a dish's availability
@app.route('/menu/<int:dish_id>', methods=['PUT'])
def update_availability(dish_id):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        dish['available'] = request.json['available']
        save_menu(menu)
        return jsonify(dish)
    else:
        return jsonify({'message': 'Dish not found'}), 404

# DELETE a dish from the menu
@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        menu.remove(dish)
        save_menu(menu)
        return jsonify({'message': 'Dish deleted'})
    else:
        return jsonify({'message': 'Dish not found'}), 404

# GET all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = load_orders()
    return jsonify(orders)

# POST a new order
@app.route('/orders', methods=['POST'])
def place_order():
    orders = load_orders()
    new_order = {
        'id': orders[-1]['id'] + 1 if orders else 1,
        'dishes': request.json['dishes'],
        'status': 'received'
    }
    orders.append(new_order)
    save_orders(orders)
    return jsonify(new_order), 201

# PUT (update) an order's status
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    orders = load_orders()
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        order['status'] = request.json['status']
        save_orders(orders)
        return jsonify(order)
    else:
        return jsonify({'message': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
