#Parent Class: User
#Holds details about a user
#Has a function to show user details
#Child class: Bank
#Stores details about the account balance
#Stores details about the amount 
#Allows for deposits, Withdraw, view_balance

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
# johan = User('Johan', 21, 'Male')
# johan.show_details()

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : UGX", self.balance)
# johan = Bank('Johan', 21, 'Male')
# johan.deposit(100)
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : UGX", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: UGx", self.balance)
# johan = Bank('Johan', 21, 'Male')
# johan.deposit(100)
# johan.withdraw(50)
# johan.withdraw(100)
    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: UGx", self.balance)
# johan = Bank('Johan', 21, 'Male')
# johan.deposit(1000)
# johan.withdraw(100)
# johan.view_balance()


