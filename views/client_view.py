import tableprint as tp


class ClientView:
    """A class representing the view for a class Client"""

    def display_all_clients(self, clients: list) -> None:
        """Method to display all clients

        Arguments:
            clients -- list: clients
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers, [15, 30]))
        for client in clients:
            print(tp.row(["Full name", client.name_client], [15, 30]))
            print(tp.row(["Mail", client.email], [15, 30]))
            print(tp.row(["Phone", client.phone], [15, 30]))
            print(tp.row(["Create date", str(client.creation_date)], [15, 30]))
            print(tp.row(["Update date", str(client.update_date)], [15, 30]))
            print(tp.row(["Company", client.company.name_company], [15, 30]))
            print(tp.row([
                "Commmercial",
                client.commercial.name_collaborator], [15, 30]))
            print("-"*52)
        print(tp.bottom(2, [15, 30]))

    def display_client(self, client: object) -> None:
        """Method to display a client

        Arguments:
            client -- object: client
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers, [30, 30]))
        print(tp.row(["Full name", client.name_client], 30))
        print(tp.row(["Mail", client.email], 30))
        print(tp.row(["Phone", client.phone], 30))
        print(tp.row(["Create date", str(client.creation_date)], 30))
        print(tp.row(["Update date", str(client.update_date)], 30))
        print(tp.row(["Company", client.company.name_company], 30))
        print(tp.row([
            "Commercial",
            client.commercial.name_collaborator], 30))
        print(tp.bottom(2, [30, 30]))

    @staticmethod
    def create_client_success() -> None:
        """Method to display a success message after the creation
        of a client.
        """
        print("Success creation client.")

    @staticmethod
    def create_client_failed() -> None:
        """Method to display a failed message after tried
        to create a client.
        """
        print("Failed creation client.")

    @staticmethod
    def update_client_success() -> None:
        """Method to display a success message after
        the update of a client.
        """
        print("Success update client.")

    @staticmethod
    def update_client_failed() -> None:
        """Method to display a failed message after tried
        to update a client.
        """
        print("Failed update client.")

    @staticmethod
    def client_not_exist() -> None:
        """Method to display a message that is none client
        of this id in database.
        """
        print("This client doesn't exist.")

    @staticmethod
    def none_clients() -> None:
        """Method to display a message that is none clients
        actually in database.
        """
        print("None clients in database")

    @staticmethod
    def not_permission_client() -> None:
        """Method to display a message that the user
        has not the permission to add or update a client.
        """
        print("You don't have the permission to perform this\
              action.")

    @staticmethod
    def not_permission_commercial_client():
        """Method to display a message that the user
        has not the permission to add or update a client.
        """
        print("You don't have the permission to perform this\
              action. You're not the client commercial.")

    @staticmethod
    def email_invalid():
        """Method to check if an email is valid
        """
        print("Invalid email")
