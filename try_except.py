#try , except Exception as 'e'
#try and except use tb hota hai jb hume program ko break ni krna hai but hume doubt hai ki error throw ho sakta hai to aise
#case me hum try except use karenge


print("enter a no")
num1 = input()
print("enter another no")
num2 = input()

try:
    print("the sum of two no is", int(num1) + int(num2))
except Exception as f:
    print(f)

print("i m glad my program is didn't break")

