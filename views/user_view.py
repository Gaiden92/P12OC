class UserView:

    def login_view(id: int, password: str):
        """Method to login to the CRM"""
        return id, password

    @staticmethod
    def token_expired():
        """Method to display message expired token"""
        print("Token expiré. Merci de vous reconnecter.")

    @staticmethod
    def token_invalid():
        """Method to display message invalid token"""
        print("Token invalide. Merci de réessayer.")

    @staticmethod
    def token_succes():
        """Method to display message succes token"""
        print("Token valide.")
