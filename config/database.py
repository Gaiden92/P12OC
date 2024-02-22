from sqlalchemy import create_engine

class Database():
    """A class represent of the Epic Event database
    """
    def __init__(self, db_user:str, db_password:str, db_host:str, db_port:str, db_name:str):
        """Constructor of the database Class

        Arguments:
            db_user -- str: the database user
            db_password -- str: the database password
            db_host -- str: the database host
            db_port -- str: the database port
            db_name -- str: the database name
        """
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name

        self.db_url = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        self.engine = create_engine(self.db_url)

    def connexion(self) -> bool:
        """Method to connect to database

        Returns:
            bool
        """
        try:
            connect = self.engine.connect()
            return connect
        except Exception as ex:
            return None
        
    def deconnexion(self) -> bool:
        """Method to deconnect from the database

        Returns:
            bool
        """
        try:
            deconnexion = self.engine.dispose()
            return deconnexion
        except Exception as ex:
            return None
        