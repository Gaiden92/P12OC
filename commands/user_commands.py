import click

from controllers.user_controller import UserController
from controllers.collaborator_controller import CollaboratorController

controller_user = UserController()
controller_collaborator = CollaboratorController()


@click.group()
def user_commands():
    """function to initiate the commands user
    """
    pass


# login command
@user_commands.command()
@click.option("--id",
              prompt="Enter your ID",
              help="ID of the collaborator",
              type=int)
@click.option(
    "--password",
    prompt="Enter your password",
    help="Password of the collaborator",
    hide_input=True,
    type=str,
)
def login(id: int, password: str) -> None:
    """Function command to login

    Arguments:
        id -- int: id of the collaborator
        password -- str: password collaborator
    """
    if controller_user.check_entry_user(id, password):
        controller_collaborator.check_login(id, password)
