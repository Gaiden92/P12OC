from dao.department_dao import DepartmentDao
from config.parameters import GESTION, COMMERCIAL, SUPPORT


class Permission:
    """A represesentation Class of a permission
    """
    def __init__(self, user: object) -> None:
        """Constructor of Permission class

        Arguments:
            user -- object: the current user object
        """
        self.user = user
        self.department_dao = DepartmentDao()

    def isSupportDepartment(self) -> bool:
        """Function to check if the user is a collaborator
        of support department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(
            self.user.rights)
        return department.name_department.lower() == SUPPORT

    def isCommercialDepartment(self) -> bool:
        """Function to check if the user is a collaborator
        of commercial department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(
            self.user.rights)
        print(department)
        return department.name_department.lower() == COMMERCIAL

    def isGestionDepartment(self) -> bool:
        """Function to check if the user is a collaborator
        of gestion department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(
            self.user.rights)
        return department.name_department.lower() == GESTION

    def isCommercialOfContract(self, contract: object) -> bool:
        """Function to check if the user is the contract commercial

        Arguments:
            user -- object: User
            contract -- object: Contract
        Returns:
            bool
        """
        return self.user.id == contract.client.commercial_id

    def isCommercialOfClient(self, client: object) -> bool:
        """Function to check if the user is the client commercial

        Arguments:
            user -- object: User
            client -- object: client
        Returns:
            bool
        """
        return self.user.id == client.commercial_id

    def isCommercialOfEvent(self, event: object) -> bool:
        """Function to check if the user is the client commercial
            of the event
        Arguments:
            user -- object: User
            event -- object: event
        Returns:
            bool
        """

    def isSupportOfEvent(self, event: object):
        """Function to check if the user is the event support

        Arguments:
            user -- object: User
            event -- object: Event
        Returns:
            bool
        """
        return self.user.id == event.support_id
