from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('mongodb+srv://faizanmd:faizan123@cluster0.defifv6.mongodb.net/hellodatabase?retryWrites=true&w=majority')

db = client['pydatabase']
collection = db['Customers']
# --- Adding only one data
# @app.route('/add_customer', methods=['POST'])
# def add_customer():
#     customer_data = request.get_json()
#     result = collection.insert_one(customer_data)
#     return jsonify({'message': 'Customer added successfully', 'id': str(result.inserted_id)})

@app.route('/add_customer', methods=['POST'])
def add_customers():
    customers_data = request.get_json()
    
    # Check if the received data is a list
    if not isinstance(customers_data, list):
        return jsonify({'message': 'Invalid data format. Expected a list of customers.'}), 400
    
    # Validate each customer object before insertion
    inserted_ids = []
    for customer in customers_data:
        if not all(field in customer for field in ['id', 'name', 'email', 'address', 'phone_number']):
            return jsonify({'message': 'Invalid customer data format. Missing required fields.'}), 400
        result = collection.insert_one(customer)
        inserted_ids.append(str(result.inserted_id))
    
    return jsonify({'message': 'Customers added successfully', 'ids': inserted_ids})

# ---
@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    data = list(collection.find())
    return jsonify(data)

# ---
@app.route('/fetch_customerid', methods=['GET'])
def fetch_customer():
    customer = collection.find_one({'id': '33'})
    if customer:
        return jsonify(customer)
    else:
        return jsonify({'message': 'Customer not found'})


if __name__ == '__main__':
    # Create an index for the id field to ensure uniqueness
    collection.create_index("id", unique=True)
    app.run(port=8080)
    