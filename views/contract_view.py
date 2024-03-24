class ContractView:
    """A class representing the view for a class Contract"""

    def display_all_contracts(self, contracts: list) -> None:
        print(contracts)

    def display_contract(self, contract: object) -> None:
        print(contract)

    @staticmethod
    def update_success():
        print("Le contrat a bien été mis à jour.")

    @staticmethod
    def update_failed():
        print("Le contrat n'a pas pu être mis à jour.")

    @staticmethod
    def create_contract_success():
        print("Le contract a été crée avec succés.")

    @staticmethod
    def create_contract_failed():
        print("Le contract n'a pas pu être crée.")

    @staticmethod
    def contract_not_exist():
        print("Le contrat n'existe pas.")

    @staticmethod
    def none_contracts():
        print("Aucuns contrat en base de donnée")

    @staticmethod
    def delete_client_success():
        print("Le client a bien été supprimé.")

    @staticmethod
    def delete_client_failed():
        print("Le client n'a pas pu être supprimé.")
