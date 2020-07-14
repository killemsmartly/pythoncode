list1 = ["anish" , "bhavya" , " akshit" , "blonde"]
print(list1)
#there is another way to print all the element of list
for item in list1:
    print(item)

#print the item of list of list
list2 = [ ["anish" ,100,200,33], ["bhavya",13] , ["akshit",190] , ["blonde",13]]
print(list2)
for item in list2:
    print(item)
#unpacking of list with some of the tag lines
list3 = [ ["anish" , " error"], ["bhavya",13] , ["akshit",190] , ["blonde",13]]
for item, number in list3:
    print(item, "he have this  much of no", number)
#now print it as dictionary

list4 = [ ["anish" ,100], ["bhavya",13] , ["akshit",190] , ["blonde",13]]
dict1 = dict(list4)
for item , number in dict1.items():
    print(item , "chal na be" ,  number)

#how to print only key of dictionary
for item in dict1:
    print(item)

#we have to make a list where anything could be we have to detect wethere it is no nd if it is no then check it is less than 6 or not

list6 = ["chintu","anish" , "meera" ,"bhavya" , "rishi" ,"shardha", "kiran" , "jyoti" , 1,2,3,7,9,3,90,56,45,34,13,4,5,6,8]

for item in list6:
    if str(item).isnumeric() and item<6:
        print("it is less than 6" , item)

    elif str(item).isnumeric() and item>6:
        print("these nos are greater than 6" , item)

    else:
        print(item)


