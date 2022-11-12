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

# empty main dictionary
contactTracing = {}

while True:

    print()
    print("CONTACT TRACING PROGRAM")

    print()
    print("======= \033[1;3mMenu\033[0m =======")
    print("\033[1m1\033[0m -> Add an item")
    print("\033[1m2\033[0m -> Search an item")
    print("\033[1m3\033[0m -> Exit")

    # checks if user input is valid
    while True:
        print()
        userInput = int(input("Enter the number you want to execute: "))
        if userInput > 0 and userInput <= 3:
            break
        else:
            print("\033[1;31;40mInvalid number. Try entering numbers from 1 to 3.\033[0m")

    # add an item in the dictionary
    if userInput == 1:
        print()
        registeredName = str(input("Register your name: ")) ; registeredName.title()
    
        print()
        print("-------- CONTACT TRACING FORM --------")
        
        print()
        print("\033[1mPersonal Information\033[0m")
        userName = input("Name: ")
        userSex = input("Sex (F/M): ")
        userAge = input("Age: ")
        userAddress = (input("Address: "))
        userContact = input("Contact number: ")

        print()
        print("\033[1mHealth Information\033[0m")
        userPositive = input("Have you been diagnosed with COVID? (Yes/No) ")
        userCold = input("Have you had a cold in the past 7 days? (Yes/No) ")
        userCough = input("Have you had a cough in the past 7 days? (Yes/No) ")
        userCommorbidities = input("Do you have commorbidities? (Yes/No) ")

        print()
        print("\033[1mTravel History\033[0m")
        userCrowded = input("Have you recently been in another public and/or crowded location? (Yes/No) ")
        userCovid = input("Have you recently been in contact with a person with COVID in the past 14 days? (Yes/No) ")
        userCity = input("Have you traveled outside your city in the past 14 days? (Yes/No) ")
        userCountry = input("Have you traveled outside the country in the past 14 days? (Yes/No) ")

        contactTracing[registeredName] = {"Name" : userName, "Sex" : userSex, "Age" : userAge, "Address" : userAddress, "Contact number" : userContact, "COVID positive" : userPositive, "Cold history" : userCold, "Cough history" : userCough, "Commorbidities" : userCommorbidities, "Public contact" : userCrowded, "COVID contact" : userCovid, "Outside city" : userCity, "Outside country" : userCountry}

        print()
        print("\033[1;32;40mSaved successfully!\033[0m")

    # search an item in the dictionary
    elif userInput == 2:
        print()
        userSearch = input("Enter the name you want to search for: ")
        if userSearch in contactTracing:
            print()
            print("\033[1mPersonal Information\033[0m")
            print("Name: " + contactTracing[userSearch]["Name"])
            print("Age: " + contactTracing[userSearch]["Age"])
            print("Sex: " + contactTracing[userSearch]["Sex"])
            print("Address: " + contactTracing[userSearch]["Address"])
            print("Contact number: " + contactTracing[userSearch]["Contact number"])

            print()
            print("\033[1mHealth Information\033[0m")          
            print("COVID positive: " + contactTracing[userSearch]["COVID positive"])            
            print("Cold history: " + contactTracing[userSearch]["Cold history"])            
            print("Cough history: " + contactTracing[userSearch]["Cough history"])            
            print("Commorbidities: " + contactTracing[userSearch]["Commorbidities"])

            print()
            print("\033[1mTravel History\033[0m")
            print("Public contact: " + contactTracing[userSearch]["Public contact"])            
            print("COVID contact: " + contactTracing[userSearch]["COVID contact"])            
            print("Outside city: " + contactTracing[userSearch]["Outside city"])            
            print("Outside country:" + contactTracing[userSearch]["Outside country"])

        else:
            print()
            print("\033[1;31;40mNo record available.\033[0m")

    # exit the program
    elif userInput == 3:
        userExit = input("Do you want to exit the program? (YES/NO) ")
        if userExit.upper() == "YES":
            break
        elif userExit.upper() == "NO":
            continue

print()
print("Thank you.")