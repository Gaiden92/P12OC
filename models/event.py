from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base
from models.contract import Contract


class Event(Base):
    """A class represent of the event table

    Arguments:
        Base -- object: declarative_base class
    """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_name = Column(String)

    contract_id = Column(Integer, ForeignKey("contracts.id"))
    contract = relationship("Contract", back_populates="event")

    support_id = Column(Integer, ForeignKey("collaborators.id"))
    support = relationship("Collaborator", back_populates="event")

    location = Column(String)
    participants = Column(Integer)
    notes = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
