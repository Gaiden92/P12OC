from dao.contract_dao import ContractDao
from views.contract_view import ContractView
from models.permissions import Permission
from models.user import User



class ContractController:
    """A class representing the contract controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = ContractDao()
        self.view = ContractView()


    def create_contract(
        self, client_id: int, total_amount: float, remaining_amount: float
    ):
        user = User.load_user()
        permission = Permission(user)
        if not permission.isGestionDepartment():
            return self.view.not_permission_contract()
        total_amount= total_amount
        remaining_amount = remaining_amount
        contract = self.dao.create_contract(
            client_id, total_amount, remaining_amount
        )
        if contract:
            self.view.create_contract_success()
        else:
            self.view.create_contract_failed()

    def get_contract_by_id(self, id) -> object:
        """Method to get contract by id

        Returns:
            object: contract object
        """
        user = User.load_user()
        permission = Permission(user)
        contract = self.dao.select_contract_by_id(id)
        if contract:
            return self.view.display_contract(contract)
        else:
            return self.view.contract_not_exist

    def get_all_contracts(self) -> list:
        """Method to get all contracts by id

        Returns:
            list: list of contracts
        """
        user = User.load_user()
        permission = Permission(user)
        contracts = self.dao.select_all_contracts()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts

    def filter_contracts_by_remaining_amount_desc(self):
        contracts = self.dao.filter_contracts_by_remaining_amount_desc()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def filter_contracts_by_total_amount_desc(self):
        contracts = self.dao.filter_contracts_by_total_amount_desc()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def filter_contracts_by_status(self):
        contracts = self.dao.filter_contracts_by_status()
        if contracts:
            return self.view.display_all_contracts(contracts)
        else:
            return self.view.none_contracts()

    def update_remaining_amount_by_id(self, id: int, new_remaining_amount: float):
        contract = self.dao.select_contract_by_id(id)
        user = User.load_user()
        permission = Permission(user)
        if not permission.isCommercialOfContract(contract):
            return self.view.not_permission_commercial_contract()
        
        contract = self.dao.update_remaining_amount_by_id(id, new_remaining_amount)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def update_total_amount_by_id(self, id: int, new_total_amount: float):
        contract = self.dao.select_contract_by_id(id)
        user = User.load_user()
        permission = Permission(user)
        if not permission.isCommercialOfContract(contract):
            return self.view.not_permission_commercial_contract()
        contract = self.dao.update_total_amount_by_id(id, new_total_amount)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()

    def update_status_by_id(self, id: int, status: str):
        contract = self.dao.select_contract_by_id(id)
        user = User.load_user()
        permission = Permission(user)
        if not permission.isCommercialOfContract(contract):
            return self.view.not_permission_commercial_contract()
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

    def update_client_contract_by_id(self, id: int, id_client: int):
        user = User.load_user()
        permission = Permission(user)
        contract = self.dao.select_contract_by_id(id)
        if not permission.isCommercialOfContract(contract):
            return self.view.not_permission_commercial_contract()
        contract = self.dao.update_client_contract_by_id(id, id_client)
        if contract:
            self.view.update_success()
        else:
            self.view.update_failed()
