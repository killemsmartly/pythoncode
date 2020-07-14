my_strng = 'anish want to print string statement'
print(my_strng[::])

my_strng = 'anish want to print string statement'
print(my_strng[9])
my_strng = 'anish want to print string statement'
print(my_strng[0:37:3])


my_strng = 'anish want to print string statement'
print(my_strng[::673])                #it will print first position char and not to others bcz 673 is out of the limit
print(len(my_strng))
print(my_strng[::-1])                   #reverse a string
print(my_strng[::-2])                   #it leaves one char gap in the string
print(my_strng.endswith('statement'))           #it gives 'true' response bcs string is ending with stmnt word
print(my_strng.isalnum())                # is alpha numeric here give 'false' response bcz here is the gap in the string
print(my_strng.isalpha())                #is alpha also give false response
print(my_strng.count('i'))               # 3 i dega result me
print(my_strng.find('to'))
print(my_strng.capitalize())
print(my_strng.lower())
print(my_strng.upper())
print(my_strng.replace('want','need'))
print(my_strng.lower())