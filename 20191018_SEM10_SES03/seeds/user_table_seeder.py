from orator.seeds import Seeder


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert({
            'name': 'Jesus',
            'last_name': 'Roncal',
            'age': 25,
            'gender': 'M',
            'status': 0
        })
