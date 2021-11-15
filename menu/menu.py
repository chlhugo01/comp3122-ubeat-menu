import flask
import pymongo
import json
import redis

##############################
# Init library / connections
#######3######################
flask_app = flask.Flask(__name__)
mongo_client = pymongo.MongoClient('mongodb://comp3122:23456@menu_db:27017')
redis_conn = redis.Redis(host='message_queue', port=6379)

db = mongo_client["menu"]
col = db["restaurants"]

##################
# Flask endpoints
##################


if __name__ == '__main__':
    redis_pubsub = redis_conn.pubsub()
    redis_pubsub.subscribe(**{'menu_deleteFood': delete_food})
    redis_pubsub_thread = redis_pubsub.run_in_thread(sleep_time=0.001)
    flask_app.run(host='0.0.0.0', debug=True, port=15000)


