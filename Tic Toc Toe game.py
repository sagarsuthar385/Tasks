while True:


 import random
 from unicodedata import name
 print("----:Welcome to Tic Toc Toe game:----\n                   ")

 deshboard={"1":"   ","2":"   ","3":"   ",
           "4":"   ","5":"   ","6":"   ",
           "7":"   ","8":"   ","9":"   "}
 lst=list(deshboard.keys())             
 player=1
 total_chance=0
 end_check=0
 def check():
  if deshboard["1"]==" x " and deshboard["2"]==" x " and deshboard["3"]==" x ":
      print("Game winner is :-", name)
      return 1
  if deshboard["4"]==" x " and deshboard["5"]==" x " and deshboard["6"]==" x ":
      print("Game winner is :-", name)
      return 1
  if deshboard["7"]==" x " and deshboard["8"]=="x" and deshboard["9"]=="x":
      print("Game winner is :-", name)
      return 1
  if deshboard["1"]==" x " and deshboard["5"]==" x " and deshboard["9"]==" x ":
      print("Game winner is :-", name)
      return 1
  if deshboard["3"]==" x " and deshboard["5"]==" x " and deshboard["7"]==" x ":
      print("Game winner is :-", name)
      return 1 
  if deshboard["1"]==" x " and deshboard["4"]==" x " and deshboard["7"]==" x ":
      print("Game winner is :-", name)
      return 1 
  if deshboard["2"]==" x " and deshboard["5"]==" x " and deshboard["8"]==" x ":
      print("Game winner is :-", name)
      return 1 
  if deshboard["3"]==" x " and deshboard["6"]==" x " and deshboard["9"]==" x ":
      print("Game winner is :-", name)
      return 1              

  if deshboard["1"]=="O" and deshboard["2"]=="O" and deshboard["3"]=="O":
      print("Game winner is :- Computer")
      return 1
  if deshboard["4"]==" O " and deshboard["5"]==" O " and deshboard["6"]==" O ":
      print("Game winner is :- Computer")
      return 1
  if deshboard["7"]==" O " and deshboard["8"]==" O " and deshboard["9"]==" O ":
      print("Game winner is :- Computer")
      return 1
  if deshboard["1"]==" O " and deshboard["5"]==" O " and deshboard["9"]==" O ":
      print("Game winner is :- Computer")
      return 1
  if deshboard["3"]==" O " and deshboard["5"]==" O " and deshboard["7"]==" O ":
      print("Game winner is :- Computer")
      return 1  
  if deshboard["1"]==" O " and deshboard["4"]==" O " and deshboard["7"]==" O ":
      print("Game winner is :- Computer")
      return 1 
  if deshboard["2"]==" O " and deshboard["5"]==" O " and deshboard["8"]==" O ":
      print("Game winner is :- Computer")
      return 1 
  if deshboard["3"]==" O " and deshboard["6"]==" O " and deshboard["9"]==" O ":
      print("Game winner is :- Computer")
      return 1      
  return 0 
   
 name=input("Please enter your name:- ")

 print('''
 x--------------------x
  1  | 2  | 3 
 :---|----|---:
  4  | 5  | 6
 :---|----|---:
  7  | 8  | 9
 x--------------------x


         ''')           
 while True:
    
    print(":-------------------:")
    print(deshboard["1"]+'|'+deshboard["2"]+'|'+deshboard["3"])
    print(":--|---|----:")

    print(deshboard["4"]+'|'+deshboard["5"]+'|'+deshboard["6"])
    print(":--|---|----:")

    print(deshboard["7"]+'|'+deshboard["8"]+'|'+deshboard["9"])
    print(":-------------------:")

    end_check=check()    
    if total_chance==9 or end_check==1:
     break
    while True:
        if player==1:
          chance=input("Your chance= ")
          if chance in deshboard and deshboard[chance]=="   ":
             deshboard[chance]=" x "
             player=2
             break
          else:
             print("Invalid input, Please right input value.")
             continue   
        else:
          chance=random.choice(lst)
          print("computer chance= ", chance)
          if chance in deshboard and deshboard[chance]=="   ":
              deshboard[chance]=" O "
              player=1
              break
          else:
             print("Invalid input, Please right input value.")     
             continue
 total_chance+=1
 print()    
 print("  :--Game Over--:")

 play_again=input("play again(y/n)= ")
 if play_again.lower()!="y":

     
   break



