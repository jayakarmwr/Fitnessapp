import json
import os
import re


def registration():
    print('Create your account')
    d = dict()
    d["phone_number"] = input('Enter your phone number: ')
    d["name"] = input('Enter your name: ')
    d["password"] = pwd()
    d["gender"] = input('Enter your gender: ')
    d["age"] = input('Enter your age: ')
    d["active"] = activity()
    d["height"] = input('Enter your height in cm: ')
    d["weight"] = input('Enter your current weight in kgs: ')
    d["target_weight"] = input('Enter your target weight: ')
    users = read()
    for person in users:
        if person["name"] == d["name"]:
            print("This name is already registered with us. Please try a different username.")
            registration()
    else:
        users.append(d)
        write(users)
        print("Thank you for registering with us.\nEnjoy your fitness journey")
        login()


def login():
    print('Welcome to my fitness')
    name = input("Enter your name: ")
    password = input("Enter password: ")
    users = read()
    for person in users:
        if person["name"] == name and person["password"] == password:
            print("Login successful")
            print("Welcome", name,"\n")
            menu(name)
            break
    else:
        print("Login unsuccessful. Please try again\n")
        first_page()


def read():
    if os.path.exists("names.json"):
        with open("names.json", "r") as fp:
            try:
                info = json.load(fp)
            except json.decoder.JSONDecodeError:
                info = []
    else:
        info = []
    return info


def write(users):
    with open("names.json", "w") as fp:
        json.dump(users, fp)


def pwd():
    print("\nRules of the password:\ni) Minimum length is 6 characters and maximum length is 15 characters.\nii) It should have a minimum of one Capital Letter, One Small Letter, One digit and one special symbol\niii) Special symbols allowed are only (*, @, #)")
    s = input('Enter a password: ')
    flag = 0
    while True:
        if len(s) < 6 or len(s) > 15:
            flag = -1
            break
        elif not re.search('[a-z]', s):
            flag = -1
            break
        elif not re.search('[A-Z]', s):
            flag = -1
            break
        elif not re.search('[0-9]', s):
            flag = -1
            break
        elif not re.search('[*@#]', s):
            flag = -1
            break
        else:
            flag = 0
            break

    if flag == -1:
        print('Not a valid password')
        print('Please try a different password')
        pwd()
    if flag == 0:
        password = s
        return(password)


def activity():
    print('\nHow active are you?\n1.Little or No Activity\n2.Lightly Active\n3.Moderately Active\n4.Very Active')
    try:
        choice = int(input('Enter the option number: '))
        if choice == 1:
            act = "Little or No Activity"
            return act
        elif choice == 2:
            act = "Lightly Active"
            return act
        elif choice == 3:
            act = "Moderately Active"
            return act
        elif choice == 4:
            act = "Very Active"
            return act
        else:
            print("Invalid choice.\nPlease try again")
            activity()
    except:
        print("Invalid choice.\nPlease enter an integer")
        activity()


def menu(name):
    print("\nLet's begin with a workout or a diet plan")
    print("1.Workout plan\n2.Diet plan\n3.Log out")
    try:
        choice = int(input('Select what would you want to do? '))
        if choice == 1:
            workout(name)
        elif choice == 2:
            diet(name)
        elif choice == 3:
            print('You are being logged out')
            first_page()
        else:
            print("Invalid choice.\nPlease try again\n")
            menu(name)
    except:
        print("Invalid choice.\nPlease enter an integer\n")
        menu(name)

