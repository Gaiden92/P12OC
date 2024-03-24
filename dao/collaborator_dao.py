from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from models.collaborator import Collaborator
from config.parameters import DB


class CollaboratorDao:
    """A class represent the collaborator table"""

    def __init__(self) -> None:
        """Constructor of CollaboratorDao class"""
        self.db = DB
        self.session = self.db.session()
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

    def select_collaborator_by_id(self, collaborator_id: int) -> object:
        """Method to get collaborator by id

        Arguments:
            collaborator_id -- int: id of a collaborator

        Returns:
            object or None
        """
        collaborator = self.query.filter(Collaborator.id == collaborator_id).first()
        if collaborator:
            return collaborator
        else:
            return None

    def select_collaborator_by_name(self, collaborator_name: str) -> object:
        """Method to get collaborator by name

        Arguments:
            collaborator_name -- str: name of a collaborator

        Returns:
            object or None
        """
        collaborator = self.query.filter(
            Collaborator.name_collaborator == collaborator_name
        ).first()
        if collaborator:
            return collaborator
        else:
            return None

    def select_all_collaborators_by_department_id(self, department_id: int) -> object:
        """Method to get collaborators by id department

        Arguments:
            department_id -- int: id department

        Returns:
            object or None
        """
        collaborators = self.query.filter(
            Collaborator.department_id == department_id
        ).all()

        if collaborators:
            return collaborators
        else:
            return None

    def create_collaborator(
        self, name: str, contact: str, password: str, department_id: int
    ) -> bool:
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
            department_id=department_id,
        )
        collaborator.set_password(password)
        try:
            self.session.add(collaborator)
            self.session.commit()
        except Exception as ex:
            return False
        return True

    def update_name_collaborator_by_id(
        self, id_collaborator: int, new_name: str
    ) -> bool:
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

    def update_password_by_id(self, id_collaborator: int, new_password: str):
        """Method to update a collaborator by his id.

        Arguments:
            id_collaborator -- int: the id of the collaborator to update
            new_password -- str: the new password of the collaborator

        Returns:
            bool
        """
        collaborator_to_update = self.query.get(id_collaborator)
        if collaborator_to_update:
            collaborator_to_update.set_password(new_password)

            self.session.commit()
            return True
        else:
            return False

    def delete_collaborator_by_id(self, id_collaborator: int) -> bool:
        """Method to delete a collaborator by his id.

        Arguments:
            id_collaborator -- int: id collaborator

        Returns:
            bool
        """
        collaborator_to_delete = self.query.filter(Collaborator.id == id_collaborator)
        if collaborator_to_delete:
            try:
                collaborator_to_delete.delete()
                self.session.commit()
                return True
            except IntegrityError:
                return False
        else:
            return False
