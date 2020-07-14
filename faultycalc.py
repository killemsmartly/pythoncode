#faulty calculator 45*3=555,  56+9=77, 56/6=4, 45-9=12
var1 = input("enter one no")
var2 = input("enter operator u want to coose")
var3 = input("enter 2nd no")
output = var1 + var2 + var3
if output == '56+9':
    print(555)
elif output == '45-9':
    print(12)
elif output == '45*3':
    print(555)
elif output == '56/6':
    print(75)
elif var2 == " * ":
    print(int(var1) * int(var3))
elif  var2 == "+" :
    print(int(var1) + int(var3))
elif var2 == "-" :
    print(int(var1) - int(var3))
elif var2 == "/" :
    print(int(var1) / int(var3))

