#examples on function

#very simple function, here 'sum' is function and it is the example of inbuilt function
a = 4
b = 6
c = sum((a,b))
print(c)

def func1():
    print("here we have our 1st user defined function")
#print(func1())                       #this print word will give none
func1()                 # here none will not be printd, matlb ki yaha function directly func1 keyword se ghusega nd print karega andar wale content ko
def func2(a,b):                #yaha pe func2 user i/p lerha hai
    print("sum of the entered two no is",a+b)
func2(4,5)

def func3(a,b):
    avg = (a+b)/2
    print(avg)
    return (avg)            # agr yaha return(avg) and  and print(n) indono ke presence me none print ni hota hai
#func3(23,33)               #ans will be 28.0 by printing this func3(23,33)
n = func3(23,33)
print(n)

#upar agar return ko comment out krdenge to o/p me none dekhega hume

def func4():
    ''' doc string ko print kiya jayega by this way print(func4._doc_) '''
    print(" hi there ")
print(func4.__doc__)
