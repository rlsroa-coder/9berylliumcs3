#This is where we create the class BankAccount
class BankAccount:
    #this is where we define the variables for the class
    def __init__(self, account_number, balance):
        self.__account_number = account_number #creating account number variable
        self.__balance = balance #creating balance variable

    #this is where we define the methods for the class
    #this specific method is used to set the account number for the bank account
    def set_account_number(self, account_number):
        if len(account_number) !=5:   #i made this because the characters in the account number must be equal to 5
            print("Account number invalid") #the display message for error
        else:
            self.__account_number = account_number #if it does not violate the argument, it will proceed to define account number

    #this specific method is used to set the balance for the bank account
    def set_balance(self, balance):
        print("Update balance to", balance) #print the balance
        if balance < 0:   #the balance must not be negative
            print("Balance must not be a negative number") #the display message for error
        else:
            self.__balance = balance #if it does not violate the argument, it will proceed to define account number
    
    #the @property decorator is used to define getter methods for the account number and balance attributes
    @property
    def account_number(self):
        return self.__account_number  #getting the variable. using this specific formatting because the variables are private

    @property
    def balance(self):
        return self.__balance #getting the variable. using this specific formatting because the variables are private

#these are the values from the sample output
a1 = BankAccount("12345", 1000)   #the account number and the balance
print("Account Number:", a1.account_number) #displaying the account number
print("Balance:", f"{a1.balance:.2f}") #displaying the balance. i used .2f because it makes the value have 2 decimal places

print(a1.set_balance(-100))  # This will print an error message
  
  
#Sir ok na po
