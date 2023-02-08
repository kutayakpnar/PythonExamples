print("""
*********User Login************
""")

sys_nickname = "kutay"
sys_password="akpınar"
rightofentry=3
while True:
    a=input("Please enter your nickname:")
    b=input("Please enter your password:")
    if (a==sys_nickname and b==sys_password):
        print("Entry is succesfull.")
        break
    else:
        print("Nickname or password is wrong.Please try it again.")
        rightofentry -= 1
        if (rightofentry==0):
            print("You cannot enter.")
            break




