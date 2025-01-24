# Welcome to your Shop Choose Here :-
# Maggi = 80
# Kulfi = 50
# Pizza = 110

print()
print("Welcome To Akash Restaurant")
print()
print("We Have Right Now \n Maggi = ₹ 80 /- \n Kulfi = ₹ 50 /- \n Pizza = ₹ 110 /-\n Burger = ₹ 75/-")
print()

Menu = { "maggi" : 80,
        "burger" : 75,
         "kulfi" : 50,
         "pizza": 110
         }

Order_List = 0

# Now Loop Is Started For (Yes or No)
while True:
    list = ["yes","no"]
    First_Order = (input("Enter Your 1st-Order : ")).lower()

    if First_Order in Menu: # check (True Or False) !

        Order_List += (Menu[First_Order])
        print(f"Your Order ( {First_Order.capitalize()} ) is added Now !")
        break
    elif(First_Order == "cancel"):
        print("Cancel")
        break    
        
    else: #  Here Loop Will Start Again
        print(f"Sorry Right Now ( {First_Order.capitalize()} ) Is Not Present")
        print("Please Re_Enter Your Items !")
        print()
        print("Or You want To Close The Program Type -(\"Cancel\") ?")

 #------------------------------(2nd Phase)---------------------------------------------       

print()
print("Confirm sir ?")
print()
# list = ["yes","no"]
while True:
    Asking_Again = (input("Do You Want To Add One more Item ? (Type -) \n \"Yes or No\"\t:-")).lower()
    print()
    if(Asking_Again == "yes"):
        while True:
            print()
            print("We Have Right Now \n Maggi = ₹ 80 /- \n Kulfi = ₹ 50 /- \n Pizza = ₹ 110 /-\n Burger = ₹ 75/-")
            print()
            Second_Order =(input("Enter Your Order Please : ")).lower()

            if Second_Order in Menu:# check (True Or False) !

                Order_List += (Menu[Second_Order]) 
                print(f"Your Order ( {Second_Order.capitalize()} ) is added Now !")
                print()
                print(f"Your Total Amount is to Pay : ₹{Order_List}/-")
                break

            elif(Second_Order == "cancel"):
                print("Cancel")
                print(f"Your Total Amount is to Pay : ₹{Order_List}/-")
                break

            else:
                print(f"Sorry Right Now ( {Second_Order.capitalize()} ) Is Not Present")
                print("Please Re_Enter Your Items !")
                print()
                print("Or You want To Close The Program Type -(\"Cancel\") ?")
                

    elif(Asking_Again == "no"):
        print()
        print(f"Your Total Amount is to Pay : ₹ {Order_List}/-")
        break


print()
while True:
    Last_Point = input(f"Conform your order of ₹ {Order_List}/-?\n\n\tType (Yes / Cancel ) : ").lower()
    print()
    if(Last_Point == "yes"):
        print("Done")
        print()
        print("Thankyou For Visitng Here !")
        break
    elif(Last_Point =="cancel"):
        Order_List -= Order_List
        print(f"Your Total Items is Canceled {Order_List}/-")
        print()
        print("Thankyou For Visitng Here !")
        break

    else:
        print(f"Sorry You Type {Last_Point.capitalize()}")
        print("Please Re_Enter (Yes or Cancel) !")

 


