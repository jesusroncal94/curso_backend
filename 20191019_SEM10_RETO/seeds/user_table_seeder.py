from orator.seeds import Seeder
import bcrypt


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        password = '12345'
        hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.db.table('users').insert({
            'username': 'jesusroncal94',
            'password': hash_pw,
            'name': 'Jesus',
            'last_name': 'Roncal',
            'age': 25,
            'gender': 'M',
            'status': 0
        })
