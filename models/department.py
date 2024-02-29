from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Department(Base):
    """A class represent of the department table

    Arguments:
        Base -- object: declarative_base class
    """

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_department = Column(String, unique=True)

    collaborators = relationship("Collaborator", back_populates='department')
