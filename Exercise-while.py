# Printing Right angled triangle using while loop

i=int(input("Enter any number here"))
j=1
while(j<=i):
    k=1
    while(k<=j):
       print("*",end=" ") 
       k+=1
    print()
    j+=1
print()        

# Printing right angles triangle in reverse order

num=int(input("Enter any number here"))
temp=num
while(temp>=1):
    s=temp
    while(s>=1):
        print("*",end=" ")
        s-=1
    temp-=1
    print()
    
print()
# printing right angled triangle of numbers using while loop
a=1
while(a<=i):
    e=1
    while(e<=a):
        print(e,end=" ")
        e+=1
    print()
    a+=1
        
# Printing mirrored right angled triangle of stars
j=1
while(j<=i):
    w=1
    while(w<=i-j):
        print(" ",end=" ")
        w+=1
    k=1
    while(k<=j):
        print("*",end=" ")
        k+=1
    print()
    j+=1

# Printing triangle pattern using while loop
inp1=int(input("Enter any number here"))
a=1
d=1
while(a<=inp1):
    b=1
    while(b<=(inp1-a)):
        print(" ",end="")
        b+=1
    c=1
    while(c<=d):
        print("*",end="")
        c+=1
    d+=2
    print()
    a+=1
        
        
        
a=int(input("Enter any number here"))
i=1
while(i<=a):
    j=1
    while(j<=i):
        print(j,end="")
        j+=1
    print()
    i+=1

a=int(input("Enter any number here "))
i=1
h=1
while(i<=a):
    j=1
    while(j<=a-i):
        print(" ",end="")
        j+=1
    k=1
    while(k<=h):
        print("*",end="")
        k+=1
    print()
    i+=1
    h+=2
i=a
r=1
x=((2*a)-3)
while(i>1):
    q=1
    while(q<=r):
        print(" ",end="")
        q+=1
    p=1
    while(p<=x):
        print("*",end="")
        p+=1
    print()
    i-=1
    x-=2
    r+=1