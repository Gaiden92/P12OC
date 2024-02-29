from sqlalchemy import select
from models.collaborator import Collaborator


class CollaboratorDao:
    """A class represents the collaborator table
    """
    def __init__(self, Session:object) -> None:
        """Constructor of CollaboratorDao class

        Arguments:
            Session -- object: an session object
        """
        self.session = Session()
        self.query = self.session.query(Collaborator)

    def select_all_collaborators(self) -> list:
        """A method for select all collaborators in database 

        Returns:
            None or list of Collaborator object: 
        """
        collaborators = self.query.all()
        if collaborators:
            return collaborators
        else:
            None

    def select_collaborator_by_id(self, collaborator_search:int) -> object:
        """Method to get collaborator by id

        Arguments:
            collaborator_search -- int: id of a collaborator

        Returns:
            object or None
        """
        collaborator = self.query.filter(Collaborator.id==collaborator_search).first()
        if collaborator:
            return collaborator
        else:
            return None

    def select_collaborator_by_name(self, collaborator_search:str) -> object:
        """Method to get collaborator by name

        Arguments:
            collaborator_search -- str: name of a collaborator

        Returns:
            object or None
        """
        collaborator = self.query.filter(Collaborator.name_collaborator==collaborator_search).first()
        if collaborator:
            return collaborator
        else:
            return None
    
    def create_collaborator(self, name: str, contact:str, password:str, department_id:int) -> bool:
        """Method to insert new collaborator in database.

        Arguments:
            name -- str: the name of the new collaborator to add.

        Returns:
            bool
        """
        collaborator = Collaborator(
            name_collaborator=name,
            contact=contact,
            password_hash=password,
            department_id=department_id)
        collaborator.set_password(password)
        try:
            self.session.add(collaborator)
            self.session.commit()
        except Exception as ex:
            return False
        return True
    
    def update_name_collaborator_by_id(self, id_collaborator:int, new_name:str) -> bool:
        """Method to update a collaborator by his id.

        Arguments:
            id_collaborator -- int: the id of the collaborator to update
            new_name -- str: the new name of the collaborator 

        Returns:
            bool
        """
        collaborator_to_update = self.query.get(id_collaborator)
        if collaborator_to_update:
            collaborator_to_update.name_collaborator = new_name
            self.session.commit()
            return True
        else:
            return False
        