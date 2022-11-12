# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890 
# What do you want to do? (1-3): 3
# Exit? n

# empty dictionary
contactTracing = {}

print()
print("CONTACT TRACING PROGRAM")

while True:

    print()
    print("Menu:")
    print("1 -> Add an item")
    print("2 -> Search an item")
    print("3 -> Exit")

    # checks if user input is valid
    while True:
        print()
        userInput = int(input("Enter the number you want to execute: "))
        if userInput > 0 and userInput <= 3:
            break
        else:
            print("Invalid number. Try entering numbers from 1 to 3.")

    # add an item in the dictionary
    if userInput == 1:
        print()
        registeredName = input("Register your name: ")
        contactTracing[registeredName] = {}

        print()
        print("Contact Tracing Form")
        
        print()
        print("Personal Information")
        userName = input("Name: ")
        userSex = input("Sex: ")
        userAge = input("Age: ")
        userAddress = (input("Address: "))
        userContact = input("Contact number: ")
        userEmail = input("Email: ")

        # print()
        # print("Health Information")
        # userPositive = input("Have you been diagnosed with COVID? ")
        # userCold = input("Have you had a cold in the past 7 days? ")
        # userCough = input("Have you had a cough in the past 7 days? ")
        # userCommorbidities = input("Do you have commorbidities? ")

        # print()
        # print("Travel History")
        # userCrowded = input("Have you recently been in another public and/or crowded location? ")
        # userCovid = input("Have you recently been in contact with a person with COVID in the past 14 days? ")
        # userCity = input("Have you traveled outside your city in the past 14 days? ")
        # userCountry = input("Have you traveled outside the country in the past 14 days? ")

        # contactTracing[registeredName] = {"Name" : userName, "Sex" : userSex, "Age" : userAge, "Address" : userAddress, "Contact number" : userContact, "Email" : userEmail, "CCOVID positive" : userPositive, "Cold history" : userCold, "Cough history" : userCough, "Commorbidities" : userCommorbidities, "Public contact" : userCrowded, "Covid contact" : userCovid, "Outside city" : userCity, "Outside country" : userCountry}

        contactTracing[registeredName]["Name"] = userName
        contactTracing[registeredName]["Sex"] = userSex
        contactTracing[registeredName]["Age"] = userAge
        contactTracing[registeredName]["Address"] = userAddress
        contactTracing[registeredName]["Contact number"] = userContact
        contactTracing[registeredName]["Email"] = userEmail

        print()
        print("Saved successfuly!")

    # search an item in the dictionary
    elif userInput == 2:
        userSearch = input("Enter the name you want to search for: ")
        for userSearch in contactTracing:
            print()
            print("Name", ":", userName)
            print("Name: " + contactTracing[registeredName]["Name"])
            print("Sex: " + contactTracing[registeredName]["Sex"])
            print("Age: " + contactTracing[registeredName]["Age"])
            print("Address: " + contactTracing[registeredName]["Address"])
            print("Contact Number: " + contactTracing[registeredName]["Contact number"])
            print("Email: " + contactTracing[registeredName]["Email"])

    # exit the program
    elif userInput == 3:
        userExit = input("Do you want to exit the program? ")
        if userExit.upper() == "YES":
            break
        elif userExit.upper() == "NO":
            continue