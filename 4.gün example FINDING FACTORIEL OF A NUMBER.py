print("""

FINDING FACTORIEL
PLEASE CLICK W IN ORDER TO EXIT!

""")
while True:
    a=input("Enter the number whose factorial you want to find:")
    if(a=="W"):
        break

    else:
        a=int(a)
        x=1
        for i in range(2,a+1):
            x = x * i

    print(x)

