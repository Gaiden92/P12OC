from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from models.company import Company


class Client(Base):
    """A class represent of the client table

    Arguments:
        Base -- object: declarative_base class
    """

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_client = Column(String)
    email = Column(String)
    phone = Column(String)
    creation_date = Column(Date)
    update_date = Column(Date)

    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="client")

    commercial_id = Column(Integer, ForeignKey("collaborators.id"))
    contract = relationship("Contract", back_populates="client")
