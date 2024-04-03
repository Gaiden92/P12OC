import click

from dao.contract_dao import ContractDao
from dao.client_dao import ClientDao
from views.contract_view import ContractView
from models.permissions import Permission
from models.user import User


class ContractController:
    """A class representing the contract controller"""

    def __init__(self) -> None:
        """Constructs all necessary attributes of the controller class"""
        self.dao = ContractDao()
        self.view = ContractView()
        self.client_dao = ClientDao()
        self.user = User.load_user()
        self.permission = Permission(self.user)

    def create_contract(
        self, client_id: int, total_amount: float, remaining_amount: float
    ) -> None:
        """Method to control a contract creation

        Arguments:
            client_id -- int: the client id
            total_amount -- float: the total amount
            remaining_amount -- float: the remaining amount

        Returns:
            None
        """

        if not self.permission.isGestionDepartment():
            return self.view.not_permission_contract()
        total_amount = total_amount
        remaining_amount = remaining_amount
        contract = self.dao.create_contract(client_id,
                                            total_amount,
                                            remaining_amount)
        if contract:
            self.view.create_contract_success()
        else:
            self.view.create_contract_failed()

    def get_contract_by_id(self, id: int) -> None:
        """Method to control to get contract by id

        Returns:
            None
        """
        contract = self.dao.select_contract_by_id(id)
        if contract:
            return self.view.display_contract(contract)
        else:
            return self.view.contract_not_exist()

    def get_all_contracts(self) -> None:
        """Method to control to get all contracts by id

        Returns:
            list: list of contracts
        """
        contracts = self.dao.select_all_contracts()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def filter_contracts_by_remaining_amount_desc(self) -> None:
        """Method to control the contracts by
        remaining amount descendant filter

        Returns:
            None
        """
        contracts = self.dao.filter_contracts_by_remaining_amount_desc()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def filter_contracts_by_total_amount_desc(self) -> None:
        """Method to control the contracts by
        total amount descendant filter

        Returns:
            None
        """
        contracts = self.dao.filter_contracts_by_total_amount_desc()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def filter_contracts_by_status(self) -> None:
        """Method to control the contracts by
        status filter

        Returns:
            None
        """
        contracts = self.dao.filter_contracts_by_status()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def update_remaining_amount_by_id(
        self, id: int, new_remaining_amount: float
    ) -> None:
        """Method to control the update remaining amount

        Arguments:
            id -- int: contract id
            new_remaining_amount -- float: the new remaining amount

        Returns:
            None
        """
        contract = self.dao.select_contract_by_id(id)
        if (
            not self.permission.isCommercialOfContract(contract)
            and not self.permission.isGestionDepartment()
        ):
            return self.view.not_permission_contract()

        contract = self.dao.update_remaining_amount_by_id(id,
                                                          new_remaining_amount)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def update_total_amount_by_id(self,
                                  id: int,
                                  new_total_amount: float) -> None:
        """Method to control the update total amount

        Arguments:
            id -- int: contract id
            new_remaining_amount -- float: the new remaining amount

        Returns:
            None
        """
        contract = self.dao.select_contract_by_id(id)
        if (
            not self.permission.isCommercialOfContract(contract)
            and not self.permission.isGestionDepartment()
        ):
            return self.view.not_permission_contract()
        contract = self.dao.update_total_amount_by_id(id, new_total_amount)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def update_status_by_id(self, id: int, status: str) -> None:
        """Method to control the update total amount

        Arguments:
            id -- int: contract id
            status -- str: open or close

        Returns:
            None
        """
        contract = self.dao.select_contract_by_id(id)

        if (
            not self.permission.isCommercialOfContract(contract)
            and not self.permission.isGestionDepartment()
        ):
            return self.view.not_permission_contract()
        match status:
            case "open":
                status = True
            case "close":
                status = False
        contract = self.dao.update_status_contract(id, status)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def update_client_contract_by_id(self, id: int, id_client: int) -> None:
        """Method to control the update total amount

        Arguments:
            id -- int: contract id
            id_client -- int: the client id

        Returns:
            None
        """

        contract = self.dao.select_contract_by_id(id)
        if (
           not self. permission.isCommercialOfContract(contract)
            and not self.permission.isGestionDepartment()
        ):
            return self.view.not_permission_contract()
        contract = self.dao.update_client_contract_by_id(id, id_client)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def is_client_valid(self,
                        ctx: object,
                        param: object,
                        id_client: int) -> int:
        """Method to control the client id validity

        Arguments:
            ctx -- object: the context
            param -- object: the parameters
            id_client -- int: the client id

        Raises:
            click.BadParameter: Exception raise if the email is not valid

        Returns:
            int
        """
        all_clients = self.client_dao.select_all_clients()
        all_clients_ids = [client.id for client in all_clients]
        if id_client not in all_clients_ids:
            raise click.BadParameter("This client does not exist.")
        else:
            return id_client
