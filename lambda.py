def add(a , b):
    return a+b

print(add(14,15))

# lambda function or anonymous function
# lambda ek function hoke bhi function ni hai , ye ek line function hota hai
# 'name of the function u want' lambda x,y = x operation y

add1 = lambda x , y : x + y
print(add1(14,19))

sub1 =lambda x,y : x - y
print(sub1(120,30))

def multi (list):
    return list[1]

list = [[1,19] , [12,3] , [23,1] , [2,6] , [29,1]]
list.sort(key=multi)
print(list)

#same program would be executed by lambda function
list1 = lambda ready
ready = [[1,4] , [2,3] , [12,45] , [12,1] , [6,90]]
ready.sort(key=list1)
print(ready)

mailtrack.io