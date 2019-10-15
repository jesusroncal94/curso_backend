from flask import Flask, request
from dotenv import load_dotenv
from pathlib import Path
from routes import route_index, route_area, route_cargo, route_empleado, route_cargo_empleado, route_error


env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)
app = Flask(__name__)

route_index.routes(app)
route_area.routes(app)
route_cargo.routes(app)
route_empleado.routes(app)
route_cargo_empleado.routes(app)
route_error.error_handler(app)

if __name__ == '__main__':
    app.run()
