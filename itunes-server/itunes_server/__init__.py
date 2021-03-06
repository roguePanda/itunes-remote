import atexit
import logging

from flask import Flask

from .advertise import NetworkAdvertiser

DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ITUNES_SERVER_SETTINGS', silent=True)

from itunes_server.json import JSONEncoder
app.json_encoder = JSONEncoder

from . import control, library
app.register_blueprint(control.mod, url_prefix='/control')
app.register_blueprint(library.mod, url_prefix='/library')

from . import auth
from . import ssl

def run():
    advertiser = NetworkAdvertiser(type='_itunes-server._tcp', port=5000)
    atexit.register(lambda: advertiser.close())

    app.run(host='0.0.0.0', ssl_context=ssl.create_ssl_context())
