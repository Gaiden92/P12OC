from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Company(Base):
    """A class represent of the company table

    Arguments:
        Base -- object: declarative_base class
    """

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_company = Column(String, unique=True)
    client = relationship("Client", back_populates="company")
