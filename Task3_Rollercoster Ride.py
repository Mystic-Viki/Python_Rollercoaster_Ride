print("Welcome to Rollercoster Ride")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
bill = 0

# This code checks if the user is tall enough to ride a rollercoaster
if height >= 120:   
    print("You can ride the rollercoaster!")

    if age<= 12:
        bill = 5
        print("Please pay $5")

    elif age<= 20:
         bill =7
         print("Please pay $7")

    else:
         bill =10
         print ("Please pay $10")

    #Check if the user wants a picture taken
    #If yes, add $3 to the bill
    

    while True:
     picture = input("Do you want your picture to be taken? Yes or No ")
      
     if picture == "Yes":
        print(f"You said Yes. Please pay ${bill+3}")
        break
     elif picture == "No":
        print(f"No Picture. Total amount is ${bill}")
        break
     else:
        print("Please Enter correct option")
    #Check if the user is tall enough to ride
else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")


    #Check if number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else    :
    print(f"{number} is an odd number.")
    

    