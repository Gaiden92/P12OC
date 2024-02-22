from sqlalchemy import Column, Integer, Date, String, ForeignKey, Boolean

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name_department = Column(String, index=True)


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name_compagny = Column(String, unique=True, index=True)


class Collaborator(Base):
    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    password = Column(String)
    name_collaborator = Column(String, unique=True, index=True)
    contact = Column(String, index=True)
    department_id = Column(Integer, ForeignKey('departments.id'))


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name_client = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    creation_date = Column(Date, index=True)
    update_date = Column(Date, index=True)
    collaborator_id = Column(Integer, ForeignKey('collaborators.id'))
    name_compagny_id = Column(Integer, ForeignKey('companies.id'))


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    collaborator_id = Column(Integer, ForeignKey('collaborators.id'))
    total_amount = Column(Integer, index=True)
    remaining_amount = Column(Integer, index=True)
    creation_date = Column(Date, index=True)
    status = Column(Boolean, default=True)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    collaborator_id = Column(Integer, ForeignKey("collaborators.id"))
    location = Column(String, index=True)
    participants = Column(Integer, index=True)
    notes = Column(String, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
