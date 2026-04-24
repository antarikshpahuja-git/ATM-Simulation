from accounts import *

def check_statement():
    unique_idd = int(input("Enter your Unique Identity  : "))
    
    if unique_idd in userIds:
        i = userIds.index(unique_idd)
        print(f"Greetings Mr. {userName[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == userPins[i]:
            print("\n---- Bank Statement ---")
            
            
            user_history = transactions[i]
            
           
            if len(user_history) == 0:
                print("No Previous transactions Done.")
            else:
               
                for record in user_history:
                    print(record)
            
            print(f"----------------------")
            print(f"Current Balance is : ₹{balances[i]}\n")
            
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique Identity.")