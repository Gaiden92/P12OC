import click

from controllers.user_controller import UserController
from controllers.contract_controller import ContractController

controller_user = UserController()
controller_contract = ContractController()


@click.group()
def contract_commands():
    """Function to init contract commands
    """
    pass


# Contract commands
@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option("--client_id",
              prompt="Enter the client id",
              help="id of the client",
              type=int,
              callback=controller_contract.is_client_valid)
@click.option(
    "--total_amount",
    prompt="Enter the contract total amount ",
    help="total amount of the contract",
    type=float,
)
@click.option(
    "--remaining_amount",
    prompt="Enter the contract remaining amount",
    help="remaining amount of the contract",
    type=float,
)
def add(
    token: str, client_id: int, total_amount: float, remaining_amount: float
) -> None:
    """Function command to add a new contract

    Arguments:
        token -- str: token user
        client_id -- int: id client
        total_amount -- float: total amount
        remaining_amount -- float: remaining amount
    """
    controller_contract.create_contract(client_id,
                                        total_amount,
                                        remaining_amount)


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Function command to select all contracts

    Arguments:
        token -- str: token user
    """
    controller_contract.get_all_contracts()


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the contract ID",
              help="contract id",
              type=int)
def select_by_id(token: str, id: int) -> None:
    """Function command to select a contract by his id

    Arguments:
        token -- str: token user
        id -- int: id contract
    """
    controller_contract.get_contract_by_id(id)


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
def filter_by_remaining_amount_desc(token: str) -> None:
    """Function command to filter contract by remaining amount

    Arguments:
        token -- str: token user
    """
    controller_contract.filter_contracts_by_remaining_amount_desc()


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
def filter_by_total_amount_desc(token: str) -> None:
    """Function command to filter contract by total amount

    Arguments:
        token -- str: token user
    """
    controller_contract.filter_contracts_by_total_amount_desc()


@contract_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def filter_by_status(token: str) -> None:
    """Function command to filter contract by status

    Arguments:
        token -- str: token user
    """
    controller_contract.filter_contracts_by_status()


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--new_remaining_amount",
    prompt="Enter the new remaining amount",
    help="new remaining amount of the contract",
    type=float,
)
def update_remaining_amount_by_id(token: str,
                                  id: int,
                                  new_remaining_amount: float) -> None:
    """Function command to update a contract remaining amount

    Arguments:
        token -- str: user token
        id -- int: contract id
        new_remaining_amount -- float: new remaining amount
    """
    controller_contract.update_remaining_amount_by_id(id, new_remaining_amount)


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--new_total_amount",
    prompt="Enter the new total amount",
    help="new total amount of the contract",
    type=float,
)
def update_total_amount_by_id(token: str,
                              id: int,
                              new_total_amount: float) -> None:
    """Function command to update a contract total amount

    Arguments:
        token -- str: user token
        id -- int: contract id
        new_total_amount -- float: new total amount
    """
    controller_contract.update_total_amount_by_id(id, new_total_amount)


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--status",
    prompt="Enter the new status",
    help="new status of the contract",
    type=click.Choice(["open", "close"], case_sensitive=False),
)
def update_status_by_id(token: str, id: int, status: str) -> None:
    """Function command to update a contract status

    Arguments:
        token -- str: user token
        id -- int: contract id
        status -- str: new status
    """
    controller_contract.update_status_by_id(id, status)


@contract_commands.command()
@click.option(
    "--token",
    prompt="Enter your token",
    help="token user",
    type=str,
    callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--id_client",
    prompt="Enter the new id client",
    help="new id client of the contract",
    type=int,
    callback=controller_contract.is_client_valid
)
def update_client_by_id(token: str, id: int, id_client: int) -> None:
    """Function command to update a contract client

    Arguments:
        token -- str: user token
        id -- int: contract id
        id_client -- int: new id client
    """
    controller_contract.update_client_contract_by_id(id, id_client)
