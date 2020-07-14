#set in python is represented by paranthesis and it is being introduced just because of its unique propert to store only unique values and doesnot repeat
p = ["anish","karbon","crrep"]
scoup = set([1, 2, 3, 4])

print(scoup)
print(type(scoup))

e = set()
e.add("anish")
e.add("bhavya")
e.add("anish")                        #only one anish will be stored in the set
e.add("meera")
e.add("kiran , jyoti")
print(e)
f = set()

f.add(" meera , karan , divya , praneet , anish ")
print(f)
#f.remove(' divya ')
print(f)
print(len(e))

print(e.intersection(f))
print("discover eat the very")
print(" forming a dictionary and we need to find the meaning of that word which is to be taken from the user ")

mole= {"anish":"lappy , phone" , "meera":["anish",12,13,19,"gulu"] , "bhavya":["karan","kunal","sinchan"]}
p = input("enter a key")
print(mole[p])
