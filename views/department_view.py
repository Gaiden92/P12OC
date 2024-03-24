class DepartmentView:
    """A class representing the view for a class Department"""

    def display_all_departments(self, departments: list) -> None:
        print(departments)

    def display_department(self, department: object) -> None:
        print(department)

    @staticmethod
    def update_success() -> None:
        print(f"Le département a bien été mis à jour.")

    @staticmethod
    def update_failed() -> None:
        print(f"Le département n'a pas pu être mis à jour.")

    @staticmethod
    def department_not_exist():
        print("Le département n'existe pas.")

    @staticmethod
    def none_departments():
        print("Aucuns départements en base de donnée")

    @staticmethod
    def create_department_success():
        print("Le department a été crée avec succès")

    @staticmethod
    def create_department_failed():
        print("La création du départment a échoué")

    @staticmethod
    def delete_department_success():
        print("Le départment a bien été supprimé.")

    @staticmethod
    def delete_department_failed():
        print("Le départment n'a pas pu être supprimé.")
