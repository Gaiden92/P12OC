import click

from controllers.user_controller import UserController
from controllers.collaborator_controller import CollaboratorController

controller_user = UserController()
controller_collaborator = CollaboratorController()


@click.group()
def collaborator_commands():
    """Function to init collaborator commands
    """
    pass


# collaborator commands
@collaborator_commands.command()
@click.option('--token',
              prompt='Enter your token',
              help="Enter your token",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--name",
    prompt="Enter name collaborator",
    help="name collaborator",
    type=str
)
@click.option(
    "--contact",
    prompt="Enter contact collaborator",
    help="contact collaborator",
    type=str,
    callback=controller_collaborator.is_phone_valid
)
@click.option(
    "--password",
    prompt="Enter password collaborator",
    help="password collaborator",
    hide_input=True,
    confirmation_prompt=True,
    type=str,
)
@click.option(
    "--department_id",
    prompt="Enter department id collaborator",
    help="department id collaborator",
    type=int,
    callback=controller_collaborator.is_department_valid
)
def add(token: str,
        name: str,
        contact: str,
        password: str,
        department_id: id) -> None:
    """Add a new collaborator in database.

    Arguments:
        token -- str: token collaborator
        name -- str: name collaborator
        contact -- str: contact collaborator
        password -- str: password collaborator
        id -- int: id department
    """
    controller_collaborator.create_collaborator(
            name, contact, password, department_id
        )


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Select all collaborators to display them.

    Arguments:
        token -- str: token user
    """
    controller_collaborator.get_all_collaborators()


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id",
    prompt="Enter the collaborator ID",
    help="ID of the collaborator",
    type=int
)
def select_by_id(token: str, id: int) -> None:
    """Select a collaborator by his id to display.

    Arguments:
        token -- str: token user
    """
    controller_collaborator.get_collaborator_by_id(id)


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id",
    prompt="Enter the collaborator ID",
    help="ID of the collaborator",
    type=int
)
@click.option(
    "--new_name",
    prompt="Enter the new collaborator's name",
    help="new name of the collaborator",
    type=str,
)
def update_name_by_id(token: str, id: int, new_name: str) -> None:
    """Update a name collaborator.

    Arguments:
        token -- str: token user
        id -- int: id collaborator
        new_name -- str: new name
    """
    controller_collaborator.update_collaborator_name_by_id(id, new_name)


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id",
    prompt="Enter the collaborator ID",
    help="ID of the collaborator",
    type=int
)
@click.option(
    "--new_contact",
    prompt="Enter the new collaborator's contact",
    help="new contact of the collaborator",
    type=str,
    callback=controller_collaborator.is_phone_valid
)
def update_contact_by_id(token: str, id: int, new_contact: str) -> None:
    """Update a contact collaborator.

    Arguments:
        token -- str: token user
        id -- int: id collaborator
        new_contact -- str: new contact
    """
    controller_collaborator.update_collaborator_contact_by_id(id, new_contact)


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id",
    prompt="Enter the collaborator ID",
    help="ID of the collaborator",
    type=int
)
def delete_by_id(token: str, id: int) -> None:
    """delete a collaborator.

    Arguments:
        token -- str: token user
        id -- int: id collaborator
    """
    controller_collaborator.delete_collaborator_by_id(id)
