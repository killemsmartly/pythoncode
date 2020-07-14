# hume f.open and f.close na leekhna pade uske liye hum with block use karte hain:- with open("fileka naam.txt") as m:
#iske use se hume file open and close karne ki jaroort ni hoti hai , with block khud hi opne nd close function handle karleta hai

with open("anish.txt") as f:
    a = f.read(28)
    b = f.read(41)
    print(a)
    print(b)

f = open("anish.txt","r")
print(f.read())
