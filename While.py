# # Exercise code to print a table which user inputs using while loop

# n=int(input("Enter a Number Here"))
# i=1
# while(i<=10):
#     print(n,"x",i,"=",(n*i))
#     i+=1
    
# # printing n-natural numbers in reverse order
# num1=int(input("Enter any number here")) 
# while(num1>=0):
#     print(num1)
#     num1-=1
    
# #Checking if a given number is palindrome or not
# n=int(input("Enter your input"))
# temp=n
# reversed=0
# while(temp>0):
#     remainder= temp%10
#     temp = temp//10
#     reversed=reversed*10+remainder
#     # print(reversed)
#     if(reversed==n):
#         print("Gven number is palindrome")
# print(reversed)
# print()

#  # Checking if a given string is palindrome or not
# str1=input("Enter a String: ")
# if(str1[:]==str1[::-1]):
#     print("The Given string is palindrome")
# else:
#     print("The Given String is not palindrome")
# print()

# # Finding Factorial!
# x=int(input("Enter Number"))
# fact=1
# while(x>=1):
#     fact=fact*x
#     x-=1
# print("Factorial:",fact)
# print()

# #Finding that a number is prime or not using loop

# pr_inp= int(input("Enter a Number"))
# flag=True
# for i in range(2,pr_inp):
#     if(pr_inp % i== 0):
#         flag=False
# if(flag==True):
#     print(pr_inp,"is a Prime number")
# else:
#     print(pr_inp,"is not a Prime number")
# print()

# Printing Fibonacci series
f=int(input("Enter Number"))
x=0
y=1
z=0
while(z<=f):
    print(z, end =" " )
    x=y
    y=z
    z=x+y

    