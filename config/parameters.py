from .database import Database

# constantes de configuration de la base de donnée
DB_USER = "postgres"

# Modifier les données en fonction de votre configuration :
# (mot de passe admin, port, nom de la base de donnée)
DB_PASSWORD = "superadmin"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "postgres"
DB_SCHEMA = "epic_events"
DB = Database(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA)

# constantes fichier json
TOKEN_PATH = "token/user.json"
DELAY = 30
SECRET_KEY = "maclesecrete"

# departements
SUPPORT = "support"
GESTION = "gestion"
COMMERCIAL = "commercial"

# Sentry clef publique
DSN = "https://0564a7dfdb9cb640b6049d9369aa2cfd@\
    o4507008616759296.ingest.us.sentry.io/4507008619839488"
