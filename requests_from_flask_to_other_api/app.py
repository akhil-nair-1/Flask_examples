from flask import Flask
from flask_restful import Api, Resource
import requests
import json

app = Flask(__name__)
api = Api(app)

URL = "https://reqres.in/api/users?page=2"

class ExternalData(Resource):
    def get(self):

        # Gets the data from a custom url
        response_from_api = requests.get(URL)
        
        # Serializes a json into a python object
        data = json.loads(response_from_api.text)

        return {"external data recovered": data["data"]}


api.add_resource(ExternalData, '/')

app.run(port=5000)