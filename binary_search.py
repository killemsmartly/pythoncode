'''
hume ek no program me chupa ke dalna hai or user se guess karwana hai ki vo no kya hai, user ko btana bhi hai ki uska guess
kum hai actual no se ya jayda hai and hume user ko sirf 5 guesses bhi dena hai or humesa btate rehna hai ki uska
guess kitna baki hai
agar guesses khatm hojate hai togame over print krdena hai
'''


n = 33

while True:
    inp = int(input("enter a no"))
    i = 1
    if i<=4:
        i+=1
        if inp<n:
            print("try for greater no",i)

        elif inp>n:
            print("try for smalller no",i)

        elif inp==n:
            print("congrats you have guessed the correct no",i)
            break

    else:
        print("you had taken more than 5 guessing\n 'well try\n'  'game over\n' ")
        break

