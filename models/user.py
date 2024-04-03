import json
import jwt
from datetime import datetime, timedelta

from config.parameters import TOKEN_PATH, DELAY


class User:
    """Class represent a User"""

    def __init__(self, user_id: int, rights: int) -> None:
        """Constructor of class User

        Arguments:
            user_id -- int: user id
            rights -- int: user rights
        """
        self.id = user_id
        self.rights = rights

    def generate_token(self) -> str:
        """Method to generate token user

        Returns:
            bool: the token user
        """
        expiration_time = datetime.utcnow() + timedelta(minutes=DELAY)

        payload = {
            "user_id": self.id,
            "rights": self.rights,
            "exp": expiration_time}
        return jwt.encode(payload, algorithm="HS256", key="maclesecrete")

    def register_info(self):
        """Method to regist information user"""
        with open(TOKEN_PATH, "w") as file:
            json.dump(
                {
                    "user_id": self.id,
                    "rights": self.rights,
                },
                file,
            )

    @staticmethod
    def load_user() -> object:
        """Method to load user file

        Returns:
            object: user
        """
        with open(TOKEN_PATH, "r") as file:
            data = json.load(file)
            return User(data["user_id"], data["rights"])
