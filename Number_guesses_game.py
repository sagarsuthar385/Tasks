import random
top_of_range=input("enter your number= ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("please enter the greater number= ")
        quit()
else:
    print("please enter number next time") 

random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guesses=input("please enter your number")
    if user_guesses.isdigit:
      user_guesses=int(user_guesses)
    else:
        print("please try again")
        continue
    if user_guesses==random_number:
        print("you got it !")
        break
    elif user_guesses>random_number:
        print("you are above the right answer")
    else:
        print("you are below the right answer")
print("you got it is ",guesses,"guesses")        
