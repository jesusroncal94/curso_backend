from flask import request
from app.controllers.business import Business
from helpers import helper


business = Business()



def routes(app):
    @app.route('/business/add', methods = ['POST'])
    @helper.token_required
    @helper.role_superadmin
    def business_add():
        values = request.values
        business.ruc = values.get('ruc')
        business.name = values.get('name')
        business.address = values.get('address')
        return business.add_business(business, app)

    @app.route('/business/list', methods = ['GET'])
    @helper.token_required
    @helper.role_superadmin
    def business_list():
        return business.list_business(app)

    @app.route('/business/update', methods = ['PUT'])
    @helper.token_required
    @helper.role_superadmin
    def business_update():
        values = request.values
        business_id = values.get('business_id')
        business.ruc = values.get('ruc')
        business.name = values.get('name')
        business.address = values.get('address')
        return business.update_business(business_id, business, app)

    @app.route('/business/delete', methods = ['DELETE'])
    @helper.token_required
    @helper.role_superadmin
    def business_delete():
        values = request.values
        business_id = values.get('business_id')
        return business.delete_business(business_id, app)

    @app.route('/business/find', methods = ['POST'])
    @helper.token_required
    @helper.role_superadmin
    def business_find():
        values = request.values
        business_id = values.get('business_id')
        business_name = values.get('name')
        return business.find_business(business_id, business_name, app)
