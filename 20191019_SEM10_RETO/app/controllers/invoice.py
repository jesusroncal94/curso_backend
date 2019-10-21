from helpers import helper
from app.models.invoice import Invoice as InvoiceModel
from app.models.invoice import User_roleModel
from app.models.invoice import Invoice_detailModel
from app.models.invoice import ProductModel


class Invoice():
    def __init__(self, user_role_id = None, subtotal = None, igv = None, total = None):
        self.user_role_id = user_role_id
        self.subtotal = subtotal
        self.igv = igv
        self.total = total

    def add_invoice(self, invoice, invoice_details_dict, app):
        invoice_details = []
        invoice_details = invoice_details_dict['invoice_details']
        try:
            user_role_found = User_roleModel.find(invoice.user_role_id)
            if user_role_found:
                try:
                    invoice_id = InvoiceModel.insert_get_id({
                        'user_role_id': invoice.user_role_id
                    })
                    #INSERCION DE DETALLES DE FACTURA
                    product_found_dict = {}
                    subtotal = 0
                    #RECORRE LOS DETALLES DE LA FACTURA DE FORMATO [[product_id1, cantidad1], [product_id2, cantidad2], ...]
                    for i in range(len(invoice_details)):
                        product_id = invoice_details[i][0]
                        quantity = invoice_details[i][1]
                        product_found = ProductModel.where('product_id', product_id).get().first()
                        product_found_dict = product_found.serialize()
                        price = product_found_dict['price']
                        #VALIDA SI EL PRODUCTO EXISTE
                        if product_found:
                            #VALIDA SI LA CANTIDAD DESEADA ES MENOR O IGUAL STOCK DISPONIBLE
                            if quantity <= product_found_dict['quantity']:
                                #VALIDA SI LA CANTIDAD ES UN ENTERO VÁLIDO
                                if quantity > 0:
                                    Invoice_detailModel.insert({
                                        'invoice_id': invoice_id,
                                        'product_id': product_id,
                                        'price': price,
                                        'quantity': quantity
                                    })
                                    stock_updated = product_found_dict['quantity'] - quantity
                                    ProductModel \
                                    .where('product_id', product_id) \
                                    .update({
                                        'quantity': stock_updated
                                    })
                                    subtotal = subtotal + (quantity * price)
                                else:
                                    message = f'''Cantidad deseada no puede ser menor o igual a 0: {product_found_dict['name']}-{product_found_dict['product_id']}!, Cantidad deseada: {quantity}'''
                                    print(message)
                                    return helper.handler_response(app, 401, message)
                            else: 
                                message = f'''Stock insuficiente de producto {product_found_dict['name']}-{product_found_dict['product_id']}! Stock actual: {product_found_dict['quantity']}, Cantidad deseada: {quantity}'''
                                print(message)
                                return helper.handler_response(app, 401, message)
                        else:
                            message = f'''Producto {product_id} no encontrado'''
                            print(message)
                            return helper.handler_response(app, 401, message)
                    #AQUÍ TERMINA LA INSERCIÓN DE DETALLES DE FACTURA
                    igv = subtotal * 0.18
                    total = subtotal + igv
                    InvoiceModel \
                    .where('invoice_id', invoice_id) \
                    .update({
                        'subtotal': subtotal,
                        'igv': igv,
                        'total': total
                    })
                    message = f'''Se agregó la factura: {invoice_id}'''
                    print(message)
                    return helper.handler_response(app, 201, message)
                except Exception as e:
                    return helper.handler_response(app, 500, f'xdxdError: {str(e)}')
        except Exception as e:
            return helper.handler_response(app, 500, f'aeaError: {str(e)}')

    def list_invoices(self, app):
        invoices_dict = {}
        try:
            invoices = InvoiceModel.get()
            invoices.load('user_role', 'invoice_details')
            invoices_dict = invoices.serialize()
            message = f'''Lista de facturas'''
            print(message)
            return helper.handler_response(app, 201, message, invoices_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def delete_invoice(self, invoice_id, app):
        try:
            InvoiceModel \
                .where('invoice_id', invoice_id) \
                .delete()
            message = f'''Se eliminó la factura: {invoice_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')

    def find_invoice(self, invoice_id, invoice_name, app):
        invoices_dict = {}
        try:
            invoices = InvoiceModel \
                .where('invoice_id', invoice_id) \
                .first()
            invoices_dict = invoices.serialize()
            message = f'''Lista de facturas'''
            print(message)
            return helper.handler_response(app, 201, message, invoices_dict)
        except Exception as e:
            return helper.handler_response(app, 500, f'Error: {str(e)}')
"""
    def add_invoice_details(self, invoice_id, invoice_details, app):
        subtotal = 0
        product_found_dict = {}
        for i in range(len(invoice_details)):
            product_id = invoice_details[i][0]
            quantity = invoice_details[i][1]
            product_found = ProductModel.where('product_id', product_id).get().first()
            product_found_dict = product_found.serialize()
            price = product_found_dict['price']
            if product_found:
                if quantity < product_found_dict['quantity']:
                    Invoice_detailModel.insert({
                        'invoice_id': invoice_id,
                        'product_id': product_id,
                        'price': price,
                        'quantity': quantity
                    })
                    subtotal = subtotal + (quantity * price)
                else: 
                    message = f'''Stock insuficiente! Stock actual: {product_found_dict['quantity']}, Cantidad deseada: {quantity}'''
                    print(message)
                    return helper.handler_response(app, 401, message)
            else:
                message = f'''Producto {product_id} no encontrado'''
                print(message)
                return helper.handler_response(app, 401, message)
        return subtotal
"""