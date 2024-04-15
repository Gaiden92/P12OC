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
            print(tp.row(["Name commercial",
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
        print(tp.row(["Name commercial",
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
        print("Success update contract.")

    @staticmethod
    def update_failed() -> None:
        """Method to display a failed message after tried
        to update a contract.
        """
        print("Failed update contract.")

    @staticmethod
    def create_contract_success() -> None:
        """Method to display a success message after the creation
        of a contract.
        """
        print("Success creation contract.")

    @staticmethod
    def create_contract_failed() -> None:
        """Method to display a failed message after tried
        to create a contract.
        """
        print("Failed creation contract.")

    @staticmethod
    def contract_not_exist() -> None:
        """Method to display a message that is none contract
        of this id in database.
        """
        print("This contract doesn't exist.")

    @staticmethod
    def none_contracts() -> None:
        """Method to display a message that is none contracts
        actually in database.
        """
        print("None contracts in database.")

    @staticmethod
    def delete_client_success() -> None:
        """Method to display a success message after
        delete a client of a contract.
        """
        print("Success delete client contract.")

    @staticmethod
    def delete_client_failed() -> None:
        """Method to display a failed message after
        tried to delete  a client contract.
        """
        print("Failed delete client contract.")

    @staticmethod
    def not_permission_contract() -> None:
        """Method to display a message that the user
        has not the permission to add or update a contract.
        """
        print("You don't have the permission to \
              add or update a contrat.")

    @staticmethod
    def not_permission_commercial_contract() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("You can perform this action cause youre not \
              the contract commercial.")
