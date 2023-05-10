priceOfApple= 210
budget= 200  
if(budget>=priceOfApple):
    print("Siri add apples to the cart")
else:
    print("siri do not add apples to the cart")
print()

age=int(input("Enter a your age here:"))
if(age<18):
    print("OOPS You are not eligible to vote")
else:
    print("You are eligible to vote")
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
print()
 # Code Exercise
 # In this exercise We can print a Greeting message based on time using if else loop 
import time
timestamp=time.strftime('%H:%M:%S') #strftime is a method that returns local time in string format
timestamp1=time.strftime('%H')
timestamp2=time.strftime('%M')
timestamp3=time.strftime('%S')
print(timestamp)

timestamp4=int(timestamp1)
if(timestamp4>=6 and timestamp4<12):
    print("Good Morning Sir !!")
elif(timestamp4>=12 and timestamp4<17):
    print("Good Afternoon Sir !!")
elif(timestamp4>=17 and timestamp4<21):
    print("Good Evening Sir !!")
else:
    print("Good Night Sir !!")
    