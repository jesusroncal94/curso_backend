from orator.migrations import Migration


class CreateInvoiceDetailsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('invoice_details') as table:
            table.increments('invoice_detail_id')
            table.integer('invoice_id')
            table.integer('product_id')
            table.float('price')
            table.integer('quantity')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('invoice_details')
