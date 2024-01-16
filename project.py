print("-"*60)
print("                     GYM MANAGEMENT            ")
print("-"*60)
print("1.Add a new member" "\n"
      "2.Show the list of members" "\n"
      "3.Remove a member" "\n"
      "4.To find a member by entering their id" "\n"
      "5.Type of training and their cost" "\n"
      "6.Type of equipments available" "\n"
      "7.Exit")
print("-"*60)
d={}
while True:
 a=(input("Enter your choice:"))
 if a=="1":
     c=input("Enter name:")
     i=input("Enter id:")
     age=int(input("Enter age:"))
     new={"Name":c,"Age":age}
     d[i]=new
     print("Member added successfully")
     print("-"*60)
 elif a=="2":
     print("All members:")
     print("-"*60)
 elif a=="3":
     
     print("-"*60)
 elif a=="4":
     v=input("Enter id:")
     if v in d:
         details=d[v]
         print("ID:{v}")
         print("Name:{details['Name']}")
         print("Age:details['Age']")
     else:
         print("Member not found")
     print("-"*60)    
 elif a=="5":
     print("1.Cardio" "\n"
           "2.Bulking" "\n"
           "3.Zumba")
     b=input("Enter your choice:")
     print("*"*60)
     if b=="1":
         print("This training is based on weight loss and it can be done without using any equipment" "\n"
               "Cost:799/- (per month)")
     elif b=="2":
         print("This training is based on building muscles" "\n"
               "Cost:999/- (per month)")
     elif b=="3":
         print("This training is based on aerobic fitness by using dance moves and improves flexibility" "\n"
               "Cost:899/- (per month)")
     else:
         print("Please enter a correct option")
     print("*"*60)
     print("-"*60)
 elif a=="6":
     print("1.Resistance training machine" "\n"
           "i.Weighted Strength training" "\n"
           "ii.Power lifting equipment")
     print("*"*60)
     print("2.Free weights" "\n"
           "Eg:Dumbell,Barbell,Resistance band,etc")
     print("*"*60)
     print("3.Cardio machines" "\n"
           "Eg:Treadmill,Ellipticals,Stair climbing,etc")
     print("*"*60)
     print("4.Home gym (all in one machines)" "\n"
           "Eg:Bench press,rowing machine,exercise bike,etc")
     print("*"*60)
     print("5.Hydraulic machines" "\n"
           "These machines are used to target specific muscles that normal machines cannot target")
     print("-"*60)
 elif a=="7":
     print("Thank you!")
     print("-"*60)
     break
 else:
     print("Please enter a valid option between 1 to 7")
     print("-"*60)
