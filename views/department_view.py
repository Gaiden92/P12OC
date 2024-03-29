from tableprint import table
import tableprint as tp


class DepartmentView:
    """A class representing the view for a class Department"""

    def display_all_departments(self, departments: list) -> None:
        """Method to diplay all departments

        Arguments:
            departments -- list: departments
        """
        data = []
        for department in departments:
            data.append(
            
                (department.id,
                 department.name_department,
                 ', '.join(
                     [collaborator.name_collaborator for collaborator in department.collaborators])
                    )
            
            )
            
        table(data, ['Id', "Departments", "Collaborators"])

        


    def display_department(self, department: object) -> None:
        """Method to display one department.

        Arguments:
            department -- object: department
        """
        data = [
            
                (department.id,
                 department.name_department,
                 ', '.join(
                     [collaborator.name_collaborator for collaborator in department.collaborators])
                    )
            
        ]

        table(data, ['Id', "Departments", "Collaborators"])

    @staticmethod
    def update_success() -> None:
        """Method to display a success message after
        the update of a department.
        """
        print("Le département a bien été mis à jour.")

    @staticmethod
    def update_failed() -> None:
        """Method to display a failed message after tried
        to update a department.
        """
        print("Le département n'a pas pu être mis à jour.")

    @staticmethod
    def department_not_exist() -> None:
        """Method to display a message that is none department
        of this id in database.
        """
        print("Le département n'existe pas.")

    @staticmethod
    def none_departments() -> None:
        """Method to display a message that is none departments
        actually in database.
        """
        print("Aucuns départements en base de donnée")

    @staticmethod
    def create_department_success() -> None:
        """Method to display a success message after the creation
        of a department.
        """
        print("Le department a été crée avec succès")

    @staticmethod
    def create_department_failed() -> None:
        """Method to display a failed message after tried
        to create a department.
        """
        print("La création du départment a échoué")

    @staticmethod
    def delete_department_success() -> None:
        """Method to display a success message after
        the creation of a department.
        """
        print("Le départment a bien été supprimé.")

    @staticmethod
    def delete_department_failed() -> None:
        """Method to display a failed message after
        tried to create a department.
        """
        print("Le départment n'a pas pu être supprimé.")
