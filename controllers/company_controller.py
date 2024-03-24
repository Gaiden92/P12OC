from dao.company_dao import CompanyDao
from views.company_view import CompanyView


class CompanyController:
    """A class representing the company controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = CompanyDao()
        self.view = CompanyView()

    def create_company(self, name: str):

        company = self.dao.create_company(name)
        if company:
            self.view.create_company_success()
        else:
            self.view.create_company_failed()

    def get_company_by_id(self, id: int) -> object:
        """Method to get company by id

        Returns:
            object: company object
        """

        company = self.dao.select_company_by_id(id)
        if company:
            return self.view.display_company(company)
        else:
            return self.view.company_not_exist()

    def get_all_companies(self) -> list:
        """Method to get all companies by id

        Returns:
            list: list of companies
        """

        companies = self.dao.select_all_companies()
        if companies:
            return self.view.display_all_companies(companies)
        else:
            return self.view.none_companies

    def update_company_name_by_id(self, id: int, new_name: str) -> None:
        """Method to update a company name by his id.

        Arguments:
            id -- int: id company
            new_name -- str: name company
        """
        company = self.dao.update_name_company_by_id(id, new_name)
        if company:
            self.view.update_company_name_success()
        else:
            self.view.update_company_name_failed()

    def delete_company_by_id(self, id_company: int) -> any:
        """Method to delete a company

        Arguments:
            id_company -- int: the company id to delete

        Returns:
            any
        """
        company = self.dao.delete_company_by_id(id_company)
        if company:
            return self.view.delete_company_success()
        else:
            return self.view.delete_company_failed()
