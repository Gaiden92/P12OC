from dao.department_dao import DepartmentDao
from views.department_view import DepartmentView
from .user_controller import UserController
from models.permissions import Permission
from models.user import User

class DepartmentController:
    """A class representing the department controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = DepartmentDao()
        self.view = DepartmentView()

    def create_department(self, department_name: str):
        """Method to create new department

        Returns:
            department_name -- str: department name
        """
        department = self.dao.create_department(department_name)

        if department:
            return self.view.create_department_success()
        else:
            return self.view.create_department_failed()

    def get_department_by_id(self, id) -> object:
        """Method to get department by id

        Returns:
            object: department object
        """

        department = self.dao.select_department_by_id(id)
        if department:
            return self.view.display_department(department)
        else:
            return self.view.department_not_exist()

    def get_all_departments(self) -> list:
        """Method to get all departments by id

        Returns:
            list: list of departments
        """

        departments = self.dao.select_all_departments()
        if departments:
            return self.view.display_all_departments(departments)
        else:
            return self.view.none_departments()

    def update_department_name_by_id(self, id: int, new_name: str) -> object:
        """Method to get update name department by id

        Returns:
            department -- object: Department
        """

        department = self.dao.update_name_department_by_id(id, new_name)
        if department:
            return self.view.update_success()
        else:
            return self.view.update_failed()

    def delete_department_by_id(self, id_department: int) -> any:
        """Method to delete a department

        Arguments:
            id_department -- int: the department id to delete

        Returns:
            any
        """
        department = self.dao.delete_department_by_id(id_department)
        if department:
            return self.view.delete_department_success()
        else:
            return self.view.delete_department_failed()
