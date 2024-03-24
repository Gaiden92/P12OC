class CollaboratorView:
    """A class representing the view for a class Collaborator"""

    def login_success(self, token: str) -> None:
        print("Vous êtes à présent connecté. Voici votre token (valable 5 minutes):")
        print(token)

    def login_failed(self) -> None:
        print("Le mot de passe est erroné.")

    def collaborator_not_exist(self) -> None:
        print("Le collaborateur n'existe pas.")

    def none_collaborators(self) -> None:
        print("Aucuns collaborateurs en base de donnée")

    def create_collaborator(
        self, name: str, contact: str, password: str, department_id: int
    ):
        """Method to create a collaborator

        Arguments:
            name -- name collaborator
            contact -- contact collabroator
            password -- str: password collaborator
            department_id -- int: departmend_id
        """
        return name, contact, password, department_id

    def get_collaborator_by_id(self, token: str) -> str:
        """Method to select a collaborator by id

        Arguments:
            token -- token user
        """
        return token

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

    def update_collaborator_name_success(self) -> None:
        """Method to display message success of collaborator's name update

        Arguments:
            collaborator -- object: collaborator
        """
        print("Le collaborateur a bien été mis à jour")

    def update_collaborator_name_failed(self) -> None:
        """Method to display message success of collaborator's name update

        Arguments:
            collaborator -- object: collaborator
        """
        print("La mise à jour du nom de collaborateur a échoué")

    @staticmethod
    def create_collaborator_success():
        print("Le collaborateur a été crée avec succès.")

    @staticmethod
    def create_collaborator_failed():
        print("Echec de la création du nouveau collaborateur.")

    @staticmethod
    def delete_collaborator_success():
        print("Le collaborateur a bien été supprimé.")

    @staticmethod
    def delete_collaborator_failed():
        print("Le collaborateur n'a pas pu être supprimé.")
