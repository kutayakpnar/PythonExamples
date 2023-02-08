print("""
**********ATM MACHINE***********
OPERATIONS:
1.Arrears Inquiry
2.Investment
3.Withdraval
If you want the exit from operations please enter E !
""")
arrears=1000

while True:
    a=input("Please select operation you want:")
    if (a=="E"):
        break
    elif (a == "1"):
        print("You have",arrears,"cash in your account")
    elif(a == "2"):
        x=int(input("Please enter the quantity you want to investment:"))
        arrears=x+arrears
        print("You have", arrears, "cash in your account")
    elif (a == "3"):
        x = int(input("Please enter the quantity you want to withdraval:"))
        if (arrears>=x):
            arrears -= x
            print("You have", arrears, "cash in your account")

        if (arrears<x):
            print("You dont have that much money Please try it again.")
            continue
    else:
        print("Unvalid operation.Please try again.")






