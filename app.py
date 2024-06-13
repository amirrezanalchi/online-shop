from flask import Flask
from shop.controllers.user_controller import user_blueprint
from shop.controllers.store_controller import store_blueprint
from shop.controllers.product_controller import product_blueprint
from shop.controllers.order_controller import order_blueprint
from shop.view.view import views_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(store_blueprint, url_prefix='/store')
app.register_blueprint(product_blueprint, url_prefix='/product')
app.register_blueprint(order_blueprint, url_prefix='/order')
app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
