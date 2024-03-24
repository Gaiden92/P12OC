class ClientView:
    """A class representing the view for a class Client"""

    def display_client(self, client: object) -> None:
        print(client)

    def display_all_clients(self, clients: list) -> None:
        print(clients)

    @staticmethod
    def update_client_success():
        print("Le client a bien été mis à jour.")

    @staticmethod
    def update_client_failed():
        print("Le client n'a pas pu être mis à jour.")

    @staticmethod
    def client_not_exist() -> None:
        print("Le client n'existe pas.")

    @staticmethod
    def none_clients() -> None:
        print("Aucuns client en base de donnée.")

    @staticmethod
    def create_client_success() -> None:
        print("Le client a été crée avec succés.")

    @staticmethod
    def create_client_failed() -> None:
        print("Le client n'a pas pu être crée.")
