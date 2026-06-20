'''
ATM Code
---------
'''
user_information = {"Name" : "ABCD",
                    "Mobile Number" : "",
                    "ATM PIN" : "1234",
                    "Balance" : 50000,
                    "Transaction History" : []
                    }
print("Please insert your ATM card")
remaining_attempts = 3
while remaining_attempts > 0:
    user_pin = input("Enter your ATM pin: ")
    if len(user_pin) == 4:
        if user_pin in user_information['ATM PIN']:
            print("\nLogin Successful")
            while True:
                print("\n1.Withdrawl \n2.Deposit \n3.Check Balance \n4.Exit")
                choice = int(input("Enter your choice: "))
                # Withdrawl
                if choice == 1:
                    amount = int(input("Enter Withdrawl amount: Rs"))
                    if amount <= user_information["Balance"] and amount > 0:
                        user_information["Balance"] -= amount
                        user_information["Transaction History"].append(f"Withdrawl Rs{amount}")
                        print("Please collect your Cash")
                        print("Remaining Balancde: Rs", user_information["Balance"])
                    else:
                        print("Insufficient Balance")
                # Deposit
                elif choice == 2:
                    amount = int(input("Enter Deposit amount: Rs"))
                    if amount > 0:
                        user_information["Balance"] += amount
                        user_information["Transaction History"].append(f"Deposited Rs{amount}")
                        print("Amount Deposited Successfully")
                        print("Updated Balance: Rs", user_information["Balance"])
                    else:
                        print("Invalid Amount")
                # Check Balance
                elif choice == 3:
                    print("\nTotal Balance: Rs",user_information["Balance"])
                # Exit
                elif choice == 4:
                    print("Thank You Please Visit Again... ")
                    break
                else:
                    print("Invalid Choice")
            break
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"Invalid pin entered and you have {remaining_attempts} left")
            else:
                print("Your are attempted many times, so please wait and try again")
    else:
        print("Please Enter 4 digit password: ")


    



























