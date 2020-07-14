#function are of two types:- 1.builtin function    2.user define function

def check_fun():
    print('if it get printed, means this func is working properly')
print(check_fun())

#if print(check_fun() is written then it will exxecute everything what ever is there in the func nd then in return it give none

def check_fun():
    print('if it get printed, means this func is working properly')
check_fun()

def check_sum(a,b):
    print('enter two no to add',a*b)
    avg = (a + b)/2
    return avg        #return is used to avoid the none in o/p console window
print(check_sum(70,50))