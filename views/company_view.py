import tableprint as tp


class CompanyView:
    """A class representing the view for a class Company"""

    def display_all_companies(self, companies: list) -> None:
        header = tp.header(["Name Company", "Clients"], 30)
        bottom = tp.bottom(2, 30)

        print(header)
        for company in companies:
            if company.client:
                for i in range(0, len(company.client)):
                    if i == 0:
                        print(tp.row(
                            [
                                company.name_company,
                                company.client[i].name_client], 30))
                    else:
                        print(tp.row(
                            [
                                "",
                                company.client[i].name_client], 30))
            else:
                print(tp.row([company.name_company, "Not clients yet"], 30))
        print(bottom)

    def display_company(self, company: object) -> None:
        print(company)
        header = tp.header(["Name Company", "Clients"], 30)
        bottom = tp.bottom(2, 30)

        print(header)
        if company.client:
            for i in range(len(company.client)):
                if i == 0:
                    print(tp.row(
                        [
                            company.name_company,
                            company.client[i].name_client], 30))
                else:
                    print(tp.row(
                        [
                            "",
                            company.client[i].name_client], 30))
        else:
            print(tp.row([company.name_company, "not clients yet"], 30))
        print(bottom)

    @staticmethod
    def create_company_success() -> None:
        """Method to display a success message after the creation
        of a company.
        """
        print("Company creation success.")

    @staticmethod
    def create_company_failed() -> None:
        """Method to display a failed message after tried
        to create a company.
        """
        print("Company creation failed.")

    @staticmethod
    def company_not_exist() -> None:
        """Method to display a message that is none company
        of this id in database.
        """
        print("This company do not exist.")

    @staticmethod
    def none_companies() -> None:
        """Method to display a message that is none companies
        actually in database.
        """
        print("None companies in database")

    @staticmethod
    def update_company_name_success() -> None:
        """Method to display a success message after
        the update of a company.
        """
        print("L'entreprise a bien été mis à jour.")

    @staticmethod
    def update_company_name_failed() -> None:
        """Method to display a failed message after tried
        to update a company.
        """
        print("The company update failed.")

    @staticmethod
    def delete_company_success() -> None:
        """Method to display a success message after
        the creation of a company.
        """
        print("The company is now delete.")

    @staticmethod
    def delete_company_failed() -> None:
        """Method to display a failed message after
        tried to create a company.
        """
        print("The company delete has failed.")
