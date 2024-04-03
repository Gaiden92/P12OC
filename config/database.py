from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base


class Database:
    """A class represent of the Epic Event database"""

    def __init__(
        self,
        db_user: str,
        db_password: str,
        db_host: str,
        db_port: str,
        db_name: str,
        db_schema: str,
    ):
        """Constructor of the database Class

        Arguments:
            db_user -- str: the database user
            db_password -- str: the database password
            db_host -- str: the database host
            db_port -- str: the database port
            db_name -- str: the database name
            db_schema -- str: the schema name
        """
        self.user = db_user
        self.password = db_password
        self.host = db_host
        self.port = db_port
        self.name = db_name
        self.schema = db_schema
        self.url = f"postgresql+psycopg2://{self.user}:"\
            f"{self.password}@{self.host}:{self.port}/{self.name}"
        self.engine = create_engine(
            self.url, connect_args={"options": f"-csearch_path={self.schema}"}
        )
        self.session = sessionmaker(bind=self.engine)

    def connexion(self) -> bool:
        """Method to connect to database

        Returns:
            bool
        """
        try:
            connect = self.engine.connect()
            print("Connexion à la base de donnée réussie.")
            return connect
        except Exception:
            print("La connexion à la base de donnée a échouée.")
            return None

    def deconnexion(self) -> bool:
        """Method to deconnect from the database

        Returns:
            bool
        """
        try:
            deconnexion = self.engine.dispose()
            print("Déconnexion de la base de donnée réussie.")
            return deconnexion
        except Exception:
            print("La déconnexion de la base de donnée a échouée.")
            return None

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)
        print("Les tables ont bien été crées")

    def drop_all_tables(self):
        Base.metadata.drop_all(self.engine)
        print("Les tables ont bien été supprimées")

    def get_session(self):
        return self.session

    def __repr__(self) -> str:
        return self.name
