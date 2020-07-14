#recursion of function is something like function ke andar function or nested function
''' it is like factorial eg:- n! = n*(n-1)*(n-2)*(n-3)*(n-4)*(N-5)
we can write in one more better way:- n!= n*(n-1)!
a thing of the school were in the same thing
'''
def stardom(str):
    print("ye function define hua sirf string argument lene ke liye",str)
stardom("ye ek string value hai")



#iterative function is the function which get executed only once

def iterfun(r):
    no = 1
    for i in range(r):
        no = no * (i+1)
    return no

    pass


num = int(input("enter a no"))
print(iterfun(num))

#this one is also an another example of iterative func

def iterfun2(num1):
    fun2 = 1
    for j in range(num1):
        fun2 = fun2 * (j+1)
    return fun2
num1 = int(input("enter another no"))
print(iterfun2(num1))


#examples for recursive
def recrfun(num3):

    if num3==1:
        return 1
    else:
        return num3 * recrfun((num3 - 1))

num3 = int(input("enter a factorial no"))
print(recrfun(num3))

#fibonacci series is just sum of addition of last two no eg:- 0 1 1 2 3 5 8 13 21....
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) * fibon(n-2)


