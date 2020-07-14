#what is global variable and global keyword
#here we will try to learn the scope of global variables and global keywords


#neeche ke examples global var ke hai
l = 10  #global var
n = 29
def func1(j):
    print(j, "ye local var hai")
    l=1+45   #local var
    m=23
    print(m)
    print(l)
    #n=n+23     #global var couldn't be changed
    #print(n)
#to do any changes in global var we need to use  global n
    global n        #ye homgya humara global keyword
    n = n+23
    print(n)
func1("ye lo ab")
func1("ye func1 me enter horha hai \n")
# print(m)
print(l)
