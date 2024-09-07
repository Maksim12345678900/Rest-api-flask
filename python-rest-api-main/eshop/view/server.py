from flask import Flask, request
from marshmallow import ValidationError
from business_logic.product_usecases import product_create, product_get_many, product_get_by_id
from view.product_schemas import ProductCreateDtoSchema, ProductSchema, ProductGetManyParams

app = Flask(__name__)

@app.post("/api/v1/product")
def product_create_endpoint():
    try:
        product_create_dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    product = product_create(product_create_dto)
    return ProductSchema().dump(product), 201

@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    products = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )
    return ProductSchema(many=True).dump(products)

@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id):
    product = product_get_by_id(id)
    if product is None:
        return {"error": 'Not found'}, 404
    return ProductSchema().dump(product)

if __name__ == "__main__":
    app.run(debug=True)
