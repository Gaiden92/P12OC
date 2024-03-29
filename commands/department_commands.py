import click

from controllers.user_controller import UserController
from controllers.department_controller import DepartmentController

controller_user = UserController()
controller_department = DepartmentController()

@click.group()
def department_commands():
    pass


# Department commands
@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--name",
              prompt="Enter name department",
              help="name department",
              type=str
)
def add_department(token: str, name: str):
    controller_department.create_department(name)


@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all_departments(token: str):
    controller_department.get_all_departments()


@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the ID department",
              help="id department",
              type=int)
def select_department_by_id(token: str, id: int):
    controller_department.get_department_by_id(id)


@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the department ID",
              help="ID of the department",
              type=int
)
@click.option(
    "--new_name",
    prompt="Enter the new department's name",
    help="new name of the department",
    type=str,
)
def update_department_name_by_id(token: str, id: int, new_name: str):
    controller_department.update_department_name_by_id(id, new_name)

@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the department ID",
              help="ID of the department",
              type=int
)
def delete_department_by_id(token: str, id: int):
    controller_department.delete_department_by_id(id)