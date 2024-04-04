import tableprint as tp


class DepartmentView:
    """A class representing the view for a class Department"""

    def display_all_departments(self, departments: list) -> None:
        """Method to diplay all departments

        Arguments:
            departments -- list: departments
        """
        header = tp.header(['Id', 'Department', "Collaborators"], 20)
        bottom = tp.bottom(3, 20)
        print(header)
        for department in departments:
            if department.collaborators:
                for i in range(len(department.collaborators)):
                    if i == 0:
                        print(tp.row(
                            [
                                department.id,
                                department.name_department,
                                department.collaborators[i].name_collaborator
                                ], 20))
                    else:
                        print(tp.row(
                            [
                                "",
                                "",
                                department.collaborators[i].name_collaborator
                                ], 20))
            else:
                print(tp.row(
                    [
                        department.id,
                        department.name_department,
                        "not collaborators yet"], 20))

        print(bottom)

    @staticmethod
    def not_permission() -> None:
        """Method to display a failed message if the
        collaborator are not the permission.
        """
        print("You are not the permission to perform this action.")

    def display_department(self, department: object) -> None:
        """Method to display one department.

        Arguments:
            department -- object: department
        """
        header = tp.header(['Id', 'Department', "Collaborators"], 20)
        bottom = tp.bottom(3, 20)
        print(header)
        if department.collaborators:
            for i in range(len(department.collaborators)):
                if i == 0:
                    print(tp.row(
                        [
                            department.id,
                            department.name_department,
                            department.collaborators[i].name_collaborator
                            ], 20))
                else:
                    print(tp.row(
                        [
                            "",
                            "",
                            department.collaborators[i].name_collaborator
                            ], 20))
        else:
            print(tp.row(
                [
                    department.id,
                    department.name_department,
                    "not collaborators yet"], 20))

        print(bottom)

    @staticmethod
    def update_success() -> None:
        """Method to display a success message after
        the update of a department.
        """
        print("The department update has been success.")

    @staticmethod
    def update_failed() -> None:
        """Method to display a failed message after tried
        to update a department.
        """
        print("The department update has failed.")

    @staticmethod
    def department_not_exist() -> None:
        """Method to display a message that is none department
        of this id in database.
        """
        print("This department doesn't exist.")

    @staticmethod
    def none_departments() -> None:
        """Method to display a message that is none departments
        actually in database.
        """
        print("None department in database.")

    @staticmethod
    def create_department_success() -> None:
        """Method to display a success message after the creation
        of a department.
        """
        print("Success creation department.")

    @staticmethod
    def create_department_failed() -> None:
        """Method to display a failed message after tried
        to create a department.
        """
        print("Failed creation department.")

    @staticmethod
    def delete_department_success() -> None:
        """Method to display a success message after
        the creation of a department.
        """
        print("Success delete department.")

    @staticmethod
    def delete_department_failed() -> None:
        """Method to display a failed message after
        tried to create a department.
        """
        print("Failed delete department.")
