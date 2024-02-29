from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class Contract(Base):
    """A class represent of the contract table

    Arguments:
        Base -- object: declarative_base class
    """

    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="contract")
    
    collaborator_id = Column(Integer, ForeignKey("collaborators.id"))
    collaborators = relationship("Collaborator", back_populates="contracts")

    total_amount = Column(Integer)
    remaining_amount = Column(Integer)
    creation_date = Column(Date)
    status = Column(Boolean, default=True)

    event = relationship('Event', back_populates='contract')

