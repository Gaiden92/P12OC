from dao.collaborator_dao import CollaboratorDao
from views.collaborator_view import CollaboratorView

from models.user import User


class CollaboratorController:
    """A class representing the collaborator controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = CollaboratorDao()
        self.view = CollaboratorView()

    def create_collaborator(
        self, name: str, contact: str, password: str, department_id: int
    ):
        """Method to create a collaborator

        Arguments:
            name -- name collaborator
            contact -- contact collabroator
            password -- str: password collaborator
            department_id -- int: departmend_id
        """

        if self.dao.create_collaborator(name, contact, password, department_id):
            self.view.create_collaborator_success()
        else:
            self.view.create_collaborator_failed()

    def get_collaborator_by_id(self, id) -> object:
        """Method to get collaborator by id

        Returns:
            object: Collaborator object
        """

        collaborator = self.dao.select_collaborator_by_id(id)
        if collaborator:
            return self.view.display_collaborator(collaborator)
        else:
            return self.view.collaborator_not_exist()

    def get_all_collaborators(self) -> list:
        """Method to get all collaborators by id

        Returns:
            list: list of collaborators
        """

        collaborators = self.dao.select_all_collaborators()
        if collaborators:
            return self.view.display_all_collaborators(collaborators)
        else:
            return self.view.none_collaborators()

    def update_collaborator_name_by_id(self, id: int, new_name: str) -> any:
        """Method to update a collaborator by his id

        Arguments:
            id -- int: collaborator id
            new_name -- str: collaborator new name

        Returns:
            view
        """
        collaborator = self.dao.update_name_collaborator_by_id(id, new_name)
        if collaborator:
            return self.view.update_collaborator_name_success()
        else:
            return self.view.update_collaborator_name_failed()

    def check_login(self, id: int, password: str):

        collaborator = self.dao.select_collaborator_by_id(id)
        if collaborator.check_password(password):
            current_user = User(id, collaborator.department_id)
            token = current_user.generate_token()
            current_user.register_info()
            return self.view.login_success(token)
        else:
            return self.view.login_failed()

    def verify_informations(self, name, contact, password, department_id):
        return self.dao.create_collaborator(name, contact, password, department_id)

    def delete_collaborator_by_id(self, id_collaborator: int) -> any:
        collaborator = self.dao.delete_collaborator_by_id(id_collaborator)
        if collaborator:
            return self.view.delete_collaborator_success()
        else:
            return self.view.delete_collaborator_failed()
