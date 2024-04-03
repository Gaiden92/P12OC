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

        """
        self.dao = CollaboratorDao()
        self.view = CollaboratorView()
        self.department_dao = DepartmentDao()
        self.user = User.load_user()
        self.permission = Permission(self.user)

    def create_collaborator(
        self, name: str, contact: str, password: str, department_id: int
    ) -> None:
        """Method to control the collaborator creation

        Arguments:
            name -- name collaborator
            contact -- contact collabroator
            password -- str: password collaborator
            department_id -- int: departmend_id
        Returns:
        None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        if self.dao.create_collaborator(name,
                                        contact,
                                        password,
                                        department_id):
            self.view.create_collaborator_success()
        else:
            self.view.create_collaborator_failed()

    def get_collaborator_by_id(self, id: int) -> None:
        """Method to control the select collaborator by his id

        Returns:
            None
        """

        collaborator = self.dao.select_collaborator_by_id(id)
        if collaborator:
            return self.view.display_collaborator(collaborator)
        else:
            return self.view.collaborator_not_exist()

    def get_all_collaborators(self) -> None:
        """Method to control get all collaborators by id

        Returns:
            None
        """
        collaborators = self.dao.select_all_collaborators()
        if collaborators:
            return self.view.display_all_collaborators(collaborators)
        else:
            return self.view.none_collaborators()

    def update_collaborator_name_by_id(self, id: int, new_name: str) -> None:
        """Method to control the update of a collaborator by his id

        Arguments:
            id -- int: collaborator id
            new_name -- str: collaborator new name

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        collaborator = self.dao.update_name_collaborator_by_id(id, new_name)
        if collaborator:
            return self.view.update_collaborator_success()
        else:
            return self.view.update_collaborator_failed()

    def update_collaborator_contact_by_id(self,
                                          id: int,
                                          new_contact: str) -> None:
        """Method to contorl the update of a collaborator by his id

        Arguments:
            id -- int: collaborator id
            new_contact -- str: collaborator new contact

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        collaborator = self.dao.update_contact_collaborator_by_id(id,
                                                                  new_contact)
        if collaborator:
            return self.view.update_collaborator_success()
        else:
            return self.view.update_collaborator_failed()

    def check_login(self, id: int, password: str) -> None:
        """Method to control the login

        Arguments:
            id -- int: id of the collaborator
            password -- str: password of the collaborator

        Returns:
            None
        """
        collaborator = self.dao.select_collaborator_by_id(id)
        if collaborator.check_password(password):
            current_user = User(id, collaborator.department_id)
            token = current_user.generate_token()
            current_user.register_info()
            return self.view.login_success(token)
        else:
            return self.view.login_failed()

    def delete_collaborator_by_id(self, id_collaborator: int) -> None:
        """Method to control the collaborator suppresion

        Arguments:
            id_collaborator -- int: id of the collaborator

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission_collaborator()
        collaborator = self.dao.delete_collaborator_by_id(id_collaborator)
        if collaborator:
            return self.view.delete_collaborator_success()
        else:
            return self.view.delete_collaborator_failed()

    def is_phone_valid(self, ctx: object, param: object, phone: str) -> str:
        """Method to control if a phone number is valid

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            phone -- str: the phone collaborator

        Raises:
            click.BadParameter: Exception: phone must have number only
            click.BadParameter: Exception: phone must have 10 numbers

        Returns:
            str: the phone
        """
        if not all(number.isdigit() for number in phone):
            raise click.BadParameter("Phone must contains only numbers.")
        if not len(phone) == 10:
            raise click.BadParameter("Phone must have 10 numbers.")
        else:
            return phone

    def is_department_valid(self,
                            ctx: object,
                            param: object,
                            departmend_id: int) -> int:
        """Method to control if a department id is valid

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            departmend_id -- int: the department id

        Raises:
            click.BadParameter: Exception: id is not exist

        Returns:
            int: department id
        """
        all_departments = self.department_dao.select_all_departments()
        all_departments_ids = [department.id for department in all_departments]
        if departmend_id not in all_departments_ids:
            raise click.BadParameter("Ce département n'existe pas.")
        else:
            return departmend_id
