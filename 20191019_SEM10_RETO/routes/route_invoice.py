from flask import request
from app.controllers.invoice import Invoice
from helpers import helper
import json


invoice = Invoice()



def routes(app):
    @app.route('/invoices/add', methods = ['POST'])
    @helper.token_required
    @helper.role_cajero
    def invoices_add():
        objeto = helper.token_get_object()
        invoice.user_role_id = objeto['user_role']['user_role_id']
        """
        values = request.values
        invoice.user_role_id = values.get('user_role_id')
        json_var = request.get_json()
        dumps = json.dumps(json_var)
        invoice_details_dict = json.loads(dumps)
        return f'x: {invoice_details_dict}'
        """
        invoice_details_dict = {}
        invoice_details_dict = {
            "invoice_details": [[25,5], [26,10], [27,15], [28,20]]
        }
        return invoice.add_invoice(invoice, invoice_details_dict, app)

    @app.route('/invoices/list', methods = ['GET'])
    @helper.token_required
    @helper.role_cajero
    def invoices_list():
        return invoice.list_invoices(app)

    @app.route('/invoices/delete', methods = ['DELETE'])
    @helper.token_required
    def invoices_delete():
        values = request.values
        invoice_id = values.get('invoice_id')
        return invoice.delete_invoice(invoice_id, app)

    @app.route('/invoices/find', methods = ['POST'])
    @helper.token_required
    def invoices_find():
        values = request.values
        invoice_id = values.get('invoice_id')
        invoice_name = values.get('name')
        return invoice.find_invoice(invoice_id, invoice_name, app)
