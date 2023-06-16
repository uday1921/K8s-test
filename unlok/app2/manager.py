from flask import Flask, request, Response, jsonify
from flask_restful import Api, Resource
import logging
import json

app = Flask(__name__)
api = Api(app)

log = app.logger
log.setLevel(logging.DEBUG)


# @app.route("/")
# def hello_world():
    # return "Hello, World!"

class Backend(Resource):
    def __init__(self):
        logging.info("Into INIT Method...")
        name = "uday"
        logging.info("Name:{}".format(name))
    @staticmethod
    def post(self):
        data = json.loads(request.data)
        logging.info("Received data:{}".format(data))
    def get(self):
        return "Hii UDAY From application2"

api.add_resource(Backend, '/app2', endpoint="/app2")

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8080)