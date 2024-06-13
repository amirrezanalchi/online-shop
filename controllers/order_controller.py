from flask import Blueprint, request, jsonify
from shop.model.da.database import DatabaseManager
from shop.model.entity.order import Order, OrderProduct
from shop.model.entity.user import User
from shop.model.entity.product import Product
from shop.model.entity.store import Store

order_blueprint = Blueprint('order', __name__)
db_manager = DatabaseManager()

@order_blueprint.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    store_id = data.get('store_id')
    product_ids = data.get('product_ids')

    if not user_id or not store_id or not product_ids:
        return jsonify({'message': 'User ID, store ID, and product IDs required'}), 400

    user = db_manager.filter(User, id=user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    store = db_manager.filter(Store, id=store_id)
    if not store:
        return jsonify({'message': 'Store not found'}), 404

    total_price = 0.0
    products = []
    for product_id in product_ids:
        product = db_manager.filter(Product, id=product_id)
        if product:
            total_price += product[0].price
            products.append(product[0])
        else:
            return jsonify({'message': f'Product with id {product_id} not found'}), 404

    if user[0].balance < total_price:
        return jsonify({'message': 'Insufficient balance'}), 400

    new_order = Order(user_id=user_id, store_id=store_id, total_price=total_price)
    db_manager.add(new_order)

    for product in products:
        order_product = OrderProduct(order_id=new_order.id, product_id=product.id)
        db_manager.add(order_product)

    user[0].balance -= total_price
    db_manager.update()

    return jsonify({'message': 'Order created successfully', 'order_id': new_order.id}), 201
