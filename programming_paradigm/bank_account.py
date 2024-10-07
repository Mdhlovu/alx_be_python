class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  

    def deposit(self, money):
        if money > 0:
            self.__account_balance += money 
        else:
            print("please deposit money.")

    def withdraw(self, money):
        if money <= self.__account_balance:
            self.__account_balance -=money 
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

