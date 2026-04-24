from accounts import *

def deposits():
    unique_idd = int(input("Enter your Unique Identity : "))
    
    # Check if the ID exists in the list
    if unique_idd in userIds:
        # Get the exact index of the user
        i = userIds.index(unique_idd)
        print(f"Welcome Mr. {userName[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        # Check the PIN at that exact same index
        if unique_pinn == userPins[i]:
            depo = int(input("Enter the amount to be  deposited : "))
            balances[i] += depo
            transactions[i].append(f"Deposited: +₹{depo}")

            print(f"The amount of {depo} has been deposited to your account Successfully .")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique Identity.")