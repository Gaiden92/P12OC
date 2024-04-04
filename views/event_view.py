import tableprint as tp


class EventView:
    """A class representing the view for a class Event"""

    def display_all_events(self, events: list) -> None:
        """Method to diplay all events

        Arguments:
            events -- list: events
        """
        headers = ["Informations", "Values"]
        print(tp.header(headers, [12, 80]))
        for event in events:
            print(tp.row(["Event id", str(event.id)], [12, 80]))
            print(tp.row(["Name event", event.event_name], [12, 80]))
            print(tp.row(["Contract id", str(event.contract_id)], [12, 80]))
            print(tp.row([
                "Client name",
                event.contract.client.name_client],
                [12, 80]))
            print(tp.row(["Start date", str(event.start_date)], [12, 80]))
            print(tp.row(["End date", str(event.end_date)], [12, 80]))
            print(tp.row(["Notes", event.notes], [12, 80]))
            print(tp.row(["Participants", str(event.participants)], [12, 80]))
            print(tp.row(["Location", event.location], [12, 80]))
            if event.support:
                print(tp.row([
                    "Support id",
                    str(event.support.name_collaborator)],
                    [12, 80]))
            else:
                print(tp.row(["Support id", "none support yet"], [12, 80]))
            print("-"*97)
        print(tp.bottom(2, [12, 80]))

    def display_event(self, event: object) -> None:
        """Method to display one event.

        Arguments:
            event -- object:event
        """
        print(tp.row(["Event id", str(event.id)], [12, 80]))
        print(tp.row(["Name event", event.event_name], [12, 80]))
        print(tp.row(["Contract id", str(event.contract_id)], [12, 80]))
        print(tp.row(["Client name",
                      event.contract.client.name_client], [12, 80]))
        print(tp.row(["Start date", str(event.start_date)], [12, 80]))
        print(tp.row(["End date", str(event.end_date)], [12, 80]))
        print(tp.row(["Notes", event.notes], [12, 80]))
        print(tp.row(["Participants", str(event.participants)], [12, 80]))
        print(tp.row(["Location", event.location], [12, 80]))
        if event.support:
            print(tp.row(
                [
                    "Support id",
                    str(event.support.name_collaborator)
                    ], [12, 80]))
        else:
            print(tp.row(["Support id", "not support yet"], [12, 80]))
        print(tp.bottom(2, [12, 80]))

    @staticmethod
    def create_event_success() -> None:
        """Method to display a success message after
        the creation of an event.
        """
        print("Success event creation.")

    @staticmethod
    def create_event_failed() -> None:
        """Method to display a failed message after tried
        to create an event.
        """
        print("Failed event creation.")

    @staticmethod
    def event_not_exist() -> None:
        """Method to display a message that is none event
        of this id in database.
        """
        print("This event didn't exist.")

    @staticmethod
    def none_events() -> None:
        """Method to display a message that is none
        events actually in database.
        """
        print("None event in database")

    @staticmethod
    def update_event_success() -> None:
        """Method to display a success message after
        the update of an event.
        """
        print("Success event update.")

    @staticmethod
    def update_event_failed() -> None:
        """Method to display a failed message after
        tried to update an event.
        """
        print("Failed event update.")

    @staticmethod
    def not_permission_commercial_contract() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("Your not the contract commercial.")

    @staticmethod
    def not_permission_support_of_event() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("Your not the contract support.")
