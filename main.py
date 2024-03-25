import click

from commands.user_commands import user_commands
from commands.client_commands import client_commands
from commands.collaborator_commands import collaborator_commands
from commands.company_commands import company_commands
from commands.contract_commands import contract_commands
from commands.event_commands import event_commands


@click.group()
def crm():
    pass


crm.add_command(user_commands)
crm.add_command(client_commands)
crm.add_command(collaborator_commands)
crm.add_command(company_commands)
crm.add_command(contract_commands)
crm.add_command(event_commands)


if __name__ == "__main__":
    crm()
