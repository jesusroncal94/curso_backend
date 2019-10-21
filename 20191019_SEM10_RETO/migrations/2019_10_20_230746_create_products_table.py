from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('products') as table:
            table.increments('product_id')
            table.string('name')
            table.float('price')
            table.integer('quantity')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('products')
