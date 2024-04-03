import tableprint as tp


class EventView:
    """A class representing the view for a class Event"""

    def display_all_events(self, events: list) -> None:
        """Method to diplay all events

        Arguments:
            events -- list: events
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers,[12, 80]))
        for event in events:
            print(tp.row(["Event id", str(event.id)], [12, 80]))
            print(tp.row( ["Name event", event.event_name], [12, 80]))
            print(tp.row(["Contract id", str(event.contract_id)], [12, 80]))
            print(tp.row(["Client name", event.contract.client.name_client], [12, 80]))
            print(tp.row(["Start date", str(event.start_date)], [12, 80]))
            print(tp.row(["End date", str(event.end_date)], [12, 80]))
            print(tp.row(["Notes", event.notes], [12, 80]))
            print(tp.row(["Participants", str(event.participants)], [12, 80]))
            print(tp.row(["Location", event.location], [12, 80]))
            if event.support:
                print(tp.row(["Support id", str(event.support.name_collaborator)], [12, 80]))
            else:
                print(tp.row(["Support id","pas de support"], [12, 80]))
            print("-"*97)
        print(tp.bottom(2, [12, 80]))

    def display_event(self, event: object) -> None:
        """Method to display one event.

        Arguments:
            event -- object:event
        """
        print(tp.row(["Event id", str(event.id)], [12, 80]))
        print(tp.row( ["Name event", event.event_name], [12, 80]))
        print(tp.row(["Contract id", str(event.contract_id)], [12, 80]))
        print(tp.row(["Client name", event.contract.client.name_client], [12, 80]))
        print(tp.row(["Start date", str(event.start_date)], [12, 80]))
        print(tp.row(["End date", str(event.end_date)], [12, 80]))
        print(tp.row(["Notes", event.notes], [12, 80]))
        print(tp.row(["Participants", str(event.participants)], [12, 80]))
        print(tp.row(["Location", event.location], [12, 80]))
        if event.support:
            print(tp.row(["Support id", str(event.support.name_collaborator)], [12, 80]))
        else:
            print(tp.row(["Support id","pas de support"], [12, 80]))
        print(tp.bottom(2, [12, 80]))

    @staticmethod
    def create_event_success() -> None:
        """Method to display a success message after
        the creation of an event.
        """
        print("L'evenement a été crée avec succés.")

    @staticmethod
    def create_event_failed() -> None:
        """Method to display a failed message after tried
        to create an event.
        """
        print("L'evenement n'a pas pu être crée.")

    @staticmethod
    def event_not_exist() -> None:
        """Method to display a message that is none event
        of this id in database.
        """
        print("L'évenement n'existe pas.")

    @staticmethod
    def none_events() -> None:
        """Method to display a message that is none
        events actually in database.
        """
        print("Aucuns évenements en base de donnée")

    @staticmethod
    def update_event_success() -> None:
        """Method to display a success message after
        the update of an event.
        """
        print("L'evenement a bien été mis à jour.")

    @staticmethod
    def update_event_failed() -> None:
        """Method to display a failed message after
        tried to update an event.
        """
        print("L'evenement n'a pas pu être mis à jour.")

    @staticmethod
    def not_permission_commercial_contract() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("Vous n'êtes pas le commercial du contrat.")

    @staticmethod
    def not_permission_support_of_event() -> None:
        """Method to display a message that the user
        has not the permission to update the contract.
        """
        print("Vous n'êtes pas le support du contrat.")