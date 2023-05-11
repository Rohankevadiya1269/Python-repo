# This is an exercise code to find the Middle number
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd  number"))
if(a>b and a<c) or (a<b and a>c):
    print("a is middle value")
elif(b>a and b<c) or (b<a and b>c):
    print("b is middle value")
else:
    print("c is middle value")

print()
 # Exercise code to calculate total marks and percentage
 # also assign grade as per percentage
total_marks=500
maths=int(input("Enter marks of maths subject"))
science=int(input("Enter marks of science subject"))
history=int(input("Enter marks of history subject"))
ss=int(input("Enter marks of ss subject"))
gujarati=int(input("Enter marks of gujarati subject"))
marks_obtained= maths+science+history+ss+gujarati
print("Your Total Marks is:",marks_obtained)
percentage= (marks_obtained/total_marks)*100
print(percentage)
if(percentage>=80):
    print("You have obtained Grade A")
elif(percentage>60 and percentage<80):
    print("You have obtained Grade B")
elif(percentage>40 and percentage<60):
    print("You have obtained Grade C")
else:
    print("You have obtained Grade D")
print()

#Even-odd exercise code
num_ber=int(input("Enter a Number Here"))
if(num_ber%2==0):
    print(num_ber,"Is an even number")
else:
    print(num_ber,"Is an odd number")
print()

#Exercise code
inp_ut= int(input("Enter any number Here"))
if(inp_ut%3==0 and inp_ut%5==0):
    print("Hello\" Crazy Programmer\"")
elif(inp_ut%3==0):
    print("Hello \"Crazy\"")
elif(inp_ut%5==0):
    print("Hello \"Programmer\"")
else:
    print("Learn Programming")