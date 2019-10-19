from orator.migrations import Migration


class CreateBusinessTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('business') as table:
            table.increments('business_id')
            table.string('ruc')
            table.string('name')
            table.string('address')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('business')
