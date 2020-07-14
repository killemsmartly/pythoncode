#fibonacci series

def fac(num):
    fac_itr = 1
    for i in range(num):
        fac_itr = fac_itr * (i+1)
    return fac_itr


num = int(input("enter any no"))
print(fac(num))


#factorial using iterative method

def recr(no):
    if no == 2:
        return 4                       #this one is the main difference , here we can return at any value
    else:
        return no * recr(no-1)

no = int(input("enter a no for factorial"))
print(recr(no))
