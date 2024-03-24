class EventView:
    """A class representing the view for a class Event"""

    def display_all_events(self, events:list)->None:
        """Method to diplay all events

        Arguments:
            events -- list: events
        """
        print(events)

    def display_event(self, event:object)->None:
        """Method to display one event.

        Arguments:
            event -- object:event
        """
        print(event)

    @staticmethod
    def create_event_success():
        """Method to display a success message after the creation of an event.
        """
        print("L'evenement a été crée avec succés.")

    @staticmethod
    def create_event_failed():
        """Method to display a failed message after tried to create an event.
        """
        print("L'evenement n'a pas pu être crée.")

    @staticmethod
    def event_not_exist():
        """Method to display a message that is none event of this id in database.
        """
        print("L'évenement n'existe pas.")

    @staticmethod
    def none_events():
        """Method to display a message that is none events actually in database.
        """
        print("Aucuns évenements en base de donnée")

    @staticmethod
    def update_event_success():
        """Method to display a success message after the update of an event.
        """
        print("L'evenement a bien été mis à jour.")

    @staticmethod
    def update_event_failed():
        """Method to display a failed message after tried to update an event.
        """
        print("L'evenement n'a pas pu être mis à jour.")
