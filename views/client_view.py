class ClientView:
    """A class representing the view for a class Client"""

    def display_all_clients(self, clients: list) -> None:
        """Method to display all clients

        Arguments:
            clients -- list: clients
        """
        print(clients)

    def display_client(self, client: object) -> None:
        """Method to display a client

        Arguments:
            client -- object: client
        """
        print(client)

    @staticmethod
    def create_client_success() -> None:
        """Method to display a success message after the creation
        of a client.
        """
        print("Le client a été crée avec succés.")

    @staticmethod
    def create_client_failed() -> None:
        """Method to display a failed message after tried
        to create a client.
        """
        print("Le client n'a pas pu être crée.")

    @staticmethod
    def update_client_success() -> None:
        """Method to display a success message after
        the update of a client.
        """
        print("Le client a bien été mis à jour.")

    @staticmethod
    def update_client_failed() -> None:
        """Method to display a failed message after tried
        to update a client.
        """
        print("Le client n'a pas pu être mis à jour.")

    @staticmethod
    def client_not_exist() -> None:
        """Method to display a message that is none client
        of this id in database.
        """
        print("Le client n'existe pas.")

    @staticmethod
    def none_clients() -> None:
        """Method to display a message that is none clients
        actually in database.
        """
        print("Aucuns client en base de donnée.")
