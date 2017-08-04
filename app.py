from flask import Flask
from uuid import getnode as get_mac
from redis import Redis

APP = Flask(__name__)
redis = Redis(host='redis', port=6379)


@APP.route('/')
def positive_results_query():
    count = redis.incr('hits')

    return get_mac().__str__() + ' haha ! 1I have been seen {} times.\n'.format(count)


APP.run(host='0.0.0.0', port=5000,debug=True)
