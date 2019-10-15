import os
from orator import DatabaseManager
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

class Conexion:
    def __init__(self):
        pass
