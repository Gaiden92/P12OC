import tableprint as tp


class ClientView:
    """A class representing the view for a class Client"""

    def display_all_clients(self, clients: list) -> None:
        """Method to display all clients

        Arguments:
            clients -- list: clients
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers,[15,30]))
        for client in clients:
            print(tp.row( ["Nom complet", client.name_client], [15,30]))
            print(tp.row(["Email", client.email], [15,30]))
            print(tp.row(["Phone", client.phone], [15,30]))
            print(tp.row(["Create date", str(client.creation_date)], [15,30]))
            print(tp.row(["Update date", str(client.update_date)], [15,30]))
            print(tp.row(["Company", client.company.name_company], [15,30]))
            print(tp.row(["Commmercial", client.commercial.name_collaborator], [15,30]))
            print("-"*52)
        print(tp.bottom(2, [15,30]))

    def display_client(self, client: object) -> None:
        """Method to display a client

        Arguments:
            client -- object: client
        """
        headers = ["Informations", "Valeurs"]
        print(tp.header(headers,[30,30]))
        print(tp.row( ["Nom complet", client.name_client], 30))
        print(tp.row(["Email", client.email], 30))
        print(tp.row(["Phone", client.phone], 30))
        print(tp.row(["Create date", str(client.creation_date)], 30))
        print(tp.row(["Update date", str(client.update_date)], 30))
        print(tp.row(["Company", client.company.name_company], 30))
        print(tp.row(["Commercial", client.commercial.name_collaborator], 30))
        print(tp.bottom(2, [30,30]))

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

    @staticmethod
    def not_permission_client() -> None:
        """Method to display a message that the user
        has not the permission to add or update a client.
        """
        print("Vous n'avez pas les droits nécessaires pour ajouter ou modifier un client")

    @staticmethod
    def not_permission_commercial_client():
        """Method to display a message that the user
        has not the permission to add or update a client.
        """
        print("Vous n'êtes pas le commercial du client")

    @staticmethod
    def email_invalid():
        """Method to check if an email is valid
        """
        print("L'email est invalide.")