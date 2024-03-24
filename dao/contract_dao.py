from datetime import datetime
from sqlalchemy import select

from models.contract import Contract
from config.parameters import DB


class ContractDao:
    """A class represents the contract table"""

    def __init__(self) -> None:
        self.db = DB
        self.session = self.db.session()
        self.query = self.session.query(Contract)

    def select_all_contracts(self) -> list:
        """A method for select all contracts in database

        Returns:
            None or list of Contract object:
        """
        contracts = self.query.all()
        if contracts:
            return contracts
        else:
            None

    def select_contract_by_id(self, contract_id: int) -> object:
        """Method to get contract by id

        Arguments:
            contract_search -- id: id of a contract

        Returns:
            object or None
        """
        contract = self.query.filter(Contract.id == contract_id).first()
        if contract:
            return contract
        else:
            return None

    def create_contract(
        self,
        client_id: int,
        total_amount: int,
        remaining_amount: int,
    ) -> bool:
        """Method to insert new contract in database.

        Arguments:
            client_id -- int: the id of the client.
            total_amount -- int: the contract total amount
            remaining_amount -- int: the contract remaining amount
        Returns:
            bool
        """
        contract = Contract(
            client_id=client_id,
            total_amount=total_amount,
            remaining_amount=remaining_amount,
            creation_date=datetime.now(),
        )
        try:
            self.session.add(contract)
            self.session.commit()
        except Exception as ex:
            return False
        return True

    def update_remaining_amount_by_id(
        self, id_contract: int, new_remaining_amount: int
    ) -> bool:
        """Method to update a contract remaining amount by his id.

        Arguments:
            id_contract -- int: the contract id to update
            new_remaining_amount -- int: the new remaining amount of the contract

        Returns:
            bool
        """
        contract_to_update = self.query.get(id_contract)
        if contract_to_update:
            contract_to_update.remaining_amount = new_remaining_amount
            self.session.commit()
            return True
        else:
            return False

    def update_total_amount_by_id(
        self, id_contract: int, new_total_amount: int
    ) -> bool:
        """Method to update a contract total amount by his id.

        Arguments:
            id_contract -- int: the contract id to update
            new_total_amount -- int: the new total amount of the contract

        Returns:
            bool
        """
        contract_to_update = self.query.get(id_contract)
        if contract_to_update:
            contract_to_update.total_amount = new_total_amount
            self.session.commit()
            return True
        else:
            return False

    def update_client_contract_by_id(self, id_contract: int, id_client: int) -> bool:
        """Method to update a contract client by his id.

        Arguments:
            id_contract -- int: the contract id to update
            id__new_client -- int: the new client in charge of the contract

        Returns:
            bool
        """
        contract_to_update = self.query.get(id_contract)
        if contract_to_update:
            contract_to_update.client_id = id_client
            self.session.commit()
            return True
        else:
            return False

    def update_status_contract(self, id_contract: int, new_status: bool) -> bool:
        """Method to update a contract status by his id.

        Arguments:
            id_contract -- int: the contract id to update
            new_status -- bool: the new status of the contract

        Returns:
            bool
        """
        contract_to_update = self.query.get(id_contract)
        if contract_to_update:
            contract_to_update.status = new_status
            self.session.commit()
            return True
        else:
            return False

    def filter_contracts_by_remaining_amount_desc(self):
        contracts = self.query.order_by(Contract.remaining_amount.desc()).all()
        if contracts:
            return contracts
        else:
            return None

    def filter_contracts_by_total_amount_desc(self):
        contracts = self.query.order_by(Contract.total_amount.desc()).all()
        if contracts:
            return contracts
        else:
            return None

    def filter_contracts_by_status(self, status: str):
        contracts = self.query.filter(Contract.status == status)
        if contracts:
            return contracts
        else:
            return None
