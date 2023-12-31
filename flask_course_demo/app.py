from flask import Flask,request

from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager


import models

from resources.items import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)


    api = Api(app)
    
    
    app.config["JWT_SECRET_KEY"]="217183519307548734633763543007051902334"
    jwt = JWTManager(app)

    # @app.before_first_request
    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app





# check swagger docs here
# http://127.0.0.1:5000/swagger-ui

# @app.get("/store")
# def get_all_stores():
#     return {"stores":list(stores.values())}


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404,message="Store Not Found")
#         # return {"message":"Store Not Found"},404

# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     new_store = {**store_data,"id":store_id}
#     stores[store_id] = new_store
#     return new_store,201

# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message":"Store Deleted."}
#     except KeyError:
#         abort(404,message="Item Not Found")

# #  items


# @app.get("/item")
# def get_all_items():
#     return {"items":list(items.values())}

# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if (
#         "price" not in item_data
#         or "name" not in item_data
#         or "store_id" not in item_data
#     ):
#         abort(400,message="Bad Request Ensure 'price' 'name' and 'store_id'.")
    
#     for item in items.values():
#         if(
#             item_data['name'] == item['name']
#             and item_data['store_id'] == item['store_id']
#         ):
#             abort(400,message="item already exists")
    
#     if item_data['store_id'] not in stores:
#         abort(404,message="store not found.")

#     if item_data["store_id"] not in stores:
#         abort(404,message="Store Not Found")

#     item_id = uuid.uuid4().hex
#     item = {**item_data,"id":item_id}
#     items[item_id] = item

#     return item,201


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404,message="item Not Found")


# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"Item Deleted."}
#     except KeyError:
#         abort(404,message="item Not Found")

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400,message="bad request Ensure price and name are valid")

#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404,message="Item Not Found.")




