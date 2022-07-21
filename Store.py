def store():
 sum=0
 disc={'sugar':45,'tea':95,'rice':100,'oil':160,'salt':20,'milk':29,'ghee':700,'soap':10,'namkeen':100,'papad':150,'butter milk':20}
         
 lst=list(disc.keys())
 print("""
      :-Welcome to Sagar Store-:
x---------------:Menu:---------------x

   1.Sugar----------------45/kg.
   2.Tea------------------100/pack.
   3.Rice-----------------100/kg.
   4.Oil------------------160/ltr.
   5.Salt-----------------20/pack.
   6.Milk-----------------29/pack
   7.Ghee-----------------700/pack
   8.Soap-----------------10/pack
   9.Namkeen--------------100/pack
   10.Papad---------------150/pack
   11.Butter milk---------20/pack
""") 
 print("x-----------------------------------x")      
  
 while True:
     choice=input("Please enter item name from menu(exist for E)= ")

     if choice in lst:
      a=int(input("Enter the quantity"))
      sum=sum+(a*disc[choice])
      print("Amount of", choice,"= ",a,"x",disc[choice],"=",(a*disc[choice]),"/-")

     elif choice=="E" or choice=="e":
      break
     else:
      print("Please enter right name of item from menu")
 print("\n\nx-----------------------------------x")         
 print("Total billing amount is = ",sum,"/-")
 print("x-----------------------------------x")         
 

 print("    Thank you for shopping with us \n     x-------Visit again-------x") 


store()