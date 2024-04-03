from .database import Database


# constantes de configuration de la base de donnée
DB_USER = "postgres"
DB_PASSWORD = "superadmin"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "postgres"
DB_SCHEMA = "epic_events"
DB = Database(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA)

# constantes fichier json
TOKEN_PATH = "token/user.json"
DELAY = 30

# departements
SUPPORT = "support"
GESTION = "gestion"
COMMERCIAL = "commercial"
