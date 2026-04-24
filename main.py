from deposit import *
from withdraw import *
from balance import *
from accounts import*
from transaction import*
print("Hello , Welcome to ATM Simulation")

while True:
    
    print("Withdraw Cash --> [1]")
    print("Check Balance --> [2]")
    print("Deposit Money --> [3]")
    print("Check Bank Statements --> [4]")
    print("Exit ATM --> [5]")

    response=int(input("Enter Your Choice : "))

    
    if response == 1:
        with_draw()
    elif response == 2:
        show_bal()
    elif response == 3:
        deposits()
        
    elif response == 4:
        check_statement()
    elif response==5:
        print("Thanks for Visiting .")
        break

    else:
        print("Please Enter a valid input between numbers 1-5")
