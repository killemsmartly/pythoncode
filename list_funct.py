#var jb square bracket use karta hai to matlb samjh lo ki ye ek list hai eg:- var1 = [ .....]
shop = ["jeans" , "shirt" , "underwear", "bill" , "belt" , "tie" , "blazzer"]
homelist = [1,2,3,5,2,1,8,0,9,3,7,2,9,0,5]
print(shop[2])
print(shop)
print(shop[1:6])
homelist.sort()
homelist.reverse()
print(homelist.append(23))
print(homelist)
homelist.insert(1,10)                          #to add a no in b/w anywhere in the list 1bit tell index value nd 2nd will tell value needed
print(homelist)
homelist.remove(5)                             #to remove any element from anywhere in the list
print(homelist)
homelist.pop()
print(homelist)                                #it will remove last element of the list
homelist[0] = 67
print(homelist)

#tupple me paranthesis use hota hai or ye immutable hota hai
tup = (1,2,5,3,4,6,7)
print(tup)

a = 20
b = 34                                      #a best way to swap the values of two var 
a , b = b , a
print(a,b)
trd = a
a = b                                       #traditional way to of swapping
b = trd

print(a , b)