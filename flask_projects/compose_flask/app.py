import time

from flask import Flask
from redis import Redis

app = Flask(__name__)
cache = Redis(host='localhost', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    cache.incr('hits')
    return 'This compose has been viewed {} time(s)'.format('hits')

