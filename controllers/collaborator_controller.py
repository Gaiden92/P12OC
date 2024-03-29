import click

from dao.collaborator_dao import CollaboratorDao
from dao.department_dao import DepartmentDao
from views.collaborator_view import CollaboratorView
from models.permissions import Permission
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
        self.department_dao = DepartmentDao()


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
        user = User.load_user()
        permission = Permission(user)
        if not permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
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
        user = User.load_user()
        permission = Permission(user)
        if not permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        collaborator = self.dao.update_name_collaborator_by_id(id, new_name)
        if collaborator:
            return self.view.update_collaborator_success()
        else:
            return self.view.update_collaborator_failed()

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
        user = User.load_user()
        permission = Permission(user)
        if not permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        collaborator = self.dao.delete_collaborator_by_id(id_collaborator)
        if collaborator:
            return self.view.delete_collaborator_success()
        else:
            return self.view.delete_collaborator_failed()

    def is_phone_valid(self, ctx, param, phone: str) -> str:
        if not all(number.isdigit() for number in phone):
            raise click.BadParameter("Le téléphone doit contenir que des chiffres.")
        if not len(phone) == 10:
            raise click.BadParameter("Le téléphone doit contenir 10 chiffres.")
        else:
            return phone
        
    def is_department_valid(self, ctx, param, departmend_id: int) -> int:
        all_departments = self.department_dao.select_all_departments()
        all_departments_ids = [department.id for department in all_departments]
        if not departmend_id in all_departments_ids:
            raise click.BadParameter("Ce département n'existe pas.")
        else:
            return departmend_id