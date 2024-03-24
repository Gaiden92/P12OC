import click

from controllers.user_controller import UserController
from controllers.client_controller import ClientController


@click.group()
def client_commmands():
    pass


# Client commands
@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--name", prompt="Enter the client name", help="name of the client", type=str
)
@click.option(
    "--contact", prompt="Enter the client contact", help="phone of the client", type=str
)
@click.option(
    "--email", prompt="Enter the client email", help="email of the client", type=str
)
@click.option(
    "--company_id",
    prompt="Enter the company id",
    help="company id of the client",
    type=int,
)
def add_client(token: str, name: str, contact: str, email: str, company_id: int):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.create_client(name, contact, email, company_id)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def select_all_clients(token: str):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.get_all_clients()


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client id", help="the client id", type=int)
def select_client_by_id(token: str, id: int):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.get_client_by_id(id)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client ID", help="ID of the client", type=int)
@click.option(
    "--new_name",
    prompt="Enter the new client's name",
    help="new name of the client",
    type=str,
)
def update_client_name_by_id(token: str, id: int, new_name: str):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.update_client_name_by_id(id, new_name)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client ID", help="ID of the client", type=int)
@click.option(
    "--new_phone",
    prompt="Enter the new client's phone",
    help="new phone of the client",
    type=str,
)
def update_phone_client_by_id(token: str, id: int, new_phone: str):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.update_phone_client_by_id(id, new_phone)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client ID", help="ID of the client", type=int)
@click.option(
    "--new_email",
    prompt="Enter the new client's email",
    help="new email of the client",
    type=str,
)
def update_email_client_by_id(token: str, id: int, new_email: str):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.update_email_client_by_id(id, new_email)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client ID", help="ID of the client", type=int)
@click.option(
    "--id_company",
    prompt="Enter the new client's id company",
    help="new company id of the client",
    type=int,
)
def update_company_client_by_id(token: str, id: int, id_company: int):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.update_company_client_by_id(id, id_company)


@client_commmands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the client ID", help="ID of the client", type=int)
@click.option(
    "--id_commercial",
    prompt="Enter the new client's id commercial",
    help="new commercial id of the client",
    type=int,
)
def update_commercial_client_by_id(token: str, id: int, id_commercial: int):
    controller_user = UserController()
    if controller_user.verify_token(token):
        controller_client = ClientController()
        controller_client.update_commercial_client_by_id(id, id_commercial)
