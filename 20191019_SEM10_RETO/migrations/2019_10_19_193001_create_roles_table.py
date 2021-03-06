from orator.migrations import Migration


class CreateRolesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('roles') as table:
            table.increments('role_id')
            table.string('name')
            table.integer('status')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('roles')
