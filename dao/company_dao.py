from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from models.company import Company
from config.parameters import DB


class CompanyDao:
    """A class represents the company table"""

    def __init__(self) -> None:
        """Constructor of CompanyDao class

        Arguments:
            Session -- object: an session object
        """
        self.db = DB
        self.session = self.db.session()
        self.query = self.session.query(Company)

    def select_all_companies(self) -> list:
        """A method for select all companies in database

        Returns:
            None or list of Company object:
        """
        companies = self.query.all()
        if companies:
            return companies
        else:
            None

    def select_company_by_id(self, company_id: int) -> object:
        """Method to get company by id

        Arguments:
            company_search -- id: id of a company

        Returns:
            object or None
        """
        company = self.query.filter(Company.id == company_id).first()
        if company:
            return company
        else:
            return None

    def select_company_by_name(self, company_search: str) -> object:
        """Method to get company by name

        Arguments:
            company_search -- str: name of a company

        Returns:
            object or None
        """
        company = self.query.filter(Company.name_company == company_search).first()
        if company:
            return company
        else:
            return None

    def create_company(self, name: str) -> bool:
        """Method to insert new company in database.

        Arguments:
            name -- str: the name of the new company to add.

        Returns:
            bool
        """
        company = Company(name_company=name)
        try:
            self.session.add(company)
            self.session.commit()
        except Exception as ex:
            return False
        return True

    def update_name_company_by_id(self, id_company: int, new_name: str) -> bool:
        """Method to update a company by his id.

        Arguments:
            id_company -- int: the id of the company to update
            new_name -- str: the new name of the company

        Returns:
            bool
        """
        company_to_update = self.query.get(id_company)
        if company_to_update:
            company_to_update.name_company = new_name
            self.session.commit()
            return True
        else:
            return False

    def delete_company_by_id(self, id_company: int) -> bool:
        """Method to delete a company by his id

        Arguments:
            id_company -- int: id company

        Returns:
            bool
        """
        company_to_delete = self.query.filter(Company.id == id_company)
        if company_to_delete.delete():
            try:
                self.session.commit()
                return True
            except IntegrityError:
                return False
        else:
            return False
