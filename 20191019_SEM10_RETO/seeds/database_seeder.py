from orator.seeds import Seeder
from seeds.user_table_seeder import UserTableSeeder
from seeds.role_table_seeder import RoleTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UserTableSeeder)
        self.call(RoleTableSeeder)
