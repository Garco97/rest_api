from flask import Flask
from flask_restful import Api, Resource, reqparse
import json


app = Flask(__name__)
api = Api(app)
users  = json.load(open("users.json"))
products = json.load(open("products.json"))

class Products(Resource):
    def get(self):
        return products

class Product(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("url")
        parser.add_argument("price")
        parser.add_argument("image")

        params = parser.parse_args()
        for product in products:
            if(params["id"] == product["id"]):
                return "Quote with id "+params["id"]+" already exists", 400
        product = {
            "id":params["id"],
            "name":params["name"],
            "url":params["url"],
            "price":params["price"],
            "image":params["image"]
        }
        products.append(product)
        # Debería guardar en base de datos o algo por el estilo
        return product, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        params = parser.parse_args()
        for product in products:
            if product["id"] == params["id"]:
                products.remove(product)
                return f"Quote with id  is deleted.", 200
        return "Quote with id "+params["id"]+" dont exists", 400

class Users(Resource):
    def get(self):
        return users

class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        params = parser.parse_args()
        lista = []
        for user in users:
            if params["id"] == user["id"]:
                lista = user["product_list"]
                break
        if not lista:
            return "User with id "+params["id"]+" does not exists", 400
        product_list = []
        for product_id in lista:
            for product in products:
                if product_id == product["id"]:
                    product_list.append(product)
        return product_list, 200
api.add_resource(Product, "/product/", "/product")
api.add_resource(Products, "/products/", "/products")
api.add_resource(Users, "/users/", "/users")
api.add_resource(User, "/user/", "/user")
if __name__ == '__main__':
    app.run(debug=True)