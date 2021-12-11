import flask
from redis import StrictRedis
from threading import Thread

# initialize our Flask application, Redis server, and Keras model

app = flask.Flask(__name__)
db = StrictRedis(host="localhost", port=6379, db=0)
model = None

from app import routes
