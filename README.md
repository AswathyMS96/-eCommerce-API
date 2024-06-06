# Build a mini eCommerce API


** Build a mini eCommerce API using Python and Flask.

`` This API should implement the following endpoints,``

1.  GET /api/products

2. GET /api/products/<id>

3. POST /api/products

4. PUT /api/products/<id>

5. DELETE /api/products/<id>

Data should be retrieved from .json file and saved to same file.

ans:

## Explanation and Steps to Run:
### Routes Definition:

1.  /api/products [GET]: Returns a list of all products.

2. /api/products/<id> [GET]: Returns a specific product by ID.

3. /api/products [POST]: Creates a new product.

4. /api/products/<id> [PUT]: Updates an existing product by ID.

5. /api/products/<id> [DELETE]: Deletes a product by ID.

## Ensure products.json Exists:

Make sure that products.json file exists in the same directory as app.py with the provided data.
`` Run the Application: ``

  Navigate to the directory containing app.py.
  Run the application with the command:
      ``   python app.py``
The Flask server will start, and the endpoints will be accessible at 
`` http://127.0.0.1:5000/api/products.``

![image](https://github.com/AswathyMS96/-eCommerce-API/assets/146731424/8427837a-9d92-4ef7-acbb-faacb1c9e701)
