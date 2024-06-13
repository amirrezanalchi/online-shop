from flask import Blueprint, request, jsonify
from shop.model.da.database import DatabaseManager
from shop.model.entity.product import Product

product_blueprint = Blueprint('product', __name__)
db_manager = DatabaseManager()

@product_blueprint.route('/<int:store_id>', methods=['GET'])
def get_products(store_id):
    products = db_manager.filter(Product, store_id=store_id)
    return jsonify([{'id': product.id, 'name': product.name} for product in products]), 200

@product_blueprint.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    store_id = data.get('store_id')

    if not name or not store_id:
        return jsonify({'message': 'Product name and store ID required'}), 400

    new_product = Product(name=name, store_id=store_id)
    db_manager.add(new_product)

    return jsonify({'message': 'Product added successfully'}), 201
