#dictionary is a pair of key and values
d1 = {"anish":"roti , daal , sabji, fish, egg, chicken", "mummy":"roti , chawal, sabji, burger, pizza", "jyoti":"pizza , "
                            "burger, roti, daal, sandwich, candies", "papa":{"morning" : ["oates , milk"] , "afternoon":["chawal , daal , sabji"]
       , "night":["pizza  snacks  maggies"]}}
d1["meera"]= "pizza , burger , oates , french fries"
print(d1)
print(d1["mummy"])
print(d1["papa"]["morning"])
d2 = {"anish":"basketball , pubg" , "jyoti":" jua , ludo" , "bhavya":{"morning":{"mon":"pubg" , "sat":"cricket"}, "afternoon":"freefire , cod"}}
d2["bhavya"]["night"] = "freeshot , pubg , badminton"
print(d2)
print(d2["bhavya"])
print(d2["bhavya"]["morning"])
del d2["bhavya"]["night"]                      #here we can del only keys not value
print(d2)

d2["bhavya"]["night"] = "freeshot , pubg , badminton"
print(d2.copy())                               #it is just creating a copy of d2 dict
d3 = d2
del d3["jyoti"]
print(d3)                                     #why jyoti key is deleted from d2 and d3 is just bcz d3 is not a new dict it is just pointing d2
print(d2)                                     # nd if we del anything in d3 it will automatically get deleted in d2 also , hence d2.copy is needed
d2["jyoti"]  = " jua , ludo"
print(d2)
print("lets give a break")
d3 = d2.copy()
del d3["jyoti"]
print(d2)                                      # it doesnot have "jyoti" key and its items
print(d3)                                      #the d3 dict doesnot have "jyoti" key and its items the so
print(d3.get("anish"))
d2.update({"kunal":"khao puri , bnana , dhokla"})
print(d2)
print(d2.keys())
print(d2.items())

print("give a long break")

#create a dictionary and take i/p from user and return the meaning of the word from the dictionary
print("what did u like to search")
dict = {"mutable":"it can be altered" , "imutable":"it cant be altered" , "computer":"an electronic computing device"}
inp = input("enter your word")
print(dict.get(inp))


