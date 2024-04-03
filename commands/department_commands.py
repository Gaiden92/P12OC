import click

from controllers.user_controller import UserController
from controllers.department_controller import DepartmentController

controller_user = UserController()
controller_department = DepartmentController()


@click.group()
def department_commands():
    """Function to init department commands 
    """
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
              type=str)
def add(token: str, name: str) -> None:
    """Function command to add a new department

    Arguments:
        token -- str: token user
        name -- str: name department
    """
    controller_department.create_department(name)


@department_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Function command to select all departments

    Arguments:
        token -- str: token user
    """
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
def select_by_id(token: str, id: int) -> None:
    """Function command to select a department by his id

    Arguments:
        token -- str: token user
        id -- id: department id
    """
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
              type=int)
@click.option(
    "--new_name",
    prompt="Enter the new department's name",
    help="new name of the department",
    type=str,
)
def update_name_by_id(token: str, id: int, new_name: str) -> None:
    """Function command to update a department

    Arguments:
        token -- str: token user
        id -- int: id department
        new_name -- str: new name department
    """
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
              type=int)
def delete_by_id(token: str, id: int) -> None:
    """Function to delete a department by his id

    Arguments:
        token -- str: token user
        id -- int: id department
    """
    controller_department.delete_department_by_id(id)
