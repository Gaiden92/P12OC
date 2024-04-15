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
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--name",
              prompt="Enter the event name",
              help="event name",
              type=str)
@click.option(
    "--contract_id",
    prompt="Enter the contract id",
    help="id of the contract",
    type=int,
    callback=controller_event.is_contract_valid
)
@click.option(
    "--location",
    prompt="Enter the event location",
    help="event location",
    type=str
)
@click.option(
    "--participants",
    prompt="Enter the number of participants",
    help="number of participant of the event",
    type=int,
)
@click.option(
    "--notes",
    prompt="Enter the event notes",
    help="event notes",
    type=str)
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
def add(
    token: str,
    name: str,
    contract_id: int,
    location: str,
    participants: int,
    notes: str,
    start_date: object,
    end_date: object,
) -> None:
    """Add a new event

    Arguments:
        token -- str: user token
        name -- str: name event
        contract_id -- int: id contract
        location -- str: location event
        participants -- int: participants event
        notes -- str: notes event
        start_date -- str: start date of the event
        end_date -- str: end date of the event
    """
    controller_event.create_event(
        name,
        contract_id,
        location,
        participants,
        notes,
        start_date,
        end_date,
    )


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def select_all(token: str) -> None:
    """Select all events

    Arguments:
        token -- str: token user
    """
    controller_event.get_all_events()


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def filter_by_not_support(token: str) -> None:
    """Filter event with no
    support.

    """
    controller_event.filter_by_not_support()


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def filter_by_if_support(token: str) -> None:
    """Filter all event with
    support.

    """
    controller_event.filter_by_if_support()

@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
def filter_by_is_support(token: str) -> None:
    """Filter all event of the
    support id.

    """
    controller_event.filter_by_is_support()


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the event ID",
              help="event id",
              type=int)
def select_by_id(token: str, id: int) -> None:
    """Select an event by his id.

    Arguments:
        token -- str: token user
        id -- int: id event
    """
    controller_event.get_event_by_id(id)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the event ID",
              help="event id",
              type=int)
@click.option(
    "--new_name",
    prompt="Enter the new event name",
    help="event new name",
    type=str
)
def update_name_by_id(token: str, id: int, new_name: str) -> None:
    """Update the name event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_name -- str: new event name
    """
    controller_event.update_name_event_by_id(id, new_name)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--contract_id",
    prompt="Enter the new contract id",
    help="new contract id",
    type=int,
    callback=controller_event.is_contract_valid
)
def update_contract_by_id(token: str,
                          id: int,
                          contract_id: int
                          ) -> None:
    """Update the contract id event.

    Arguments:
        token -- str: token user
        id -- int: id event
        contract_id -- int: contract id
    """
    controller_event.update_contract_id_event_by_id(id, contract_id)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--support_id",
    prompt="Enter the new support id",
    help="new support id",
    type=int,
    callback=controller_event.is_support_valid
)
def update_support_by_id(token: str,
                         id: int,
                         support_id: int) -> None:
    """Update the support id event.

    Arguments:
        token -- str: token user
        id -- int: id event
        support_id -- int: support id
    """
    controller_event.update_support_id_event_by_id(id, support_id)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_location",
    prompt="Enter the new location",
    help="new location",
    type=str
)
def update_location_by_id(token: str, id: int, new_location: str) -> None:
    """Update the location event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_location -- str: new location
    """
    controller_event.update_location_event_by_id(id, new_location)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id",
              prompt="Enter the event ID",
              help="event id",
              type=int)
@click.option(
    "--new_participants",
    prompt="Enter the new participants",
    help="new participants",
    type=int,
)
def update_participants_by_id(token: str,
                              id: int,
                              new_participants: int) -> None:
    """Update the participants event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_participants -- int: new participants
    """
    controller_event.update_participants_event_by_id(id, new_participants)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option("--new_notes",
              prompt="Enter the new notes",
              help="new notes",
              type=str)
def update_notes_by_id(token: str, id: int, new_notes: str):
    """Update the notes event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_notes -- str: new notes
    """
    controller_event.update_notes_event_by_id(id, new_notes)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_start_date",
    prompt="Enter the new start_date",
    help="new start_date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
def update_start_date_by_id(token: str, id: int, new_start_date: str) -> None:
    """Update the start date event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_start_date -- str: new start date
    """
    controller_event.update_start_date_event_by_id(id, new_start_date)


@event_commands.command()
@click.option("--token",
              prompt="Enter your token",
              help="token user",
              type=str,
              callback=controller_user.verify_token)
@click.option("--id", prompt="Enter the event ID", help="event id", type=int)
@click.option(
    "--new_end_date",
    prompt="Enter the new end_date",
    help="new end_date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
)
def update_end_date_by_id(token: str, id: int, new_end_date: str) -> None:
    """Update the end date event.

    Arguments:
        token -- str: token user
        id -- int: id event
        new_end_date -- str: new end date
    """
    controller_event.update_end_date_event_by_id(id, new_end_date)
