import math
class skpizza:
    def pizza(self):
        print("     ") 
        print("--------------Welcome to Amazing Pizza and Pasta---------------")
        print("     ")
        order_comform='''
        Pizzeria :-

        press 1 : Order menu
        press 2 : Exit
        '''
        print(order_comform)
        order_comform=int(input("Enter your choice= ")) 
        if order_comform==1:
            print('''
            ---------------------------------------------------------
            Pizza menu:-
            1 large pizza= 200 rupees
            2 large pizza= 380 rupees
            3 large pizza= 650 rupees
            *** Buy 4 or more pizza and get 1.5 lt soft drink free***
            ---------------------------------------------------------
            Pasta menu:-
            1 large pizza= 150 rupees
            2 large pizza= 280 rupees
            3 large pizza= 400 rupees
            *** Buy 4 or more pasta and get 2 bruschetta free***
            ---------------------------------------------------------
            *** Buy 4 or more pizzas and pastas and get 2 bruschetta free***
            
            ----------------------Thank you--------------------------
            ''') 
            bill=0
            bill1=0
            sum=0
            sum1=0
            while True:
              print("             ") 
              name= input("Enter your name= ")
              print("Welcome,", name)
              print("             ") 
              piz=int(input("Enter number or pizza order you want= "))
              if piz==1:
                  sum=sum+piz
                  bill+=200
                  print("Your pizza amount is= ",200)
              elif piz==2:
                    sum=sum+piz
                    bill+=380
                    print("Your pizza amount is= ",380)
              elif piz==3:
                    sum=sum+piz
                    bill+=650
                    print("Your pizza amount is= ",650) 
              else :
                    sum=sum+piz
                    bill+=(piz*180)
                    print("      ")
                    print('-------------------------------------------------------------')
                    print("***Congratutions !! 1.5 lt soft drink free***")
                    print("      ")
                    print('-------------------------------------------------------------')
                    print("Your pizza amount is= ",(piz*180)) 
              print("             ")        
              A=input("Do you want to order pasta(y/n)= ")
              print("             ") 
              if A=="y":
                    pas=int(input("Enter number or pasta order you want= "))
                    if pas==1:
                        sum1=sum1+pas
                        bill1+=150
                        print("Your pasta amount is= ",150)
                    elif pas==2:
                        sum1=sum1+pas
                        bill1+=280
                        print("Your pasta amount is= ",280)
                    elif pas==3:
                        sum1=sum1+pas
                        bill1+=400
                        print("Your pasta amount is= ",400)
                    else:
                        sum1=sum1+pas
                        bill1+=(pas*130)
                        print("       ")
                        print('-------------------------------------------------------------')
                        print("***Congratutions !! get 1 bruschetta free***")
                        print("***Congratutions !! get 1 choco brownies ice cream free***")
                        print("       ")
                        print('-------------------------------------------------------------')
                        print("Your pasta amount is= ",(pas*130)) 
              print("             ")                              
              total_bill=(bill+bill1) 
              print(f"Your total amount is = {total_bill}") 
              print("             ") 
              print("---------------------------------------------------------------------")  
              Again=input("Want to enter order from another customer(y/n)= ")
              if Again.lower()!="y": 
                print("             ") 
                print("-------------Pizza and Pasta Bill-----------------")
                print("             ") 
                print("Payment received from pizza= ",round(bill))
                print("Payment received from pasta= ",round(bill1))
                print("             ") 
                print(f"Your net order amount of the day is= {total_bill}")
                print("             ") 
                print("Number of pizza and pasta sold in one sift= ", round(sum+sum1))
                print("             ") 
                if sum>=4:
                    print("Number of soft drink bottle given= ",round(math.floor(sum/4)))
                else:
                    print("Number of soft drink bottle given= ",0) 
                if sum1>=4:    
                    print("Number of bruschetta given to customer= ",round(math.floor(sum1/4)))
                else:
                    print("Number of bruschetta given to customer= ",0)
                print("             ") 
                if (sum+sum1)>=4:   
                    print("Number of choco brownies ice cream given to customer= ",(math.floor((sum+sum1)/4)))
                else:
                    print("Number of choco brownies ice cream given to customer= ",0)    
                print("             ") 
                print("---------------Have a nice day !!!-----------------") 
                print("             ")   
                break

                

                
              



f=skpizza()
f.pizza()
    