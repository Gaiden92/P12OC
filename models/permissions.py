from dao.department_dao import DepartmentDao
from config.parameters import GESTION, COMMERCIAL, SUPPORT

class Permission:
    def __init__(self, user) -> None:
        self.user = user
        self.department_dao = DepartmentDao()

    def isSupportDepartment(self) -> bool:
        """Function to check if the user is a collaborator of support department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(self.user.rights)
        return department.name_department == SUPPORT


    def isCommercialDepartment(self) -> bool:
        """Function to check if the user is a collaborator of commercial department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(self.user.rights)
        return department.name_department == COMMERCIAL


    def isGestionDepartment(self) -> bool:
        """Function to check if the user is a collaborator of gestion department

        Arguments:
            user -- object: User

        Returns:
            bool
        """
        department = self.department_dao.select_department_by_id(self.user.rights)
        return department.name_department == GESTION


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
