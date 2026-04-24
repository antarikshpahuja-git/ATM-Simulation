from accounts import *

def with_draw():
    unique_idd = int(input("Enter your Unique Identity : "))
    
    if unique_idd in userIds:
        i = userIds.index(unique_idd)
        print(f"Greetings Mr. {userName[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == userPins[i]:
            withd = int(input("Enter amount to be withdrawn : "))
            
            if balances[i] >= withd:
                balances[i] -= withd
                transactions[i].append(f"Withdrawn: -₹{withd}")
                print(f"The amount of {withd} has been withdrawn from your account Successfully .")
            else:
                print("Insufficient Balance !!")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique Identity.")