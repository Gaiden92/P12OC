import tableprint as tp


class CollaboratorView:
    """A class representing the view for a class Collaborator"""

    def login_success(self, token: str) -> None:
        """Method to display the user token and a success message.
        """
        print("Vous êtes connecté. Votre token (valable 30 minutes):")
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
        headers = ['id', 'name', 'contact', 'department']
        print(tp.header(headers, 20))
        for collaborator in collaborators:
            print(tp.row(
                [
                    collaborator.id,
                    collaborator.name_collaborator,
                    collaborator.contact,
                    collaborator.department.name_department
                ],
                width=20)
                )
        print(tp.bottom(4, width=20))

    def display_collaborator(self, collaborator: object) -> None:
        """Method to display a collaborator

        Arguments:
            collaborator -- object: collaborator
        """
        headers = ['id', 'name', 'contact', 'department']
        print(tp.header(headers, 20))

        print(tp.row(
                [
                    collaborator.id,
                    collaborator.name_collaborator,
                    collaborator.contact,
                    collaborator.department.name_department
                ], width=20))
        print(tp.bottom(4, width=20))

    def update_collaborator_success(self) -> None:
        """Method to display message success of collaborator update

        Arguments:
            collaborator -- object: collaborator
        """
        print("The update has been success")

    def update_collaborator_failed(self) -> None:
        """Method to display message success of collaborator update

        Arguments:
            collaborator -- object: collaborator
        """
        print("The update has not work.")

    @staticmethod
    def create_collaborator_success() -> None:
        """Method to display a success message after the creation
        of a collaborator.
        """
        print("The collaborator has been create.")

    @staticmethod
    def create_collaborator_failed() -> None:
        """Method to display a failed message after tried
        to create a collaborator.
        """
        print("Creation of a new collaborator echec.")

    @staticmethod
    def delete_collaborator_success() -> None:
        """Method to display a success message after
        the creation of a collaborator.
        """
        print("The collaborator has been delete.")

    @staticmethod
    def delete_collaborator_failed() -> None:
        """Method to display a failed message after
        tried to create a collaborator.
        """
        print("The collaborator didn't be deleted.")

    @staticmethod
    def not_permission_collaborator() -> None:
        """Method to display a failed message after
        tried to create a collaborator if not permission.
        """
        print("You don't have the permission to create a new collaborator.")
