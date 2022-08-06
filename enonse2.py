n=input("Enter an integer: ")
try:
    int(n)
    if int(n)%4==0:
        print("NOK")
    else:
        print("OK")
except ValueError:
    print("The value enterd is not an integer")

