class Investor():

    def __init__(self, name, savings, investment_goal_percentage):
        self.name = name
        self.savings = savings
        self.investment_goal_percentage = investment_goal_percentage


class Property():
    
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.investment = {}

    def calculate_quick_COCROI(self):
        try:
            self.income['total'] = int(input("What is your total income? "))
            self.expenses['total'] = int(input("What is your total expenses? "))
            self.investment['total'] = int(input("What is your total investment? "))
            self.monthly_profit = self.income['total'] - self.expenses['total']
            self.COCROI = ((self.monthly_profit * 12) / self.investment['total']) * 100
        except:
            print("Please input a number")
            self.calculate_quick_COCROI
        answer = input("Would you like to take the longer route to calculating your COCROI? y/n ")
        if answer == 'y':
            self.calculate__long_COCROI
        else:
            pass


    def calculate__long_COCROI(self):
        try:
            self.investment['down_payment'] = int(input("What is the down payment? "))
            self.investment['closing_cost'] = int(input("What is the closing cost? "))
            self.investment['rehab'] = int(input("What is the rehab budget? "))
            self.investment['other'] = int(input("Any other payments? "))
            self.investment['total'] = self.investment['down_payment'] + self.investment['closing_cost'] + self.investment['rehab'] + self.investment['other']
        except:
            print("Please input a number")
            self.calculate__long_COCROI
        self.calculate_Income()
        self.calculate_Expenses()

        self.monthly_profit = self.income['total'] - self.expenses['total']

        self.COCROI = ((self.monthly_profit * 12) / self.investment['total']) * 100


    def calculate_Income(self):
        try:
            self.income["rental_income"] = int(input("What is the rental income? "))
            self.income["laundry_income"] = int(input("What is the laundry income? "))
            self.income["storage_income"] = int(input("What is the storage income? "))
            self.income["other_income"] = int(input("Any other income? "))
            self.income["total"] = self.income['rental_income'] + self.income['laundry_income'] + self.income['storage_income'] + self.income['other_income']
        except:
            print("Please input a number")
            self.calculate_Income
    def calculate_Expenses(self):
        try:
            self.expenses["tax"] = int(input("What is the tax expense? "))
            self.expenses["insurance"] = int(input("What is the insurance expense? "))
            self.expenses["utilities"] = int(input("What is the utilities expense? "))
            self.expenses["HOA"] = int(input("What is the HOA expense? "))
            self.expenses["lawn"] = int(input("What is the lawn expense? "))
            self.expenses["vacancy"] = int(input("What is the vacancy expense? "))
            self.expenses["repairs"] = int(input("What is the repairs expense? "))
            self.expenses["capEX"] = int(input("What is the cpital expendatures? "))
            self.expenses["management"] = int(input("What is the management expense? "))
            self.expenses["mortgage"] = int(input("What is the mortgage expense? "))
            self.expenses['total'] = self.expenses["tax"] + self.expenses["insurance"] +  self.expenses["utilities"] +  self.expenses["HOA"] +  self.expenses['lawn'] + self.expenses["vacancy"] + self.expenses["repairs"] + self.expenses["capEX"] + self.expenses["management"] + self.expenses["mortgage"]
        except:
            print("Please input a number")
            self.calculate_Expenses

def main():
    persons = []

    Noah = Investor("Noah", 50000, 10)
    Jack = Investor("Jack", 50000, 1)
    Jimmy = Investor("Jimmy", 50000, 100)
    Jamantha = Investor("Jamantha", 5000000000, 10)
    John = Investor("John", 5, 10)

    persons.append(Noah)
    persons.append(Jack)
    persons.append(Jimmy)
    persons.append(Jamantha)
    persons.append(John)


    property1 = Property()
    property1.calculate_quick_COCROI()
    print(f'Monthly profit: {property1.monthly_profit}')
    print(f'COCROI: {property1.COCROI}')


    for investor in persons:

        if investor.savings >= property1.investment['total']:
            # if can afford property
            print(f"{investor.name}: ", end='')
            if investor.investment_goal_percentage < property1.COCROI:
                print("Worth investing")
            else:
                print("Not worth investing")
        else:
            print(f"{investor.name} cant afford this property")

main()