priceOfApple= 210
budget= 200
if(budget>=priceOfApple):
    print("Siri add apples to the cart")
else:
    print("siri do not add apples to the cart")
print()
num=int(input("Enter a number here:"))
if(num>0):
    print("Number is Positive")
elif(num==0):
    print("Number is Zero")
else:
    print("Number is negative")
print()

#Nested if statements
inp1=int(input("Enter any number here"))
if(inp1==0):
    print("The number is zero")
elif(inp1>0):
    if(inp1<=10):
        print("The number is between 0 to 10")
    elif(inp1>=10 and inp1<=20):
        print("The number is between 10 to 20")
    elif(inp1>=20 and inp1<=30):
        print("The number is between 20 to 30")
    elif(inp1>=30 and inp1<=40):
        print("The number is between 30 to 40")
    elif(inp1>=40 and inp1<=50):
        print("The number is between 40 to 50")
    elif(inp1>=50 and inp1<=60):
        print("The number is between 50 to 60")
    else:
        print("Number is greater than 60")
else:
    print("Number is negative")
