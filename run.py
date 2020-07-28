from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)
users  = json.load(open("users.json",))
products = json.load(open("products.json",))

class Product(Resource):
    def get(self, id):
        print(id)
        id = int(id)
        for product in products:
            if(product["id"] is id):
                return product, 200
        return "Product not found", 404

    """  
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if(id == quote["id"]):
                return f"Quote with id {id} already exists", 400
        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }
        ai_quotes.append(quote)
        return quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if(id == quote["id"]):
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200
        
        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }
        
        ai_quotes.append(quote)
        return quote, 201

    def delete(self, id):
        global ai_quotes
        ai_quotes = [quote for quote in ai_quotes if quote["id"] != id]
        return f"Quote with id {id} is deleted.", 200
 """
api.add_resource(Product, "/products/","/products/<string:id>")
if __name__ == '__main__':
    app.run(debug=True)