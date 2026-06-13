'''
FILE HANDLING:
-------------
---------->>>>file handler is an object of file to maintain several function of file like,creating,reading,updating and deleting the file.

open a file:
-------
1.open()
2.with open()


modes:
-----
--->>
  'r'-->>is used to reading the file,error if file doesnot exist..
  'a'-->>is used to add the text into file,if file doesnot exist..
not exist...
'w'-->>is used to add the text into file but it will override of all text inside file.if the file does not exist it will create with that name.
'x'-->>used to create the file.
'r'-->>mode to create.

method:
------
write()
read()
---->>this method can read entire file chunk by chunk where we can specify the side.
readline()
readlines()

any_=open('karthi.txt','r')
print(any_.read())
any_.close()

any_=open('karthi.txt','r')
print(any_.readlines())
any_.close()
'''
class ATM:
    def __init__(self, balance=1000):
        self.balance = balance
        self.pin = "2817"

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: ₹"))
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def menu(self):
        if not self.check_pin():
            print("Invalid PIN.")
            return

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option. Try again.")


atm = ATM()
atm.menu()
