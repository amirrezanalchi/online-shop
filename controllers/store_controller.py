from flask import Blueprint, request, jsonify
from shop.model.da.database import DatabaseManager
from shop.model.entity.store import Store

store_blueprint = Blueprint('store', __name__)
db_manager = DatabaseManager()

@store_blueprint.route('/', methods=['GET'])
def get_stores():
    stores = db_manager.query(Store)
    return jsonify([{'id': store.id, 'name': store.name} for store in stores]), 200

@store_blueprint.route('/', methods=['POST'])
def add_store():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Store name required'}), 400

    new_store = Store(name=name)
    db_manager.add(new_store)

    return jsonify({'message': 'Store added successfully'}), 201
