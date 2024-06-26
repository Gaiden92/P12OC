from dao.company_dao import CompanyDao
from views.company_view import CompanyView
from models.permissions import Permission
from models.user import User


class CompanyController:
    """A class representing the company controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        """
        self.dao = CompanyDao()
        self.view = CompanyView()
        self.permission = Permission(User.load_user())

    def create_company(self, name: str) -> None:
        """Method to control the company creation

        Arguments:
            name -- str: name company
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        company = self.dao.create_company(name)
        if company:
            self.view.create_company_success()
        else:
            self.view.create_company_failed()

    def get_company_by_id(self, id: int) -> None:
        """Method to controle the select company

        Returns:
            None
        """
        company = self.dao.select_company_by_id(id)
        if company:
            return self.view.display_company(company)
        else:
            return self.view.company_not_exist()

    def get_all_companies(self) -> None:
        """Method to get all companies by id

        Returns:
            None
        """
        companies = self.dao.select_all_companies()
        if companies:
            return self.view.display_all_companies(companies)
        else:
            return self.view.none_companies

    def update_company_name_by_id(self, id: int, new_name: str) -> None:
        """Method to control the company to update.

        Arguments:
            id -- int: id company
            new_name -- str: name company
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        company = self.dao.update_name_company_by_id(id, new_name)
        if company:
            self.view.update_company_name_success()
        else:
            self.view.update_company_name_failed()

    def delete_company_by_id(self, id_company: int) -> None:
        """Method to control a suppression company

        Arguments:
            id_company -- int: the company id to delete

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        company = self.dao.delete_company_by_id(id_company)
        if company:
            return self.view.delete_company_success()
        else:
            return self.view.delete_company_failed()
