from dao.department_dao import DepartmentDao
from config.parameters import GESTION, COMMERCIAL, SUPPORT


def isSupportDepartment(user: object) -> bool:
    """Function to check if the user is a collaborator of support department

    Arguments:
        user -- object: User

    Returns:
        bool
    """
    department = DepartmentDao().select_department_by_id(user.rights)
    return department.name_department == SUPPORT


def isCommercialDepartment(user: object) -> bool:
    """Function to check if the user is a collaborator of commercial department

    Arguments:
        user -- object: User

    Returns:
        bool
    """
    department = DepartmentDao().select_department_by_id(user.rights)
    return department.name_department == COMMERCIAL


def isGestionDepartment(user: object) -> bool:
    """Function to check if the user is a collaborator of gestion department

    Arguments:
        user -- object: User

    Returns:
        bool
    """
    department = DepartmentDao().select_department_by_id(user.rights)
    return department.name_department == GESTION


def isCommercialofContract(user: object, contract: object) -> bool:
    """Function to check if the user is the contract commercial

    Arguments:
        user -- object: User
        contract -- object: Contract
    Returns:
        bool
    """
    return user.id == contract.collaborator_id


def isSupportOfEvent(user: object, event: object):
    """Function to check if the user is the event support

    Arguments:
        user -- object: User
        event -- object: Event
    Returns:
        bool
    """
    return user.id == event.collaborator_id
