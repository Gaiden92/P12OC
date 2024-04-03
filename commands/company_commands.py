import click

from controllers.user_controller import UserController
from controllers.company_controller import CompanyController


controller_user = UserController()
controller_company = CompanyController()


@click.group()
def company_commands():
    """Function to init company commands
    """
    pass


# company commands
@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option(
    "--name",
    prompt="Enter the company name",
    help="name of the company",
    type=str
)
def add(token: str, name: str) -> None:
    """Function command to add a new company

    Arguments:
        token -- str: token user
        name -- str: name company
    """
    controller_company.create_company(name)


@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Function to select all companies

    Arguments:
        token -- str: token user
    """
    controller_company.get_all_companies()


@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the company id",
              help="the company id",
              type=int)
def select_by_id(token: str, id: int) -> None:
    """Function to select a company by his id

    Arguments:
        token -- str: token user
        id -- int: company id
    """
    controller_company.get_company_by_id(id)


@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the company ID",
              help="ID of the company",
              type=int)
@click.option(
    "--new_name",
    prompt="Enter the new company's name",
    help="new name of the company",
    type=str,
)
def update_name_by_id(token: str, id: int, new_name: str) -> None:
    """Function command to update a name company

    Arguments:
        token -- str: token user
        id -- int: id company
        new_name -- str: new name company
    """
    controller_company.update_company_name_by_id(id, new_name)


@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the company ID",
              help="ID of the company",
              type=int)
def delete_by_id(token: str, id: int) -> None:
    """Function command to delete a company by his id

    Arguments:
        token -- str: token user
        id -- int: company id
    """
    controller_company.delete_company_by_id(id)
