import click

from controllers.user_controller import UserController
from controllers.collaborator_controller import CollaboratorController

controller_user = UserController()
controller_collaborator = CollaboratorController()


@click.group()
def collaborator_commands():
    pass


# collaborator commands
@collaborator_commands.command()
@click.option('--token', prompt='Enter your token', help="Enter your token", type=str, callback=controller_user.verify_token)
@click.option(
    "--name", prompt="Enter name collaborator", help="name collaborator", type=str
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
def add_collaborator(token, name, contact, password, department_id):
    controller_collaborator.create_collaborator(
            name, contact, password, department_id
        )


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all_collaborators(token):
    controller_collaborator.get_all_collaborators()


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the collaborator ID", help="ID of the collaborator", type=int
)
def select_collaborator_by_id(token: str, id: int):
    controller_collaborator.get_collaborator_by_id(id)


@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
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
def update_collaborator_name_by_id(token: str, id: int, new_name: str):
    controller_collaborator.update_collaborator_name_by_id(id, new_name)

@collaborator_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--id", prompt="Enter the collaborator ID", help="ID of the collaborator", type=int
)
def delete_collaborator_by_id(token: str, id: int):
    controller_collaborator.delete_collaborator_by_id(id)
