from dao.client_dao import ClientDao
from views.client_view import ClientView
from models.user import User
from models.permissions import Permission

class ClientController:
    """A class representing the client controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = ClientDao()
        self.view = ClientView()
        self.user = User.load_user()
        self.permission = Permission(self.user)

    def create_client(self, name: str, contact: str, email: str, company_id: int):
        if not self.permission.isCommercialDepartment():
            return self.view.not_permission_client()
        commercial_id = self.user.id
        client = self.dao.create_client(name, contact, email, company_id, commercial_id)
        if client:
            self.view.create_client_success()
        else:
            self.view.create_client_failed()

    def get_client_by_id(self, id) -> object:
        """Method to get client by id

        Returns:
            object: client object
        """

        client = self.dao.select_client_by_id(id)
        if client:
            return self.view.display_client(client)
        else:
            return self.view.client_not_exist

    def get_all_clients(self) -> list:
        """Method to get all clients by id

        Returns:
            list: list of clients
        """

        clients = self.dao.select_all_clients()
        if clients:
            return self.view.display_all_clients(clients)
        else:
            return self.view.none_clients

    def update_client_name_by_id(self, id: int, new_name: str):
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()       
        client = self.dao.update_name_client_by_id(id, new_name)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_phone_client_by_id(self, id: int, new_phone: str):
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_phone_client_by_id(id, new_phone)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_email_client_by_id(self, id: int, new_email: str):
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_email_client_by_id(id, new_email)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_company_client_by_id(self, id: int, id_company: str):
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_company_client_by_id(id, id_company)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_commercial_client_by_id(self, id: int, id_commercial: str):
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_commercial_client_by_id(id, id_commercial)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def delete_client_by_id(self, id_client: int) -> any:
        """Method to delete a client

        Arguments:
            id_client -- int: the client id to delete

        Returns:
            any
        """
        client = self.dao.select_client_by_id(id_client)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        if self.dao.delete_client_by_id(id_client):
            return self.view.delete_client_success()
        else:
            return self.view.delete_client_failed()
