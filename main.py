from sqlalchemy.orm import sessionmaker

from config.database import Database
from config.parameters import  DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from dao.tables import Base


database = Database(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
# connection
database.connexion()
# création des tables (une fois)
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)


