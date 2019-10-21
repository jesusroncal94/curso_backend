from orator.migrations import Migration


class CreateInvoicesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('invoices') as table:
            table.increments('invoice_id')
            table.integer('user_role_id')
            table.float('subtotal')
            table.float('igv')
            table.float('total')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('invoices')
