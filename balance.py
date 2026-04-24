from accounts import *

def show_bal():
    unique_idd = int(input("Enter your Unique Identity : "))
    
    if unique_idd in userIds:
        i = userIds.index(unique_idd)
        print(f"Greetings Mr. {userName[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == userPins[i]:
            balancee = balances[i]
            print(f"Available Balance in your account is : ₹{balancee}")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique Identity.")