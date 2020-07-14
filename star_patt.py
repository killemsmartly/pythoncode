#printing star pattern
#first simple method to print a right angled triangle
'''
no = int(input(" please provide a no "))           #asking user to state that how many rows of triangle a user want
for i in range(0,no):                              # this is an outer loop which will be used for running a row
    for k in range(0,i+1):
        print(" * " , end=" ")
    print()                                        #new line character

#printing star but odd no of pattern is followed

no2 = int(input("enter how many rows u want to print"))
n=1
for l in range(0,no2):                                 #printing given no of rows
    for m in range(0,n):                          #printing +2 more coloumns than rows
        print(" # ",end=" ")
    n=n+2
    print()

#we will make mirror image of right angleed triangle by using for loop

1. 1 loop which will control no of rows
2. another loop which will control spacing
3. another loop which will control the printing of asterik

- outer loop is for rows
-2nd for loop is to print no of spacing , 1st rows--4spacing , 2nd rows--3spacing...


no = int(input("enter a no"))
for row in range(1,no+1):
    for col in range(1,row+1):
        print(" * ",end="")
    print()                                       #new line character , is used to add a new line after executing col

#same pattern in reverse order
no1 = int(input("enter another no"))
for row1 in range(no1,0,-1):
    for col1 in range(1,row1+1):
        print(" * ",end=" ")
    print()

#printg another pattern
n = int(input("enter a diff no"))
for f in range(0,n+1):
    for g in range(0,f+1):
        print(" * ",end=" ")
    print()

for h in range(n+1,0,-1):
    for o in range(1,h):
        print(" * ", end=" ")
    print()
'''
# similarly if we want to print no's of row or col at the place of asterik, right below are the examples

t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        print( row , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        print(x , end="  ")
    print()

print("here is your another pattern , displaying column value")

t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        print( col , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        print(y , end="  ")
    print()

print("now we will agin print another pattern where we will display row nd col value together")

t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        print( "{} {}".format(row,col)  , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        print("{} {}".format(x,y) , end="  ")
    print()

print("here we are printing one more pattern of A, we are using ascii value of a that is 65")

t=int(input("enter a no here"))
asc = 65
asc1 = 67
for row in range(0,t+1):
    for col in range(0,row+1):
        print( "{}{} ".format(chr(asc) , chr(asc1))  , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        print("{}{} ".format(chr(asc) , chr(asc1)) , end="  ")
    print()

print("we want to print one pattern where letters of alphabets are to be printed")

t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        print( "{}".format(chr(asc+col))  , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        print("{}".format(chr(asc1+y)) , end="  ")
    print()

print("here one more pattern is printing tha alphabets in order with no repetition")

asc = 64
t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        asc = asc +1
        print( "{}".format(chr(asc))  , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        asc = asc + 1
        print("{}".format(chr(asc)) , end="  ")
    print()

print(" printing last pattern where we will represent no in ascending order in this pattern")

sum = 0
t=int(input("enter a no here"))
for row in range(0,t+1):
    for col in range(0,row+1):
        sum = sum +1
        print( "{}".format(sum)  , end="  " )
    print()
for x in range(t,0,-1):
    for y in range(0,x):
        sum = sum + 1
        print("{}".format(sum) , end="  ")
    print()
