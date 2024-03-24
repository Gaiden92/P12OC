import click

from controllers.user_controller import UserController
from controllers.contract_controller import ContractController

controller_user = UserController()
controller_contract = ContractController()


@click.group()
def contract_commands():
    pass


# Contract commands
@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--client_id", prompt="Enter the client id", help="id of the client", type=int
)
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
def add_contract(
    token: str, client_id: int, total_amount: float, remaining_amount: float
):
    if controller_user.verify_token(token):
        print(total_amount, remaining_amount)
        controller_contract.create_contract(client_id, total_amount, remaining_amount)


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def select_all_contracts(token: str):
    if controller_user.verify_token(token):
        controller_contract.get_all_contracts()


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the contract ID", help="contract id", type=int)
def select_contract_by_id(token: str, id: int):
    if controller_user.verify_token(token):
        controller_contract.get_contract_by_id(id)


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def filter_contracts_by_remaining_amount_desc(token: str):
    if controller_user.verify_token(token):
        controller_contract.filter_contracts_by_remaining_amount_desc()


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def filter_contracts_by_total_amount_desc(token: str):
    if controller_user.verify_token(token):
        controller_contract.filter_contracts_by_total_amount_desc()


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def filter_contracts_by_status(token: str):
    if controller_user.verify_token(token):
        controller_contract.filter_contracts_by_status()


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--new_remaining_amount",
    prompt="Enter the new remaining amount",
    help="new remaining amount of the contract",
    type=float,
)
def update_remaining_amount_by_id(token: str, id: int, new_remaining_amount: float):
    if controller_user.verify_token(token):
        controller_contract.update_remaining_amount_by_id(id, new_remaining_amount)


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--new_total_amount",
    prompt="Enter the new total amount",
    help="new total amount of the contract",
    type=float,
)
def update_total_amount_by_id(token: str, id: int, new_total_amount: float):
    if controller_user.verify_token(token):
        controller_contract.update_total_amount_by_id(id, new_total_amount)


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--status",
    prompt="Enter the new status",
    help="new status of the contract",
    type=click.Choice(["open", "close"], case_sensitive=False),
)
def update_status_by_id(token: str, id: int, status: str):
    if controller_user.verify_token(token):
        controller_contract.update_status_by_id(id, status)


@contract_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--id", prompt="Enter the contract ID", help="ID of the contract", type=int
)
@click.option(
    "--id_client",
    prompt="Enter the new id client",
    help="new id client of the contract",
    type=int,
)
def update_client_contract_by_id(token: str, id: int, id_client: int):
    if controller_user.verify_token(token):
        controller_contract.update_client_contract_by_id(id, id_client)
