from sqlalchemy import select
from models.department import Department


class DepartmentDao:
    """A class represents the department table
    """
    def __init__(self, Session:object) -> None:
        """Constructor of DepartmentDao class

        Arguments:
            Session -- object: an session object
        """
        self.session = Session()
        self.query = self.session.query(Department)

    def select_all_departments(self) -> list:
        """A method for select all departments in database 

        Returns:
            None or list of Department object: 
        """
        departments = self.query.all()
        if departments:
            return departments
        else:
            None

    def select_department_by_id(self, department_id:int) -> object:
        """Method to get department by id

        Arguments:
            department_id -- int: id of a department

        Returns:
            object or None
        """
        department = self.query.filter(Department.id==department_id).first()
        if department:
            return department
        else:
            return None

    def select_department_by_name(self, department_search:str) -> object:
        """Method to get department by name

        Arguments:
            department_search -- str: name of a department

        Returns:
            object or None
        """
        department = self.query.filter(Department.name_department==department_search).first()
        if department:
            return department
        else:
            return None
    
    def create_department(self, name: str) -> bool:
        """Method to insert new department in database.

        Arguments:
            name -- str: the name of the new department to add.

        Returns:
            bool
        """
        department = Department(name_department=name)
        try:
            self.session.add(department)
            self.session.commit()
        except Exception as ex:
            return False
        return True
    
    def update_name_department_by_id(self, id_department:int, new_name:str) -> bool:
        """Method to update a department by his id.

        Arguments:
            id_department -- int: the id of the department to update
            new_name -- str: the new name of the department 

        Returns:
            bool
        """
        department_to_update = self.query.get(id_department)
        if department_to_update:
            department_to_update.name_department = new_name
            self.session.commit()
            return True
        else:
            return False
        