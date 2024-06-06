from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load products
def load_products_data():
    with open('products.json', 'r', encoding="utf-8") as file:
        return json.load(file)
    
# Save products
def save_products_data(products):
    with open('products.json', 'w', encoding="utf-8") as file:
        json.dump(products, file, indent=4)

# welcome root msg -http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the mini eCommerce API. Use /api/products to access the products data."})

# GET /api/products
@app.route('/api/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

# GET /api/products/<id>
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    products = load_products_data()
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else (jsonify({"error": "Product not found"}), 404)

# POST /api/products
@app.route('/api/products', methods=['POST'])
def create_product():
    new_product = request.json
    products = load_products_data()

    new_product["id"] = max(p["id"] for p in products) + 1 if products else 1

    products.append(new_product)
    save_products_data(products)
    return jsonify(new_product), 201

# PUT /api/products/<id>
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products_data()
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    updated_product = request.json
    product.update(updated_product)
    save_products_data(products)
    return jsonify(product)

# DELETE /api/products/<id>
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products_data()
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    updated_list = [p for p in products if p["id"] != product_id]
    save_products_data(updated_list)
    return 'deleted product succesfully', 204

if __name__ == "__main__":
    app.run(debug=True)
