class CompanyView:
    """A class representing the view for a class Company"""

    def display_all_companies(self, companies: list) -> None:
        print(companies)

    def display_company(self, company: object) -> None:
        print(company)

    @staticmethod
    def create_company_success():
        print("L'entreprise a été ajouté avec succés.")

    @staticmethod
    def create_company_failed():
        print("L'entreprise n'a pas pu été ajouté.")

    @staticmethod
    def company_not_exist():
        print("L'entreprise n'existe pas.")

    @staticmethod
    def none_companies():
        print("Aucunes entreprises en base de donnée")

    @staticmethod
    def update_company_name_succes():
        print("L'entreprise a bien été mis à jour.")

    @staticmethod
    def update_company_name_failed():
        print("L'entreprise n'a pas pu être mis à jour.")

    @staticmethod
    def delete_company_success():
        print("L'entreprise a bien été supprimé.")

    @staticmethod
    def delete_company_failed():
        print("L'entreprise n'a pas pu être supprimé.")
