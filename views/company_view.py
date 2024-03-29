import tableprint as tp


class CompanyView:
    """A class representing the view for a class Company"""

    def display_all_companies(self, companies: list) -> None:
        header = tp.header(["Name Company", "Clients"], 30)
        bottom = tp.bottom(2, 30)

        print(header)
        for company in companies:
            for i in range(0, len(company.client)):
                print(tp.row([company.name_company,
                              company.client[i].name_client], 30)) if i == 0 else \
                    print(tp.row(["", company.client[i].name_client], 30))   
        print(bottom)      

    def display_company(self, company: object) -> None:

        header = tp.header(["Name Company", "Clients"], 30)
        bottom = tp.bottom(2, 30)

        print(header)
        for i in range(0, len(company.client)):
            print(tp.row([company.name_company, company.client[i].name_client], 30)) if i == 0 else \
                print(tp.row(["", company.client[i].name_client], 30))   
        print(bottom)         

    @staticmethod
    def create_company_success() -> None:
        """Method to display a success message after the creation
        of a company.
        """
        print("L'entreprise a été ajouté avec succés.")

    @staticmethod
    def create_company_failed() -> None:
        """Method to display a failed message after tried
        to create a company.
        """
        print("L'entreprise n'a pas pu été ajouté.")

    @staticmethod
    def company_not_exist() -> None:
        """Method to display a message that is none company
        of this id in database.
        """
        print("L'entreprise n'existe pas.")

    @staticmethod
    def none_companies() -> None:
        """Method to display a message that is none companies
        actually in database.
        """
        print("Aucunes entreprises en base de donnée")

    @staticmethod
    def update_company_name_success() -> None:
        """Method to display a success message after
        the update of a company.
        """
        print("L'entreprise a bien été mis à jour.")

    @staticmethod
    def update_company_name_failed() -> None:
        """Method to display a failed message after tried
        to update a company.
        """
        print("L'entreprise n'a pas pu être mis à jour.")

    @staticmethod
    def delete_company_success() -> None:
        """Method to display a success message after
        the creation of a company.
        """
        print("L'entreprise a bien été supprimé.")

    @staticmethod
    def delete_company_failed() -> None:
        """Method to display a failed message after
        tried to create a company.
        """
        print("L'entreprise n'a pas pu être supprimé.")
