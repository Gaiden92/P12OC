import json
from .database import Database


with open("user_config.json", "r") as file:
    config = json.load(file)

# constantes de configuration de la base de donnée
DB_USER = config["user"]
DB_PASSWORD = config["password"]
DB_HOST = config["host"]
DB_PORT = config["port"]
DB_NAME = config["name"]

DB_SCHEMA = "epic_events"
DB = Database(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA)

# constantes fichier json
TOKEN_PATH = "token/user.json"
DELAY = 30
SECRET_KEY = config["secret_key"]

# departements
SUPPORT = "support"
GESTION = "gestion"
COMMERCIAL = "commercial"

# Sentry clef publique
DSN = config["dsn"]
