import tableprint as tp


class ContractView:
    """A class representing the view for a class Contract"""

    def display_all_contracts(self, contracts: list) -> None:
        """Method to diplay all contracts

        Arguments:
            contracts -- list: contracts
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers, [30, 30]))
        for contract in contracts:
            print(tp.row(["Name client",
                          contract.client.commercial.name_collaborator
                          ], [30, 30]))
            print(tp.row(["Name client",
                          contract.client.name_client
                          ], [30, 30]))
            print(tp.row(["Total amount",
                          str(contract.total_amount)+"€"
                          ], [30, 30]))
            print(tp.row(["Remaining amount",
                          str(contract.remaining_amount)+"€"
                          ], [30, 30]))
            print(tp.row(["Create date",
                          str(contract.creation_date)
                          ], [30, 30]))
            print(tp.row(["Status",
                          "Open" if contract.status == 1 else "Close"
                          ], [30, 30]))
            print("-"*67)
        print(tp.bottom(2, [30, 30]))

    def display_contract(self, contract: object) -> None:
        """Method to display one contract.

        Arguments:
            contract -- object: contract
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers, [30, 30]))
        print(tp.row(["Name client",
                      contract.client.commercial.name_collaborator
                      ], [30, 30]))
        print(tp.row(["Name client",
                      contract.client.name_client
                      ], [30, 30]))
        print(tp.row(["Total amount",
                      str(contract.total_amount)+"€"
                      ], [30, 30]))
        print(tp.row(["Remaining amount",
                      str(contract.remaining_amount)+"€"
                      ], [30, 30]))
        print(tp.row(["Create date",
                      str(contract.creation_date)
                      ], [30, 30]))
        print(tp.row(["Status",
                      "Open" if contract.status == 1 else "Close"
                      ], [30, 30]))
        print(tp.bottom(2, [30, 30]))

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

    @staticmethod
    def not_permission_contract() -> None:
        """Method to display a message that the user
        has not the permission to add or update a contract.
        """
        print("Vous n'avez pas les droits nécessaire \
              pour ajouter ou modifier un contrat.")

    @staticmethod
    def not_permission_commercial_contract() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("Vous n'êtes pas le commercial du contrat.")
