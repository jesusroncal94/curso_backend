from orator.migrations import Migration


class CreateUserRolesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user_roles') as table:
            table.increments('id')
            table.integer('user_id')
            table.integer('role_id')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user_roles')