def workout(name):
    print("\nHere you go, the workouts are:")
    print("1.Our recommended workout plan for you\n2.Beginner workout routine\n3.Quick workout routine\n4.Intense workout routine\n5.Exercises for reducing belly fat\n6.Exercises for improving body posture\n7.Breathing exercises\n8.Workout routine for cardiac patients\n9.Return to main menu")
    try:
        choice = int(input("Choose according to your preference: "))
        if choice == 1:
            with open("names.json","r") as file:
                check=json.load(file)
            for i in check:
                if i["name"]==name:
                    if i["active"] == "Little or No Activity":
                        with open("beginner.json","r") as file:
                            d=json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a,b in d.items():
                            print(a)
                            for c,d in b.items():
                                print(c,":",d)
                            print()
                    elif i["active"] == "Lightly Active":
                        with open("beginner.json","r") as file:
                            d=json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a,b in d.items():
                            print(a)
                            for c,d in b.items():
                                print(c,":",d)
                            print()
                    if i["active"] == "Moderately Active":
                        with open("intense.json","r") as file:
                            d=json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a,b in d.items():
                            print(a)
                            for c,d in b.items():
                                print(c,":",d)
                            print()
                    elif i["active"] == "Very Active":
                        with open("intense.json","r") as file:
                            d=json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a,b in d.items():
                            print(a)
                            for c,d in b.items():
                                print(c,":",d)
                            print()
            print("Try another workout\n")
            workout(name)
        elif choice == 2:
            with open("beginner.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the beginner friendly workout.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 3:
            with open("quick.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the quick workout.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 4:
            with open("intense.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the intense workout.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 5:
            with open("belly_fat.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the workout that will help you reduce your belly fat.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 6:
            with open("body_posture.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the workout that will help you improve your body posture.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 7:
            with open("breathing_exercises.json", "r") as file:
                d=json.load(file)
            print("\n\nHere are some breathing exercises.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 8:
            with open("cardiac.json","r") as file:
                d=json.load(file)
            print("\n\nHere's the workout that will be helpful for cardiac patients.")
            for a,b in d.items():
                print(a)
                for c,d in b.items():
                    print(c,":",d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 9:
            print('You are being redirected to main menu\n')
            menu(name)
        else:
            print("Invalid choice.\nPlease try again")
            workout(name)
    except:
        print("Invalid choice.\nPlease enter an integer")
        workout(name)

def diet(name):
    print('\nThe following list contains various diet plans: ')
    print("1.Our recommended diet plan\n2.Weight loss diet plan\n3.Weight gain plan\n4.Balanced diet plan\n5.Protein rich diet plan\n6.Vegan diet plan\n7.Diet plan for Diabetes\n8.Diet plan for cardiac patients\n9.Return to main menu")
    try:
        choice = int(input('Choose according to your preference: '))
        if choice == 1:
            with open("names.json","r") as file:
                check=json.load(file)
            for i in check:
                if i["name"]==name:
                    if i["weight"]<i["target_weight"]:
                        with open("weight_gain.json","r") as file:
                            d=json.load(file)
                        day=input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a,b in d.items():
                            if day==a.lower():
                                print("For",a)
                                for c,d in b.items():
                                    print(c,":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
                    elif i["weight"]>i["target_weight"]:
                        with open("weight_loss.json","r") as file:
                            d=json.load(file)
                        day=input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a,b in d.items():
                            if day==a.lower():
                                print("For",a)
                                for c,d in b.items():
                                    print(c,":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
                    else:
                        with open("balanceddiet.json","r") as file:
                            d=json.load(file)
                        day=input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a,b in d.items():
                            if day==a.lower():
                                print("For",a)
                                for c,d in b.items():
                                    print(c,":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
        elif choice == 2:
            with open("weight_loss.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the weight loss diet plan for you.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 3:
            with open("weight_gain.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the weight diet plan for you.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 4:
            with open("balanceddiet.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the balanced diet plan for you.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 5:
            with open("protein_rich.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the protein rich diet plan for you.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 6:
            with open("vegan.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the vegan diet plan for you.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 7:
            with open("diabetic.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the diet plan appropriate for Diabetes.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 8:
            with open("cardiac_diet.json","r") as file:
                d=json.load(file)
            day=input("Specify the day of the week: ").lower()
            print("\nHere's the diet plan appropriate for Cardiac patients.")
            print("Hope you enjoy your meal!")
            for a,b in d.items():
                if day==a.lower():
                    print("For",a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans\n")
            diet(name)
        elif choice == 9:
            print('You are being redirected to main menu\n')
            menu(name)
        else:
            print("Invalid choice.\nPlease try again")
            diet(name)
    except:
        print("Invalid choice.\nPlease enter an integer")
        diet(name)


def analysis(name):




def first_page():
    try:
        option = int(input("\n1.Login\n2.Registration\n3.Exit out of the app\nChoose an option: "))
        if option == 1:
            login()
        elif option == 2:
            registration()
        elif option == 3:
            print("\nThank you")
            print("Please come back again")
        else:
            print("Invalid option")
            print("Try again")
            first_page()
    except:
        print("Please enter an integer")
        first_page()


first_page()
