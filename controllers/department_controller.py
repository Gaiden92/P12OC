from dao.department_dao import DepartmentDao
from views.department_view import DepartmentView
from models.permissions import Permission
from models.user import User


class DepartmentController:
    """A class representing the department controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        """
        self.dao = DepartmentDao()
        self.view = DepartmentView()
        self.permission = Permission(User.load_user())

    def create_department(self, department_name: str) -> None:
        """Method to create new department

        Returns:
            None
        """
        department = self.dao.create_department(department_name)
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        if department:
            return self.view.create_department_success()
        else:
            return self.view.create_department_failed()

    def get_department_by_id(self, id) -> None:
        """Method to get department by id

        Returns:
            None
        """

        department = self.dao.select_department_by_id(id)
        if department:
            return self.view.display_department(department)
        else:
            return self.view.department_not_exist()

    def get_all_departments(self) -> None:
        """Method to get all departments by id

        Returns:
            None
        """

        departments = self.dao.select_all_departments()
        if departments:
            return self.view.display_all_departments(departments)
        else:
            return self.view.none_departments()

    def update_department_name_by_id(self, id: int, new_name: str) -> None:
        """Method to get update name department by id

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        department = self.dao.update_name_department_by_id(id, new_name)
        if department:
            return self.view.update_success()
        else:
            return self.view.update_failed()

    def delete_department_by_id(self, id_department: int) -> None:
        """Method to delete a department

        Arguments:
            id_department -- int: the department id to delete

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        department = self.dao.delete_department_by_id(id_department)
        if department:
            return self.view.delete_department_success()
        else:
            return self.view.delete_department_failed()
