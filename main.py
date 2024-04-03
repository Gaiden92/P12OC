import click
import sentry_sdk

from config.parameters import DSN
from commands.user_commands import user_commands
from commands.client_commands import client_commands
from commands.collaborator_commands import collaborator_commands
from commands.company_commands import company_commands
from commands.contract_commands import contract_commands
from commands.event_commands import event_commands
from commands.department_commands import department_commands


@click.group()
def crm():
    """Function to init the crm commands
    """
    sentry_sdk.init(
        dsn=DSN,
        enable_tracing=True)


crm.add_command(user_commands)
crm.add_command(client_commands)
crm.add_command(collaborator_commands)
crm.add_command(company_commands)
crm.add_command(contract_commands)
crm.add_command(event_commands)
crm.add_command(department_commands)


if __name__ == "__main__":
    crm()
