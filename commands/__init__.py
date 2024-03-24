import click
from controllers.user_controller import UserController
from controllers.collaborator_controller import CollaboratorController


@click.group()
def crm():
    pass


@crm.command()
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
    controller_user.login(id, password)


@crm.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option(
    "--name", prompt="Enter name collaborator", help="name collaborator", type=str
)
@click.option(
    "--contact",
    prompt="Enter contact collaborator",
    help="contact collaborator",
    type=str,
)
@click.option(
    "--password",
    prompt="Enter password collaborator",
    help="password collaborator",
    type=str,
)
@click.option(
    "--department_id",
    prompt="Enter department id collaborator",
    help="department id collaborator",
    type=int,
)
def add_collaborator(token, name, contact, password, department_id):
    controller_collaborator = CollaboratorController()
    controller_collaborator.create_collaborator(
        token, name, contact, password, department_id
    )
