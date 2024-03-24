import click

from controllers.user_controller import UserController
from controllers.event_controller import EventController

controller_user = UserController()
controller_event = EventController()


@click.group()
def event_commands():
    pass


# Events
@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--name", prompt="Enter the event name", help="event name", type=str)
@click.option(
    "--contract_id", prompt="Enter the contract id", help="id of the contract", type=int
)
@click.option(
    "--support_id", prompt="Enter the support id", help="id of the support", type=int
)
@click.option(
    "--location", prompt="Enter the event location", help="event location", type=str
)
@click.option(
    "--participants",
    prompt="Enter the number of participants",
    help="number of participant of the event",
    type=int,
)
@click.option("--notes", prompt="Enter the event notes", help="event notes", type=str)
@click.option(
    "--start_date",
    prompt="Enter the event start date",
    help="event start date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
@click.option(
    "--end_date",
    prompt="Enter the event end date",
    help="event end date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
def add_event(
    token: str,
    name: str,
    contract_id: int,
    support_id: int,
    location: str,
    participants: int,
    notes: str,
    start_date: object,
    end_date: object,
):
    if controller_user.verify_token(token):
        controller_event.create_event(
            name,
            contract_id,
            support_id,
            location,
            participants,
            notes,
            start_date,
            end_date,
        )


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
def select_all_events(token: str):
    if controller_user.verify_token(token):
        controller_event.get_all_events()


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
def select_event_by_id(token: str, id: int):

    if controller_user.verify_token(token):
        controller_event.get_event_by_id(id)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_name", prompt="Enter the new event name", help="event new name", type=str
)
def update_name_event_by_id(token: str, id: int, new_name: str):
    if controller_user.verify_token(token):
        controller_event.update_name_event_by_id(id, new_name)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--contract_id",
    prompt="Enter the new contract id",
    help="new contract id",
    type=int,
)
def update_contract_id_event_by_id(token: str, id: int, contract_id: int):
    if controller_user.verify_token(token):
        controller_event.update_contract_id_event_by_id(id, contract_id)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--support_id", prompt="Enter the new support id", help="new support id", type=int
)
def update_support_id_event_by_id(token: str, id: int, support_id: int):
    if controller_user.verify_token(token):
        controller_event.update_support_id_event_by_id(id, support_id)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_location", prompt="Enter the new location", help="new location", type=str
)
def update_location_event_by_id(token: str, id: int, new_location: str):
    if controller_user.verify_token(token):
        controller_event.update_location_event_by_id(id, new_location)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_participants",
    prompt="Enter the new participants",
    help="new participants",
    type=int,
)
def update_participants_event_by_id(token: str, id: int, new_participants: int):
    if controller_user.verify_token(token):
        controller_event.update_participants_event_by_id(id, new_participants)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option("--new_notes", prompt="Enter the new notes", help="new notes", type=str)
def update_notes_event_by_id(token: str, id: int, new_notes: str):
    if controller_user.verify_token(token):
        controller_event.update_notes_event_by_id(id, new_notes)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_start_date",
    prompt="Enter the new start_date",
    help="new start_date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
def update_start_date_event_by_id(token: str, id: int, new_start_date: str):
    if controller_user.verify_token(token):
        controller_event.update_start_date_event_by_id(id, new_start_date)


@event_commands.command()
@click.option("--token", prompt="Enter your token", help="token user", type=str)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_end_date",
    prompt="Enter the new end_date",
    help="new end_date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
def update_end_date_event_by_id(token: str, id: int, new_end_date: str):
    if controller_user.verify_token(token):
        controller_event.update_end_date_event_by_id(id, new_end_date)
