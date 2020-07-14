#we will practice for the local and global variable
l=37
def func1(j):
    print("inside part of the func1")
    l = 23
    m=34
    print("l is local var",l)
    print("m is also a local var",m)
    print(j)                                #ye j ko print krrha hai jisme "chalo chalte hai leekha hai"
    print(j,"ye j ke sath print hoga")      #yaha j ke sath "ye j ke sath print hoga"
print(l)                                    #ye l jo ki global var hai pehle print hoga
func1("chalo chalte hai")                   #ye ni hoga to program execute hi ni hoga
print(l)                                    #ye sbse last me print hoga, after the execution of func1


# ab jo program hai vo global keyword pe hai

k=12
def func2():
    print("ye ek 2nd example hai")
    m=96
    print(m)
    global k               #global keyword
    k = k+3                #global value get added
    print(k,"yaha pe global var ko update krdiya hai")

func2()


#now examples on nested function of global var

def animal():
    x=90
    y=23
    print("here x nd y are under animal func")
    def cow():
        global x
        x = 105
        print(x)
        print("cow comes under the function of cow")
        cow()
    print("here all the values")
    print(x)
    print(y)

animal()

#more clearity on nested function
#function ka execution tabhi hota hai jb uska call hota hai
def students():                                                     #2
    def kumar():                                                    #5
        print("kumar is under kumar function")                      #6
    print("this print statement is of students() function")         #3
    kumar()                                                         #4
students()                                                          #1


