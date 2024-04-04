class UserView:
    """A user view class representation.
    """
    def login_view(id: int, password: str) -> tuple:
        """Method to login to the CRM"""
        return id, password

    @staticmethod
    def token_expired() -> None:
        """Method to display message expired token"""
        print("Token expired. You must to login again.")

    @staticmethod
    def token_invalid() -> None:
        """Method to display message invalid token"""
        print("The token is not valid token. Try again.")

    @staticmethod
    def token_succes() -> None:
        """Method to display message succes token"""
        print("The token is valid.")
