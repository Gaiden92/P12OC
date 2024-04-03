from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, Float
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

    total_amount = Column(Float)
    remaining_amount = Column(Float)
    creation_date = Column(Date)
    status = Column(Boolean, default=True)

    event = relationship("Event", back_populates="contract")
