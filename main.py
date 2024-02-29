from config.database import Database
from config.parameters import  DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA

from dao.collaborator_dao import CollaboratorDao
from dao.department_dao import DepartmentDao
from dao.company_dao import CompanyDao
from dao.client_dao import ClientDao

from models.collaborator import Collaborator
from models.client import Client
from models.company import Company
from models.contract import Contract
from models.department import Department
from models.event import Event

db = Database(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA)

