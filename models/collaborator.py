import bcrypt

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from models.event import Event
from models.client import Client
from models.department import Department

class Collaborator(Base):

    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_collaborator = Column(String, unique=True)
    contact = Column(String)
    # mot de passe
    password_hash = Column(String)

    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="collaborators")
    event = relationship("Event", back_populates="support")
    client = relationship('Client', back_populates="commercial")

    # Vérification mot de passe
    def set_password(self, password: str):
        """Method to set a password

        Arguments:
            password -- str: a password
        """
        salt = bcrypt.gensalt()
        password_hash_bytes = bcrypt.hashpw(password.encode("utf-8"), salt)
        self.password_hash = password_hash_bytes.decode("utf-8")

    def check_password(self, password: str) -> bool:
        """Method for check if password is correct

        Arguments:
            password -- str: password

        Returns:
            bool
        """

        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )
