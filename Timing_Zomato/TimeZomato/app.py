from flask import Flask, jsonify, request
import pickle
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins='*')

def load_menu():
    try:
        with open('menu.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_menu(menu):
    with open('menu.pickle', 'wb') as f:
        pickle.dump(menu, f)

def load_orders():
    try:
        with open('orders.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_orders(orders):
    with open('orders.pickle', 'wb') as f:
        pickle.dump(orders, f)

@app.route('/menu', methods=['GET'])
def get_menu():
    menu = load_menu()
    return jsonify(menu)

@app.route('/menu/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        return jsonify(dish)
    else:
        return jsonify({'message': 'Dish not found'}), 404

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

@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = load_orders()
    return jsonify(orders)

# @app.route('/orders', methods=['POST'])
# def place_order():
#     orders = load_orders()
#     new_order = {
#         'id': orders[-1]['id'] + 1 if orders else 1,
#         'dishes': request.json['dishes'],
#         'status': 'received'
#     }
#     orders.append(new_order)
#     save_orders(orders)
#     socketio.emit('order_status', {'order_id': new_order['id'], 'status': new_order['status']}, broadcast=True)
#     return jsonify(new_order), 201

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
    socketio.send({'order_id': new_order['id'], 'status': new_order['status']}, broadcast=True)
    return jsonify(new_order), 201



# -----
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    status = request.json['status']
    socketio.emit('order_status_update', {'order_id': order_id, 'status': status}, broadcast=True)
    return '', 204

@socketio.on('connect')
def handle_connect():
    emit('connected')

@socketio.on('disconnect')
def handle_disconnect():
    emit('disconnected')

@socketio.on('order_status_updated')
def handle_order_status_update(data):
    order_id = data['order_id']
    status = data['status']
    orders = load_orders()
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        order['status'] = status
        save_orders(orders)
        emit('order_status', {'order_id': order_id, 'status': status}, broadcast=True)
    else:
        emit('order_not_found', {'order_id': order_id})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    # socketio.run(app, port=5000)
