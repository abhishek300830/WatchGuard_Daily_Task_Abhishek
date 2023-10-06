import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort,Blueprint
from sqlalchemy.exc import SQLAlchemyError,IntegrityError


from schemas import StoreSchema
from models import StoreModel
from db import stores,db

blp = Blueprint("stores",__name__,description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
        
        # try:
        #     return stores[store_id]
        # except KeyError:
        #     abort(404,message="Store Not Found")
    
    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        
        return {"message":"store deleted."}
        # raise NotImplementedError("Delete store is not implemented yet")
        # try:
        #     del stores[store_id]
        #     return {"message":"Store Deleted."}
        # except KeyError:
        #     abort(404,message="Item Not Found")

@blp.route("/store")
class StoreList(MethodView):

    @blp.response(200,StoreSchema(many=True))
    def get(self):
        # return {"stores":list(stores.values())}
        # return stores.values()
        return StoreModel.query.all()
    
    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,store_data):
        # store_data = request.get_json()
        # if "name" not in store_data:
        #     abort(400,message="bad Request,name is not included in json Data.")

        # for store in stores.values():
        #     if store_data["name"] == store["name"]:
        #         abort(400,message="Store Already Exists")

        # store_id = uuid.uuid4().hex
        # new_store = {**store_data,"id":store_id}
        # stores[store_id] = new_store

        new_store = StoreModel(**store_data)

        try:
            db.session.add(new_store)
            db.session.commit()
        except IntegrityError:
            abort(400,message="A store with this name exists")
        except SQLAlchemyError:
            abort(500,message="An Error Occured while creating a Store")

        return new_store