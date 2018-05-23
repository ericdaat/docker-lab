from flask import Flask, request
import redis
import os

app = Flask(__name__)
cache_db = redis.StrictRedis(host=os.environ['REDIS_HOST'])


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/cache/<key>', methods=['GET', 'POST'])
def cache(key):
    if request.method == 'POST':
        value = request.form['value']
        cache_db.set(name=key, value=value, ex=30)

        return 'done'

    value_in_cache = cache_db.get(key)

    return 'Value {0} equals {1}'.format(key, value_in_cache)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
