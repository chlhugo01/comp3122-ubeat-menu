import json
from types import new_class
import redis
import requests

redis_conn = redis.Redis(host='message_queue', port=6379)
