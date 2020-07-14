# here we will learn how to use read , write operation
#if we use write , then it will always remove the previous content and and new fresh content
#nd similarly if we use append, then we can add further more content without deleting previous one
# 'a' - use hota hai describe karne me ki isne kitne char print kiye hai

''' ye rha program yaha se start ho rha hai '''

# f = open("anish.txt","w")
# f.write(" anish bhai tu chalega mere sath bol na re\n")
# f.write("check karke bta de if it is possible \n")
# f.close()

#handle read and write both
f = open("anish.txt","r+")
f.write("anish bhai tu catch krlega na\n")
print(f.read())
f.write("thankyou for everything \n")
f.write("thats my real concern \n")
