#to print a single line we can use keyword suchas f.readline(),here only one line wpuld be printed
#what if we want to know our file pointer, where is our file pointer after reading every line

f = open("anish.txt","r")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

#f.readlines se aage ke sare line print ho rhae hai
#f.seek() function is used to print the line from the given fle pointer
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(6)
print(f.readlines())
f.close()

