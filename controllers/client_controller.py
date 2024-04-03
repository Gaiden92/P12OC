import click

from config.parameters import COMMERCIAL
from dao.client_dao import ClientDao
from dao.company_dao import CompanyDao
from dao.collaborator_dao import CollaboratorDao
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
        self.company_dao = CompanyDao()
        self.collaborator_dao = CollaboratorDao()
        self.user = User.load_user()
        self.permission = Permission(self.user)

    def create_client(self,
                      name: str,
                      contact: str,
                      email: str,
                      company_id: int) -> None:
        """Method to control the client creation

        Arguments:
            name -- str: name client
            contact -- str: phone client
            email -- str: email client
            company_id -- int: company id

        Returns:
            None
        """

        if not self.permission.isCommercialDepartment():
            return self.view.not_permission_client()
        commercial_id = self.user.id
        client = self.dao.create_client(name,
                                        contact,
                                        email,
                                        company_id,
                                        commercial_id)
        if client:
            self.view.create_client_success()
        else:
            self.view.create_client_failed()

    def get_client_by_id(self, id) -> None:
        """Method to get client by id

        Returns:
            None
        """

        client = self.dao.select_client_by_id(id)
        if client:
            return self.view.display_client(client)
        else:
            return self.view.client_not_exist

    def get_all_clients(self) -> None:
        """Method to get all clients by id

        Returns:
            None
        """

        clients = self.dao.select_all_clients()
        if clients:
            return self.view.display_all_clients(clients)
        else:
            return self.view.none_clients

    def update_client_name_by_id(self, id: int, new_name: str) -> None:
        """Method to control the client name update

        Arguments:
            id -- int: client id
            new_name -- str: client new name

        Returns:
            None
        """
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_name_client_by_id(id, new_name)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_phone_client_by_id(self, id: int, new_phone: str) -> None:
        """Method to control the client phone update

        Arguments:
            id -- int: client id
            new_phone -- str: client new phone

        Returns:
            None
        """
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_phone_client_by_id(id, new_phone)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_email_client_by_id(self, id: int, new_email: str) -> None:
        """Method to control the client email update

        Arguments:
            id -- int: client id
            new_email -- str: client new email

        Returns:
            None
        """
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        if not self.is_email_valid(new_email):
            return self.view.email_invalid()
        client = self.dao.update_email_client_by_id(id, new_email)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def update_commercial_client_by_id(self,
                                       id: int,
                                       id_commercial: int) -> None:
        """Method to control the client commercial update

        Arguments:
            id -- int: client id
            id_commercial -- str: client id commercial

        Returns:
            None
        """
        client = self.dao.select_client_by_id(id)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        client = self.dao.update_commercial_client_by_id(id, id_commercial)
        if client:
            self.view.update_client_success()
        else:
            self.view.update_client_failed()

    def delete_client_by_id(self, id_client: int) -> None:
        """Method to delete a client

        Arguments:
            id_client -- int: the client id to delete

        Returns:
            None
        """
        client = self.dao.select_client_by_id(id_client)
        if not self.permission.isCommercialOfClient(client):
            return self.view.not_permission_commercial_client()
        if self.dao.delete_client_by_id(id_client):
            return self.view.delete_client_success()
        else:
            return self.view.delete_client_failed()

    def is_email_valid(self, ctx: object, param: object, email: str) -> str:
        """Method to control if an email is valid

        Arguments:
            ctx -- object: the context
            param -- object: the parameters
            email -- str: the email client

        Raises:
            click.BadParameter: _description_

        Returns:
            _description_
        """
        if "@" not in email or (".fr" not in email and ".com" not in email):
            raise click.BadParameter(
                'This email is not valid. Please Try again.')
        else:
            return email

    def is_phone_valid(self, ctx: object, param: object, phone: str) -> str:
        """Method to control if a phone number is valid

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            phone -- str: the phone client

        Raises:
            click.BadParameter: Exception: phone must have number only
            click.BadParameter: Exception: phone must have 10 numbers

        Returns:
            str: the phone
        """
        if not all(number.isdigit() for number in phone):
            raise click.BadParameter(
                "Le téléphone doit contenir que des chiffres.")
        if not len(phone) == 10:
            raise click.BadParameter(
                "Le téléphone doit contenir 10 chiffres.")
        else:
            return phone

    def is_company_valid(self,
                         ctx: object,
                         param: object,
                         id_company: int) -> int:
        """Method to control if the company id exist

        Arguments:
            ctx -- object: the context
            param -- object: the param
            id_company -- int: the company id

        Raises:
            click.BadParameter: Exception: The company didn't exist

        Returns:
            int: id company
        """
        companies = self.company_dao.select_all_companies()
        all_companies_ids = [company.id for company in companies]
        if id_company not in all_companies_ids:
            raise click.BadParameter("This company id doesn't exist.")
        else:
            return id_company

    def is_commercial_valid(self,
                            ctx: object,
                            param: object,
                            id_commercial: int) -> int:
        """Method to control if the commercial id exist

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            id_commercial -- int: the commercial id

        Raises:
            click.BadParameter: Exception: the commercial id didn't exist

        Returns:
            int: the commercial id
        """
        commercials = self.collaborator_dao.select_all_collaborators()
        all_commercial_ids = [
            commercial.department.name_department == COMMERCIAL
            for commercial in commercials]
        if id_commercial not in all_commercial_ids:
            raise click.BadParameter("This commercial id doesn't exist.")
        else:
            return id_commercial
