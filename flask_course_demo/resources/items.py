import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError

from db import items,db
from models import ItemModel
from schemas import ItemSchema,ItemUpdateSchema





blp = Blueprint("items",__name__,description="Operation on items")

@blp.route("/items/<string:item_id>")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
        
        # try:
        #     return items[item_id]
        # except KeyError:
        #     abort(404,message="item not found")
    
    def delete(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        
        db.session.delete(item)
        db.session.commit()
        
        return {"message":"item deleted."}
        # raise NotImplementedError("Deleteing an item is not implemented")
        # try:
        #     del items[item_id]
        #     return {"message":"Item Deleted."}
        # except KeyError:
        #     abort(404,message="Item not found")
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self,item_data, item_id):
        
        item = ItemModel.query.get_or_404(item_id)
        
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id,**item_data)
        
        db.session.add(item)
        db.session.commit()
        
        return item
        # raise NotImplementedError("Deleteing an item is not implemented")
    
        # item_data = request.get_json()

        # if "price" not in item_data or "name" not in item_data:
        #     abort(400,message="Bad request, Ensure name and price")

        # try:
        #     item = items[item_id]
        #     item |= item_data

        #     return item
        # except KeyError:
        #     abort(404,message="Item not Found")

@blp.route("/item")
class ItemList(MethodView):

    @blp.response(200,ItemSchema(many=True))
    def get(self):
        # return {"items":list(items.values())}
        # return items.values()
        return ItemModel.query.all()
    
    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self,item_data):
        # item_data = request.get_json()
        # if (
        #     "price" not in item_data
        #     or "name" not in item_data
        #     or "store_id" not in item_data
        # ):
        #     abort(400,message="Bad Request Ensure 'price' 'name' and 'store_id'.")
        #  this is replaces by marshmallow schemna @blp.arguments
        
        # for item in items.values():
        #     if(
        #         item_data['name'] == item['name']
        #         and item_data['store_id'] == item['store_id']
        #     ):
        #         abort(400,message="item already exists")
        

        # item_id = uuid.uuid4().hex
        # item = {**item_data,"id":item_id}
        # items[item_id] = item

        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="An error occured while inserting data")

        return item 

