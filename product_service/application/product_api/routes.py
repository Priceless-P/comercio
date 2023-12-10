from application.product_api import product_api_blueprint
from application import db
from application.models import Product
from flask import request, jsonify, make_response

@product_api_blueprint.route('/api/products')
def products():
    """Returns all available products"""
    items = []
    products = Product.query.all()
    for product in products:
        items.append(product.to_json())
    response = jsonify({'results': items})
    return response

@product_api_blueprint.route('/api/product/<slug>')
def product(slug):
    """Return a particular product given its slug"""
    product = Product.query.filter_by(slug=slug).first()
    if product is not None:
        response = jsonify({'result': product.to_json()})
    else:
        response = make_response({'message': 'Product not found'}), 404
    return response

@product_api_blueprint.route('/api/product/create', methods=['POST'])
def post_create():
    item = Product()
    item.name = request.form['name']
    item.price = request.form['price']
    item.slug = request.form['slug']
    if 'image' in request.form:
        item.image = request.form['image']

    db.session.add(item)
    db.session.commit()

    response = jsonify({'message': 'Product added', 'product': item.to_json()})
    return response
