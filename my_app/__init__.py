from flask import Flask
from my_app.product.views import product_blueprint
from redis import Redis

app = Flask(__name__)
app.register_blueprint(product_blueprint)
redis = Redis()
