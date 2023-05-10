# variables are like empty containers that stores some values. It basically holds data
a=1234
print(a)
print()
name="Rohan"
print(name)
print()
b=True
print(type(b))# Type keyword is used to get the type of the data
print()
# arithmetic operators
print (15+2)# addition operator
print (15-2)# subtraction operator
print (15*2)# multiplication operator
print (15/2)# division operator
print (15%2)# Modulus operator (returns remainder)
print (15//2)# floor division operator (returns quotient)
print (15**2)# exponential operator(same as 15^2)


#simple calculator
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
print("Addition of two numbers is:",num1+num2)
print("Subtraction of two numbers is:",num1-num2)
print("Multiplication of two numbers is:",num1*num2)
print("Division of two numbers is:",num1/num2)

print()
# comparison Operators
g=22
h=34
print(g==h)
print(g!=h)
print(g<h)
print(g>h)
 
typecasting Example
Typecasting means change one data type into other
var1="22"
var2=8
var3=int(var1) # here we've converted string into integer
sum=var3+var2
print(sum)

nm= "Harry"
print(nm[-4:-2]) 