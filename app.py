# import requests
# req =requests.get("https://www.google.com")
# print(req.status_code)

from flask import Flask, jsonify, request
import json

app =Flask(__name__)

#load products
def load_products_data():
    with open('products.json', 'r', encoding="utf-8") as file:
        return json.load(file)
    
#save
def save_products_data(products):
    with open('products.json', 'w', encoding="utf-8") as file:
      json.dump(products, file, indent=4)
      
#http://127.0.0.1:5000/  -GET
# @app.route('/', methods=['GET'])
# def hello():
#     return "hello"


#GET /api/products

@app.route('/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

#GET /api/products/<id>

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    products = load_products_data()
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    return jsonify(product) if product else ('product not found', 404)

#POST /products  //create new product-just add
# @app.route('/products', methods=['POST'])
# def create_product():
#     new_product = request.json
#     return new_product

#added & save new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    
    products = load_products_data()
    products.append(new_product)
    save_products_data(products)
    return new_product

#PUT  update the products
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products_data()
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    updated_product = request.json #data received from frontend
    product.update(updated_product)
    save_products_data(products)
    return updated_product


#DELETE  delete the products
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products_data()
    
    updated_list = list(filter(lambda p: p["id"] !=product_id, products))
    save_products_data(updated_list)
    return 'deleted product succesfully', 204

app.run(debug=True)
