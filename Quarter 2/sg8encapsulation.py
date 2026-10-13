class BankAccount:
    #this is where we define the variables for the class
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    #this is where we define the methods for the class
    #this specific method is used to set the account number for the bank account
    def set_account_number(self, account_number):
        if len(account_number) < 5:
            print("Account number invalid")
        else:
            self.__account_number = account_number

    #this specific method is used to set the balance for the bank account
    def set_balance(self, balance):
        print("Update balance to", balance)
        if balance < 0:
            print("Balance must not be a negative number")
        else:
            self.__balance = balance
    
    #the @property decorator is used to define getter methods for the account number and balance attributes
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

a1 = BankAccount("12345", 1000)
print("Account Number:", a1.account_number)
print("Balance:", f"{a1.balance:.2f}")

print(a1.set_balance(-100))  # This will print an error message
  
  
