import bcrypt

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Collaborator(Base):

    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_collaborator = Column(String, unique=True)
    contact = Column(String)
    # mot de passe
    password_hash = Column(String)
    salt = Column(String)

    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="collaborators")
    contracts = relationship('Contract', back_populates='collaborators')

    events = relationship('Event', back_populates='collaborators')

    # Vérification mot de passe
    def set_password(self, password: str):
        """Method to set a password

        Arguments:
            password -- str: a password
        """
        self.salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), self.salt)

    def check_password(self, password: str) -> bool:
        """Method for check if password is correct

        Arguments:
            password -- str: password

        Returns:
            bool
        """
        if bcrypt.checkpw(password.encode("utf-8"), self.password_hash):
            return True
        else:
            return False
