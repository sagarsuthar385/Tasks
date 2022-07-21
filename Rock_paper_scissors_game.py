import random
while True:
 print("--------:Welcome to Rock Paper Scisser game:--------")


 print(":------------------------------:")
 chance=input("my chance(rock/paper/scisser)= ").lower()

 lst=["rock", "paper", "scisser"]
 computer=random.choice(lst)
 print("computer chance= ", computer)
 print(":------------------------------:")

 print(":------------------------------:")

 if chance==computer:
    print("Both are same! Game tie.")

 elif chance=="rock":
    if computer=="scisser":
        print("Rock break scisser! You win.")
    else:
        print("Paper covered rock! Computer win.")

 elif chance=="scisser":
    if computer=="paper":
        print("Scisser cuts paper! You win")
    else:
        print("Rock break scisser! Computer win")
 
 elif chance=="paper":
    if computer=="rock":
        print("Paper covered rock! You win")
    else:
        print("Scisser cut Paper! Computer win")                    
 
 print(":------------------------------:")
 print("    :------Game Over-----:")
 play_again=input("play again(y/n)= ")
 if play_again.lower()!="y":
        break         