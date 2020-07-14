#continue and break
#break means to come out of the loop
i =0
while True:
    print(i)
    if i>33:
        break         #stop the loop
    i += 1
print("here is another slot of examp")
#here we will learn the use of continue , continue means to skip the current itteration

j=0

while True:
    if j%2==0:
        print("here is the no", j)
        j = j+1
        continue
    print(j)

    if j==45:
        print("thats the end")
        break
    j = j+1

#we have to print a loop where we need to take the i/p from the user and if user provided i/p is less than 100 then
#it will print the content if it greater than 100 it will print sry u had invalid i/p and break the loop
print("here we have this program where we are only using break method\n")
while True:
    inp = int(input("enter a no\n"))
    if inp<100:
        print("it is a valid no\n",inp)
    else:
        print("the entered no  is not valid\n",inp)
        break

#same program but using the break and continue method
print("here we have another program")
while 1:
    inp1 = int(input("enter a no \n"))
    if inp1>100:
        print("entere no is greater than 100, 'congrats'\n",inp1)
        break
    else:
        print("please try once more\n")
        continue