import click

from config.parameters import SUPPORT
from dao.event_dao import EventDao
from dao.contract_dao import ContractDao
from dao.department_dao import DepartmentDao
from views.event_view import EventView
from models.permissions import Permission
from models.user import User


class EventController:
    """A class representing the event controller"""

    def __init__(self) -> None:
        """
        Constructs all necessary attributes of the class

        Arguments:
            database -- str: the database to manage
        """
        self.dao = EventDao()
        self.view = EventView()
        self.department_dao = DepartmentDao()
        self.contract_dao = ContractDao()
        self.user = User.load_user()
        self.permission = Permission(self.user)

    def create_event(
        self,
        name: str,
        contract_id: int,
        location: str,
        participants: int,
        notes: str,
        start_date: str,
        end_date: str,
    ):
        """Method to control an event creation

        Arguments:
            name -- str: the event name
            contract_id -- int: the contract id
            location -- str: the event location
            participants -- int: the participants number
            notes -- str: the event notes
            start_date -- str: the event start date
            end_date -- str: the event end date

        Returns:
            None
        """
        contract = ContractDao().select_contract_by_id(contract_id)
        if not self.permission.isCommercialOfContract(contract):
            return self.view.not_permission_commercial_contract()

        event = self.dao.create_event(
            name,
            contract_id,
            location,
            participants,
            notes,
            start_date,
            end_date,
        )
        if event:
            self.view.create_event_success()
        else:
            self.view.create_event_failed()

    def get_event_by_id(self, id) -> object:
        """Method to get event by id

        Returns:
            object: Event object
        """

        event = self.dao.select_event_by_id(id)
        if event:
            return self.view.display_event(event)
        else:
            return self.view.event_not_exist()

    def get_all_events(self) -> list:
        """Method to get all events by id

        Returns:
            list: list of events
        """

        events = self.dao.select_all_events()
        if events:
            return self.view.display_all_events(events)
        else:
            return self.view.none_events

    def filter_by_not_support(self) -> None:
        """Method to control the filter all events
        if not support.

        Returns:
            None
        """
        if not self.permission.isGestionDepartment():
            return self.view.not_permission()
        events = self.dao.filter_by_not_support()
        if events:
            return self.view.display_all_events(events)
        else:
            return self.view.none_events()

    def filter_by_if_support(self) -> None:
        """Method to control the filter all events
        with support.

        Returns:
            None
        """
        if not self.permission.isSupportDepartment():
            return self.view.not_permission()
        events = self.dao.filter_by_if_support()
        if events:
            return self.view.display_all_events(events)
        else:
            return self.view.none_events()

    def update_name_event_by_id(self, id: int, new_name: str) -> None:
        """Method to update the event name.

        Arguments:
            id -- int: the event id
            new_name -- str: the event new name
        """
        event = self.dao.select_event_by_id(id)
        user = User.load_user()
        permission = Permission(user)
        if not permission.isSupportOfEvent(event):
            return self.view.not_permission_support_of_event()
        event = self.dao.update_name_event_by_id(id, new_name)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_location_event_by_id(self, id: int, new_location: str) -> None:
        """Method to update the event location.

        Arguments:
            id -- int: the event id
            new_location -- str: the event new location
        """
        event = self.dao.update_location_event_by_id(id, new_location)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_notes_event_by_id(self, id: int, new_notes: str) -> None:
        """Method to update the event notes.

        Arguments:
            id -- int: the event id
            new_notes -- str: the event new notes
        """
        event = self.dao.select_event_by_id(id)
        if not self.permission.isSupportOfEvent(event):
            return self.view.not_permission_support_of_event()
        event = self.dao.update_notes_event_by_id(id, new_notes)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_start_date_event_by_id(self,
                                      id: int,
                                      new_start_date: str) -> None:
        """Method to update the event start date.

        Arguments:
            id -- int: the event id
            new_start_date -- str: the event new start date
        """
        event = self.dao.select_event_by_id(id)
        if not self.permission.isSupportOfEvent(event):
            return self.view.not_permission_support_of_event()
        event = self.dao.update_start_date_event_by_id(id, new_start_date)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_end_date_event_by_id(self, id: int, new_end_date: str) -> None:
        """Method to update the event end date.

        Arguments:
            id -- int: the event id
            new_end_date -- str: the event new end date
        """
        event = self.dao.select_event_by_id(id)
        if not self.permission.isSupportOfEvent(event):
            return self.view.not_permission_support_of_event()
        event = self.dao.update_end_date_event_by_id(id, new_end_date)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_participants_event_by_id(self,
                                        id: int,
                                        new_participants: int) -> None:
        """Method to update the event participants.

        Arguments:
            id -- int: the event id
            new_participants -- int: the event new participants
        """
        event = self.dao.select_event_by_id(id)
        if not self.permission.isSupportOfEvent(event):
            return self.view.not_permission_support_of_event()
        event = self.dao.update_participants_event_by_id(id, new_participants)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    def update_support_id_event_by_id(self,
                                      id: int,
                                      new_support_id: int) -> None:
        """Method to update the event support id.

        Arguments:
            id -- int: the event id
            new_support_id -- int: the event new support id
        """
        event = self.dao.select_event_by_id(id)
        if not self.permission.isSupportDepartment():
            return self.view.not_permission_support_of_event()
        event = self.dao.update_support_id_event_by_id(id, new_support_id)
        if event:
            return self.view.update_event_success()
        else:
            return self.view.update_event_failed()

    # Methodes de vérification
    def is_email_valid(self, ctx: object, param: object, email: str) -> str:
        """Method to control if an email is valid

        Arguments:
            ctx -- object: the context
            param -- object: the parameters
            email -- str: the email

        Raises:
            click.BadParameter: _description_

        Returns:
            _description_
        """
        if not "@" and ".fr" in email or "@" and ".com" in email:
            raise click.BadParameter('This email is not valid.\
                                     Please Try again.')
        else:
            return email

    def is_support_valid(self,
                         ctx: object,
                         param: object,
                         id_support: int) -> None:
        """Method to control if the support id exist

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            id_support -- int: the support id

        Raises:
            click.BadParameter: Exception: the support id didn't exist

        Returns:
            int: the support id
        """
        departments = self.department_dao.select_all_departments()
        for department in departments:
            if department.name_department == SUPPORT:
                all_support_ids = [collaborator.id for
                                   collaborator in department.collaborators]
        if id_support not in all_support_ids:
            raise click.BadParameter("This support id doesn't exist.")
        else:
            return id_support

    def is_contract_valid(self,
                          ctx: object,
                          param: object,
                          id_contract: int) -> None:
        """Method to control if the contract id exist

        Arguments:
            ctx -- object: the context
            param -- object: the parameter
            id_contract -- int: the contract id

        Raises:
            click.BadParameter: Exception: the contract id didn't exist

        Returns:
            int: the contract id
        """
        all_contracts_id = [contract.id for contract in
                            self.contract_dao.select_all_contracts()]
        if id_contract not in all_contracts_id:
            raise click.BadParameter("This contract id doesn't exist.")
        else:
            return id_contract
