from flask_restful import Resource

from mongo_functions.function import read_from_mongo


class Image(Resource):
    def get(self):
        return {"data": read_from_mongo()}, 200
