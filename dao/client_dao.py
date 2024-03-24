from datetime import datetime
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from models.client import Client
from config.parameters import DB


class ClientDao:
    """A class represents the client table"""

    def __init__(self) -> None:
        """Constructor of ClientDao class

        Arguments:
            Session -- object: an session object
        """
        self.db = DB
        self.session = self.db.session()
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

    def select_client_by_id(self, client_search: int) -> object:
        """Method to get a client by id

        Arguments:
            client_search -- int: id of a client

        Returns:
            object or None
        """
        client = self.query.filter(Client.id == client_search).first()
        if client:
            return client
        else:
            return None

    def select_client_by_name(self, client_search: str) -> object:
        """Method to get client by name

        Arguments:
            client_search -- str: name of a client

        Returns:
            object or None
        """
        client = self.query.filter(Client.name_client == client_search).first()
        if client:
            return client
        else:
            return None

    def create_client(
        self, name: str, phone: str, email: str, company_id: int, commercial_id: int
    ) -> bool:
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
            company_id=company_id,
            commercial_id=commercial_id,
        )

        try:
            self.session.add(client)
            self.session.commit()
        except Exception as ex:
            return False
        return True

    def update_name_client_by_id(self, id_client: int, new_name: str) -> bool:
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
            client_to_update.update_date = datetime.now()
            self.session.commit()
            return True
        else:
            return False

    def update_phone_client_by_id(self, id_client: int, new_phone: str) -> bool:
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
            client_to_update.update_date = datetime.now()
            self.session.commit()
            return True
        else:
            return False

    def update_email_client_by_id(self, id_client: int, new_email: str) -> bool:
        """Method to update a email client by his id.

        Arguments:
            id_client -- int: the id of the client to update
            new_email -- str: the new email of the client

        Returns:
            bool
        """
        client_to_update = self.query.get(id_client)
        if client_to_update:
            client_to_update.email = new_email
            client_to_update.update_date = datetime.now()
            self.session.commit()
            return True
        else:
            return False

    def update_company_client_by_id(self, id_client: int, id_new_company: int) -> bool:
        """Method to update a company client by his id.

        Arguments:
            id_client -- int: the id of the client to update
            id_new_company -- int: the new company of the client

        Returns:
            bool
        """
        client_to_update = self.query.get(id_client)
        if client_to_update:
            client_to_update.company_id = id_new_company
            client_to_update.update_date = datetime.now()
            self.session.commit()
            return True
        else:
            return False

    def update_commercial_client_by_id(
        self, id_client: int, id_new_commercial: int
    ) -> bool:
        """Method to update a commercial client by his id.

        Arguments:
            id_client -- int: the id of the client to update
            id_new_commercial -- int: the new commercial id of the client

        Returns:
            bool
        """
        client_to_update = self.query.get(id_client)
        if client_to_update:
            client_to_update.commercial_id = id_new_commercial
            client_to_update.update_date = datetime.now()
            self.session.commit()
            return True
        else:
            return False

    def delete_client_by_id(self, id_client: int) -> bool:
        client = self.query.filter(Client.id == id_client)
        if client:
            try:
                client.delete()
                self.session.commit()
                return True
            except IntegrityError:
                return False
        else:
            return False
