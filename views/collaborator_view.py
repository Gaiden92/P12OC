class CollaboratorView:
    """A class representing the view for a class Collaborator"""

    def login_success(self, token: str) -> None:
        """Method to display the user token and a success message.
        """
        print("Vous êtes connecté. Votre token (valable 5 minutes):")
        print(token)

    def login_failed(self) -> None:
        """Method to display a message that the password is invalid.
        """
        print("Le mot de passe est erroné.")

    def collaborator_not_exist(self) -> None:
        """Method to display a message that is none collaborator
        of this id in database.
        """
        print("Le collaborateur n'existe pas.")

    def none_collaborators(self) -> None:
        """Method to display a message that is none collaborators
        actually in database.
        """
        print("Aucuns collaborateurs en base de donnée")

    def display_all_collaborators(self, collaborators: list) -> None:
        """Method to display all collaborators

        Arguments:
            collaborators -- list: collaborators
        """
        print(collaborators)

    def display_collaborator(self, collaborator: object) -> None:
        """Method to display a collaborator

        Arguments:
            collaborator -- object: collaborator
        """
        print(collaborator)

    def update_collaborator_success(self) -> None:
        """Method to display message success of collaborator update

        Arguments:
            collaborator -- object: collaborator
        """
        print("Le collaborateur a bien été mis à jour")

    def update_collaborator_failed(self) -> None:
        """Method to display message success of collaborator update

        Arguments:
            collaborator -- object: collaborator
        """
        print("La mise à jour du nom de collaborateur a échoué")

    @staticmethod
    def create_collaborator_success() -> None:
        """Method to display a success message after the creation
        of a collaborator.
        """
        print("Le collaborateur a été crée avec succès.")

    @staticmethod
    def create_collaborator_failed() -> None:
        """Method to display a failed message after tried
        to create a collaborator.
        """
        print("Echec de la création du nouveau collaborateur.")

    @staticmethod
    def delete_collaborator_success() -> None:
        """Method to display a success message after
        the creation of a collaborator.
        """
        print("Le collaborateur a bien été supprimé.")

    @staticmethod
    def delete_collaborator_failed() -> None:
        """Method to display a failed message after
        tried to create a collaborator.
        """
        print("Le collaborateur n'a pas pu être supprimé.")
