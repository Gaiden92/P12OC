import click

from controllers.user_controller import UserController
from controllers.collaborator_controller import CollaboratorController


@click.group()
def user_commands():
    pass


# login command
@user_commands.command()
@click.option("--id", prompt="Enter your ID", help="ID of the collaborator", type=int)
@click.option(
    "--password",
    prompt="Enter your password",
    help="Password of the collaborator",
    hide_input=True,
    type=str,
)
def login(id, password):
    controller_user = UserController()
    controller_collaborator = CollaboratorController()
    if controller_user.check_entry_user(id, password):
        controller_collaborator.check_login(id, password)
