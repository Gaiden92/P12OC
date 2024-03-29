import click

from controllers.user_controller import UserController
from controllers.company_controller import CompanyController


controller_user = UserController()
controller_company = CompanyController()


@click.group()
def company_commands():
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
def add_company(token: str, name: str):
    controller_company.create_company(name)


@company_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all_companies(token: str):
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
def select_company_by_id(token: str, id: int):
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
def update_company_name_by_id(token: str, id: int, new_name: str):
    controller_company.update_company_name_by_id(id, new_name)


@company_commands.command()
@click.option("--token", 
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the company ID", help="ID of the company", type=int)
def delete_company_by_id(token: str, id: int):
    controller_company.delete_company_by_id(id)
