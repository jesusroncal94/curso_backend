from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes import route_index, route_business, route_role, route_user, route_user_role, route_error, route_prueba


env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)
app = Flask(__name__)

route_index.routes(app)
route_business.routes(app)
route_user.routes(app)
route_role.routes(app)
route_user_role.routes(app)
route_error.error_handler(app)
route_prueba.routes(app)

if __name__ == '__main__':
    app.run()
