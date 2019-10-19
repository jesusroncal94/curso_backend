from helpers import helper
from app.models.business import Business as BusinessModel


class Business():
    def __init__(self, ruc = None, name = None, address = None):
        self.ruc = ruc
        self.name = name
        self.address = address

    def add_business(self, business, app):
        try:
            BusinessModel.insert({
                'ruc': business.ruc,
                'name': business.name,
                'address': business.address
            })
            message = f'''Se agregó el negocio {business.name} con ruc {business.ruc}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def list_business(self, app):
        business_dict = {}
        try:
            business = BusinessModel.get()
            business_dict = business.serialize()
            message = f'''Lista de negocios'''
            print(message)
            return helper.handler_response(app, 201, message, business_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_business(self, business_id, business, app):
        try:
            BusinessModel \
                .where('business_id', business_id) \
                .update({
                'ruc': business.ruc, 
                'name': business.name,
                'address': business.address
            })
            message = f'''Se actualizó el negocio: {business.name} con ruc {business.ruc}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_business(self, business_id, app):
        try:
            BusinessModel \
                .where('business_id', business_id) \
                .delete()
            message = f'''Se eliminó el negocio: {business_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_business(self, business_id, business_name, app):
        businesss_dict = {}
        try:
            businesss = BusinessModel \
                .where('business_id', business_id) \
                .or_where('name', business_name) \
                .first()
            businesss_dict = businesss.serialize()
            message = f'''Búsqueda de negocio'''
            print(message)
            return helper.handler_response(app, 201, message, businesss_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
