from models.event import Event
from config.parameters import DB


class EventDao:
    """A class represents the department table"""

    def __init__(self) -> None:
        """Constructor of EventDao class

        Arguments:
            Session -- object: an session object
        """
        self.db = DB
        self.session = self.db.session()
        self.query = self.session.query(Event)

    def select_all_events(self) -> list:
        """A method for select all events in database

        Returns:
            None or list of Event object:
        """
        events = self.query.all()
        if events:
            return events
        else:
            None

    def filter_by_not_support(self) -> None:
        """Method to get all events with no support.

        Returns:
            None
        """
        events = self.query.filter(Event.support_id is None).all()
        if events:
            return events
        else:
            return None

    def filter_by_if_support(self) -> None:
        """Method to get all events with support.

        Returns:
            None
        """
        events = self.query.filter(Event.support_id is not None).all()
        if events:
            return events
        else:
            return None

    def filter_by_is_support(self, support_id: int) -> None:
        """Method to get all the events of the support id.

        Arguments:
            support_id -- int: id of the support
        Returns:
            None
        """
        events = self.query.filter(Event.support_id == support_id).all()
        if events:
            return events
        else:
            return None

    def select_event_by_id(self, event_id: int) -> object:
        """Method to get event by id

        Arguments:
            event_id -- int: id of a event

        Returns:
            object or None
        """
        event = self.query.filter(Event.id == event_id).first()
        if event:
            return event
        else:
            return None

    def create_event(
        self,
        event_name: str,
        contract_id: int,
        location: str,
        attendees: int,
        notes: str,
        start_date: str,
        end_date: str,
    ) -> bool:
        """Method to insert new event in database.

        Arguments:
            event_name -- str: the name of the new event to add.
            contract_id -- int: the contract id
            location -- str: the event location
            attendees -- int: the event attendees
            notes -- str: the event notes

        Returns:
            bool
        """
        event = Event(
            event_name=event_name,
            contract_id=contract_id,
            location=location,
            participants=attendees,
            notes=notes,
            start_date=start_date,
            end_date=end_date,
        )
        try:
            self.session.add(event)
            self.session.commit()
        except Exception:
            return False
        return True

    def update_name_event_by_id(self, event_id: int, new_name: str) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            new_name -- str: the new name of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.event_name = new_name
            self.session.commit()
            return True
        else:
            return False

    def update_contract_id_event_by_id(self,
                                       event_id: int,
                                       contract_id: int) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            contract_id -- int: the contract id of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.contract_id = contract_id
            self.session.commit()
            return True
        else:
            return False

    def update_support_id_event_by_id(self,
                                      event_id: int,
                                      support_id: int) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            support_id -- int: the support id of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.support_id = support_id
            self.session.commit()
            return True
        else:
            return False

    def update_location_event_by_id(self,
                                    event_id: int,
                                    location: str) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            location -- str: the location of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.location = location
            self.session.commit()
            return True
        else:
            return False

    def update_participants_event_by_id(self,
                                        event_id: int,
                                        participants: int) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            participants -- int: the participants of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.participants = participants
            self.session.commit()
            return True
        else:
            return False

    def update_notes_event_by_id(self,
                                 event_id: int,
                                 notes: str) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            notes -- str: the notes of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.notes = notes
            self.session.commit()
            return True
        else:
            return False

    def update_start_date_event_by_id(self,
                                      event_id: int,
                                      start_date: str) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            start_date -- str: the start date of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.start_date = start_date
            self.session.commit()
            return True
        else:
            return False

    def update_end_date_event_by_id(self,
                                    event_id: int,
                                    end_date: str) -> bool:
        """Method to update a event by his id.

        Arguments:
            event_id -- int: the id of the event to update
            end_date -- str: the end date of the event

        Returns:
            bool
        """
        event_to_update = self.query.get(event_id)
        if event_to_update:
            event_to_update.end_date = end_date
            self.session.commit()
            return True
        else:
            return False
