import click

from controllers.user_controller import UserController
from controllers.client_controller import ClientController


controller_user = UserController()
controller_client = ClientController()


@click.group()
def client_commands():
    """Function to initiate the client commands
    """
    pass


# Client commands
@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--name",
    prompt="Enter the client name",
    help="name of the client",
    type=str
)
@click.option(
    "--contact",
    prompt="Enter the client contact",
    help="phone of the client",
    type=str,
    callback=controller_client.is_phone_valid
)
@click.option(
    "--email",
    prompt="Enter the client email",
    help="email of the client",
    type=str,
    callback=controller_client.is_email_valid
)
@click.option(
    "--company_id",
    prompt="Enter the company id",
    help="company id of the client",
    type=int,
    callback=controller_client.is_company_valid
)
def add(token: str, name: str, contact: str, email: str, company_id: int) -> None:
    """Function command to add a new client 

    Arguments:
        token -- str: token user
        name -- str: client name
        contact -- str: client phone
        email -- str: client email
        company_id -- int: company id
    """
    controller_client.create_client(name, contact, email, company_id)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Function command to select all client

    Arguments:
        token -- str: token user
    """
    controller_client.get_all_clients()


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client id",
              help="the client id",
              type=int)
def select_by_id(token: str, id: int) -> None:
    """Function command to select by id a client

    Arguments:
        token -- str: token user
        id -- int: client id
    """
    controller_client.get_client_by_id(id)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client ID",
              help="ID of the client",
              type=int)
@click.option(
    "--new_name",
    prompt="Enter the new client's name",
    help="new name of the client",
    type=str,
)
def update_name_by_id(token: str, id: int, new_name: str) -> None:
    """Function command to update a name client by id

    Arguments:
        token -- str: token user
        id -- int: id client
        new_name -- str: new name client
    """
    controller_client.update_client_name_by_id(id, new_name)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client ID",
              help="ID of the client",
              type=int)
@click.option(
    "--new_phone",
    prompt="Enter the new client's phone",
    help="new phone of the client",
    type=str,
    callback=controller_client.is_phone_valid
)
def update_phone_by_id(token: str, id: int, new_phone: str) -> None:
    """Function command to update a phone client by id

    Arguments:
        token -- str: token user
        id -- int: id client
        new_phone -- str: new phone client
    """
    controller_client.update_phone_client_by_id(id, new_phone)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client ID",
              help="ID of the client",
              type=int)
@click.option(
    "--new_email",
    prompt="Enter the new client's email",
    help="new email of the client",
    type=str,
    callback=controller_client.is_email_valid
)
def update_email_by_id(token: str, id: int, new_email: str) -> None:
    controller_client.update_email_client_by_id(id, new_email)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client ID",
              help="ID of the client",
              type=int)
@click.option(
    "--id_commercial",
    prompt="Enter the new client's id commercial",
    help="new commercial id of the client",
    type=int,
    callback=controller_client.is_commercial_valid
)
def update_commercial_by_id(token: str, id: int, id_commercial: int):
    """Function command to update a commercial client by id

    Arguments:
        token -- str: token user
        id -- int: id client
        id_commercial -- int: id new commercial client
 id    """
    controller_client.update_commercial_client_by_id(id, id_commercial)


@client_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the client ID",
              help="ID of the client",
              type=int)
def delete_by_id(token: str, id: int) -> None:
    """Function command to delete a client by id

    Arguments:
        token -- str: token user
        id -- int: id client
    """
    controller_client.delete_client_by_id(id)
