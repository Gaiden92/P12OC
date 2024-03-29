import jwt, os, click

from config.parameters import TOKEN_PATH
from controllers.collaborator_controller import CollaboratorController
from views.user_view import UserView


class UserController:
    """A class representing the client controller"""

    def __init__(self) -> None:
        self.view = UserView()
        self.collaborator_controller = CollaboratorController()

    def check_entry_user(self, id: int, password: str) -> any:
        """Method to check the user's entries

        Arguments:
            id -- int: the user id
            password -- str: the user password

        Returns:
            str
        """
        if not isinstance(id, int):
            return self.view.id_not_int()
        else:
            if password == "" and not isinstance(password, str):
                return self.view.password_error()
            else:
                return True

    def verify_token(self, ctx, param, token: str) -> bool:
        """
        Method to verify token
        Arguments:
            token -- str: a token

        Returns:
            bool
        """
        try:
            payload = jwt.decode(token, key="maclesecrete", algorithms="HS256")
            return token
        except jwt.ExpiredSignatureError:
            raise click.BadParameter("le token a expiré")
        except jwt.InvalidTokenError:
            raise click.BadParameter("le token est invalide")
