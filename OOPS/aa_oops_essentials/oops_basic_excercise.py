class Employees:
    # Class Attributes/Variables
    vacation_very_week = 2

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, base_sal, bonus_percentage, employment_year, retirement_fund_percentage, first_name, last_name):
        # self.base_sal = ""
        # self.bonus_percentage = ""
        # self.employment_year = ""
        # self.retirement_fund_percentage = ""
        # self.first_name = ""
        # self.last_name = ""
        # self.vacation_hrs = ""
        # self.tot_retirement_fund = ""
        # self.company_retirement_fund_percentage = ""

        self.base_sal = base_sal
        self.bonus_percentage = bonus_percentage
        self.employment_year = employment_year
        self.retirement_fund_percentage = retirement_fund_percentage
        self.first_name = first_name
        self.last_name = last_name
        # self.vacation_hrs = vacation_hrs
        # self.tot_retirement_fund = tot_retirement_fund
        # self.company_retirement_fund_percentage = company_retirement_fund_percentage

    #  Methods
    def calc_bonus(self):
        return (self.bonus_percentage / 100) * self.base_sal

    def calc_vacation(self):
        if self.employment_year >= 1 and self.employment_year < 2:
            vacation_hrs = 52 * 2 + ((52 * 2) * 10) / 100
        elif self.employment_year >= 2 and self.employment_year < 3:
            vacation_hrs = 52 * 2 + ((52 * 2) * 20) / 100
        elif self.employment_year >= 3 and self.employment_year < 4:
            vacation_hrs = 52 * 2 + ((52 * 2) * 30) / 100
        elif self.employment_year >= 4 and self.employment_year < 5:
            vacation_hrs = 52 * 2 + ((52 * 2) * 40) / 100
        elif self.employment_year >= 5:
            vacation_hrs = 52 * 2 + ((52 * 2) * 50) / 100
        else:
            vacation_hrs = "Invalid number of years "
        return vacation_hrs

    def calc_fund_contribution(self):
        if self.retirement_fund_percentage > 5:
            self.company_retirement_fund_percentage = 5
        else:
            self.company_retirement_fund_percentage = self.retirement_fund_percentage / 2

        tot_retirement_fund = ((self.retirement_fund_percentage / 100) * self.base_sal) + ((
                                                                                                   self.company_retirement_fund_percentage / 100) * self.base_sal)
        return tot_retirement_fund


def main():
    emp1 = Employees(100000, 12, 2, 10, "Saurabh", "Wasule")

    # Values
    # emp1.first_name = input("Enter the employee's first name: ")
    # emp1.last_name = input("Enter the employee's last name: ")
    # emp1.base_sal = input("Enter the base annual salary: ")
    # emp1.bonus_percentage = int(input("Enter bonus percentage: "))
    # emp1.employment_year = int(input("Enter number of years of employment: "))
    # emp1.retirement_fund_percentage = int(input("Enter  the retirement contribution percentage : "))
    print(("Report:" + emp1.first_name + "  " + emp1.last_name).center(50, '-'))

    print("Bonus : {:.2f}".format(emp1.calc_bonus()))
    print("Vacation Hours :{:.2f}".format(emp1.calc_vacation()))
    print("Retirement Fund Contribution :{:.2f}".format(emp1.calc_fund_contribution()))


if __name__ == "__main__":
    main()
