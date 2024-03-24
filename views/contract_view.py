class ContractView:
    """A class representing the view for a class Contract"""

    def display_all_contracts(self, contracts: list) -> None:
        """Method to diplay all contracts

        Arguments:
            contracts -- list: contracts
        """
        print(contracts)

    def display_contract(self, contract: object) -> None:
        """Method to display one contract.

        Arguments:
            contract -- object: contract
        """
        print(contract)

    @staticmethod
    def update_success() -> None:
        """Method to display a success message after
        the update of a contract.
        """
        print("Le contrat a bien été mis à jour.")

    @staticmethod
    def update_failed() -> None:
        """Method to display a failed message after tried
        to update a contract.
        """
        print("Le contrat n'a pas pu être mis à jour.")

    @staticmethod
    def create_contract_success() -> None:
        """Method to display a success message after the creation
        of a contract.
        """
        print("Le contract a été crée avec succés.")

    @staticmethod
    def create_contract_failed() -> None:
        """Method to display a failed message after tried
        to create a contract.
        """
        print("Le contract n'a pas pu être crée.")

    @staticmethod
    def contract_not_exist() -> None:
        """Method to display a message that is none contract
        of this id in database.
        """
        print("Le contrat n'existe pas.")

    @staticmethod
    def none_contracts() -> None:
        """Method to display a message that is none contracts
        actually in database.
        """
        print("Aucuns contrat en base de donnée")

    @staticmethod
    def delete_client_success() -> None:
        """Method to display a success message after
        the creation of a contract.
        """
        print("Le client a bien été supprimé.")

    @staticmethod
    def delete_client_failed() -> None:
        """Method to display a failed message after
        tried to create a contract.
        """
        print("Le client n'a pas pu être supprimé.")
