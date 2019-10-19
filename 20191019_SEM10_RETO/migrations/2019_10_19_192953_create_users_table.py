from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('user_id')
            table.string('username')
            table.string('password')
            table.string('name')
            table.string('last_name')
            table.integer('age')
            table.string('gender')
            table.integer('status')
            table.nullable_timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
