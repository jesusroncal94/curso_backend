from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes import route_index, route_user, route_role, route_user_role, route_error


env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)
app = Flask(__name__)

route_index.routes(app)
route_user.routes(app)
route_role.routes(app)
route_user_role.routes(app)
route_error.error_handler(app)

if __name__ == '__main__':
    app.run()
