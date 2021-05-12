import flask
import redis
from threading import Thread

# initialize our Flask application, Redis server, and Keras model

app = flask.Flask(__name__)
db = redis.StrictRedis(host="localhost", port=6379, db=0)
model = None

from app import routes
