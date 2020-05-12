from flask import Flask
from uuid import getnode as get_mac
import os
APP = Flask(__name__)


@APP.route('/')
def positive_results_query():

    return get_mac().__str__()


APP.run(host='0.0.0.0', port=5000,debug=True)
