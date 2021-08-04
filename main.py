from flask import Flask
from flask_restful import Api

from controller.controller import Image

app = Flask(__name__)
api = Api(app)
api.add_resource(Image, '/images')  # '/users' is our entry point

if __name__ == '__main__':
    app.run()
