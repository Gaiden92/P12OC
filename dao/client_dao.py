from sqlalchemy import select
from models.client import Client
from datetime import datetime

class ClientDao:
    """A class represents the client table
    """
    def __init__(self, Session:object) -> None:
        """Constructor of ClientDao class

        Arguments:
            Session -- object: an session object
        """
        self.session = Session()
        self.query = self.session.query(Client)

    def select_all_clients(self) -> list:
        """A method for select all clients in database 

        Returns:
            None or list of Client object: 
        """
        clients = self.query.all()
        if clients:
            return clients
        else:
            None

    def select_client_by_id(self, client_search:int) -> object:
        """Method to get a client by id

        Arguments:
            client_search -- int: id of a client

        Returns:
            object or None
        """
        client = self.query.filter(Client.id==client_search).first()
        if client:
            return client
        else:
            return None

    def select_client_by_name(self, client_search:str) -> object:
        """Method to get client by name

        Arguments:
            client_search -- str: name of a client

        Returns:
            object or None
        """
        client = self.query.filter(Client.name_client==client_search).first()
        if client:
            return client
        else:
            return None
    
    def create_client(self, name: str, phone:str, email:str, company_id:int) -> bool:
        """Method to insert new client in database.

        Arguments:
            name -- str: the name of the new client to add.

        Returns:
            bool
        """
        client = Client(
            name_client=name,
            email=email,
            phone=phone,
            creation_date=datetime.now(),
            update_date=datetime.now(),
            compagny_id=company_id)

        try:
            self.session.add(client)
            self.session.commit()
        except Exception as ex:
            return False
        return True
    
    def update_name_client_by_id(self, id_client:int, new_name:str) -> bool:
        """Method to update a client by his id.

        Arguments:
            id_client -- int: the id of the client to update
            new_name -- str: the new name of the client 

        Returns:
            bool
        """
        client_to_update = self.query.get(id_client)
        if client_to_update:
            client_to_update.name_client = new_name
            self.session.commit()
            return True
        else:
            return False

    def update_phone_client_by_id(self, id_client:int, new_phone:str) -> bool:
        """Method to update a phone client by his id.

        Arguments:
            id_client -- int: the id of the client to update
            new_phone -- str: the new phone of the client 

        Returns:
            bool
        """
        client_to_update = self.query.get(id_client)
        if client_to_update:
            client_to_update.phone = new_phone
            self.session.commit()
            return True
        else:
            return False