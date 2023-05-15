a=int(input("Enter number here: "))
for x in range(1,a+1):
    for y in range(x):
        print("*",end="")
    print()
    
print()
# right angled triangle of numbers
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
print()
# right angled triangle of same number '11111'
for i in range(1,a+1):
    for j in range(i):
        print(i,end="")
    print()
    
print()

# Inverted Triangle of star
temp=a
for i in range(temp,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print()
# inverted triangle of same number in row
for i in range(temp,0,-1):
    for j in range(i):
        print(i,end="")
    print()
print()

# inverted triangle of number 
for i in range(temp,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()

# Mirrored triangle
for i in range(1,a+1):
    for j in range(a,0,-1):
        if j>i:
            print(" ",end="")
        else:
            print("*",end="")
    print()
            
print()

#Mirrored triangle of numbers
for i in range(1,a+1):
    num=1
    for j in range(a,0,-1):
        if j>i:
            print(" ",end="")
        else:
            print(num,end="")
            num+=1
    print()
            