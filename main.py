import json
import os
import re

def registration():
    print('Create your account')
    d = dict()
    d["phone_number"] = phone()
    d["name"] = input('Enter your name: ')
    d["password"] = pwd()
    d["gender"] = gender()
    d["age"] = age()
    d["active"] = activity()
    d["height"] = height()
    d["weight"] = weight()
    d["target_weight"] = target_weight()
    d["cal_walking"] = "0"
    d["cal_running"] = "0"
    d["cal_swimming"] = "0"
    d["cal_cycling"] = "0"
    d["sleep"] = "0"
    d["water"] = "0"
    d["day"] = "1"
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
    name = input("Enter your name: ")
    password = input("Enter password: ")
    users = read()
    for person in users:
        if person["name"] == name and person["password"] == password:
            print("Login successful")
            print("Welcome", name, "\n")
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            print("Embark Day", d["day"], "of your fitness journey")
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
        return pwd()
    elif flag == 0:
        return s


def phone():
    n = input('Enter your phone number:+91 ')
    if len(n)==10:
        if not re.match('[6-9]{1}[0-9]{9}', n):
            print("Invalid number.Try again")
            return phone()
        else:
            return n
    else:
        print("Invalid number.Try again")
        return phone()


def activity():
    print('\nHow active are you?\n1.Little or No Activity\n2.Lightly Active\n3.Moderately Active\n4.Very Active')
    try:
        choice = int(input('Enter the option number:').strip())
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
            return activity()
    except ValueError:
        print("Invalid choice.\nPlease enter an integer")
        return activity()


def age():
    try:
        n=int(input("Enter Your Age(12 years or above):"))
        if n >= 12:
            return str(n)
        else:
            print("Invalid age")
            return age()
    except ValueError:
        print("Invalid age")
        return age()


def height():
    try:
        n=int(input("Enter your height in cm:"))
        if n >= 91:
            return str(n)
        else:
            print("That's wrong. Try again")
            return height()
    except ValueError:
        print("That's wrong. Try again")
        return height()


def weight():
    try:
        n=int(input("Enter your weight in kgs:"))
        if n > 0:
            return str(n)
        else:
            print("That's wrong. Try again")
            return weight()
    except ValueError:
        print("That's wrong. Try again")
        return weight()


def target_weight():
    try:
        n=int(input("Enter your target weight in kgs:"))
        if n > 0:
            return str(n)
        else:
            print("That's wrong. Try again")
            return target_weight()
    except ValueError:
        print("That's wrong. Try again")
        return target_weight()


def gender():
    n=input("Specify your gender(Male\Female):").lower()
    if n == "male" or n == "female":
        return n
    else:
        print("Try again")
        return gender()


def menu(name):
    print("\nLet's begin with a workout or a diet plan")
    print("1.Workout plan\n2.Diet plan\n3.Activity Tracker\n4.Edit Your Profile\n5.Log out")
    try:
        choice = int(input('Select what would you want to do?').strip())
        if choice == 1:
            workout(name)
        elif choice == 2:
            diet(name)
        elif choice == 3:
            analysis(name)
        elif choice == 4:
            edit(name)
        elif choice == 5:
            print('You are being logged out')
            logout(name)
            first_page()
        else:
            print("Invalid choice.\nPlease try again\n")
            menu(name)
    except ValueError:
        print("Invalid choice.\nPlease enter an integer\n")
        menu(name)


def edit(name):
    print("\nHere's your profile\n")
    with open("names.json", "r") as file:
        json_obj = json.load(file)
    for i in range(len(json_obj)):
        if json_obj[i]["name"] == name:
            d = json_obj[i]
            break
    print("Username:", d["name"])
    print("Phone Number:", d["phone_number"])
    print("Password:", d["password"])
    print("Gender:", d["gender"])
    print("Age:", d["age"])
    print("Activity:", d["active"])
    print("Height:", d["height"])
    print("Current Weight:", d["weight"])
    print("Target Weight:", d["target_weight"])
    print()
    print("NOTE:You can't change your username.")
    print("You can edit the following details.")
    m = True
    while m:
        print('\n1.Phone Number\n2.Password\n3.Gender\n4.Age\n5.Activity\n6.Height\n7.Weight\n8.Target Weight\n9.Return to Main Menu\n')
        try:
            option = int(input("\nChoose an option:").strip())
            if option == 1:
                d["phone_number"] = phone()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 2:
                d["password"] = pwd()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 3:
                d["gender"] = gender()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 4:
                d["age"] = age()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 5:
                d["active"] = activity()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 6:
                d["height"] = height()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 7:
                d["weight"] = weight()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 8:
                d["target_weight"] = target_weight()
                json_obj.append(d)
                del json_obj[i]
                with open("names.json", "w") as file:
                    json.dump(json_obj, file)
            elif option == 9:
                print("You are being redirected to Main Menu")
                m = False
                menu(name)
            else:
                print("Invalid option")
                print("Try again")
                edit(name)
        except ValueError:
            print("Please enter an integer")
            edit(name)


def workout(name):
    print("\nHere you go, the workouts are:")
    print("1.Our recommended workout plan for you\n2.Beginner workout routine\n3.Quick workout routine\n4.Intense workout routine\n5.Exercises for reducing belly fat\n6.Exercises for improving body posture\n7.Breathing exercises\n8.Workout routine for cardiac patients\n9.Return to main menu")
    try:
        choice = int(input("Choose according to your preference:").strip())
        if choice == 1:
            with open("names.json", "r") as file:
                check = json.load(file)
            for i in check:
                if i["name"] == name:
                    if i["active"] == "Little or No Activity":
                        with open("beginner.json", "r") as file:
                            d = json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a, b in d.items():
                            print(a)
                            for c, d in b.items():
                                print(c, ":", d)
                            print()
                    elif i["active"] == "Lightly Active":
                        with open("beginner.json", "r") as file:
                            d = json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a, b in d.items():
                            print(a)
                            for c, d in b.items():
                                print(c, ":", d)
                            print()
                    if i["active"] == "Moderately Active":
                        with open("intense.json", "r") as file:
                            d = json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a, b in d.items():
                            print(a)
                            for c, d in b.items():
                                print(c, ":", d)
                            print()
                    elif i["active"] == "Very Active":
                        with open("intense.json", "r") as file:
                            d = json.load(file)
                        print("\n\nHere's our recommended workout for you.")
                        for a, b in d.items():
                            print(a)
                            for c, d in b.items():
                                print(c, ":", d)
                            print()
            print("Try another workout\n")
            workout(name)
        elif choice == 2:
            with open("beginner.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the beginner friendly workout.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 3:
            with open("quick.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the quick workout.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 4:
            with open("intense.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the intense workout.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 5:
            with open("belly_fat.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the workout that will help you reduce your belly fat.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 6:
            with open("body_posture.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the workout that will help you improve your body posture.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 7:
            with open("breathing_exercises.json", "r") as file:
                d = json.load(file)
            print("\n\nHere are some breathing exercises.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 8:
            with open("cardiac.json", "r") as file:
                d = json.load(file)
            print("\n\nHere's the workout that will be helpful for cardiac patients.")
            for a, b in d.items():
                print(a)
                for c, d in b.items():
                    print(c, ":", d)
                print()
            print("Try another workout\n")
            workout(name)
        elif choice == 9:
            print('You are being redirected to main menu\n')
            menu(name)
        else:
            print("Invalid choice.\nPlease try again")
            workout(name)
    except ValueError:
        print("Invalid choice.\nPlease enter an integer")
        workout(name)


def diet(name):
    print('\nThe following list contains various diet plans: ')
    print(
        "1.Our recommended diet plan\n2.Weight loss diet plan\n3.Weight gain plan\n4.Balanced diet plan\n5.Protein rich diet plan\n6.Vegan diet plan\n7.Diet plan for Diabetes\n8.Diet plan for cardiac patients\n9.Return to main menu")
    try:
        choice = int(input('Choose according to your preference:').strip())
        if choice == 1:
            with open("names.json", "r") as file:
                check = json.load(file)
            for i in check:
                if i["name"] == name:
                    if int(i["weight"]) < int(i["target_weight"]):
                        with open("weight_gain.json", "r") as file:
                            d = json.load(file)
                        day = input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a, b in d.items():
                            if day == a.lower():
                                print("For", a)
                                for c, d in b.items():
                                    print(c, ":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
                    elif int(i["weight"]) > int(i["target_weight"]):
                        with open("weight_loss.json", "r") as file:
                            d = json.load(file)
                        day = input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a, b in d.items():
                            if day == a.lower():
                                print("For", a)
                                for c, d in b.items():
                                    print(c, ":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
                    else:
                        with open("balanceddiet.json", "r") as file:
                            d = json.load(file)
                        day = input("Specify the day of the week: ").lower()
                        print("\nHere's the nutritionist recommended diet plan for you.")
                        print("Hope you enjoy your meal!")
                        for a, b in d.items():
                            if day == a.lower():
                                print("For", a)
                                for c, d in b.items():
                                    print(c, ":")
                                    for e in d:
                                        print(e)
                                    print()
                                print()
                                break
                        print("Try checking out other diet plans")
                        print()
                        diet(name)
        elif choice == 2:
            with open("weight_loss.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the weight loss diet plan for you.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 3:
            with open("weight_gain.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the weight diet plan for you.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 4:
            with open("balanceddiet.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the balanced diet plan for you.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 5:
            with open("protein_rich.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the protein rich diet plan for you.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 6:
            with open("vegan.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the vegan diet plan for you.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 7:
            with open("diabetic.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the diet plan appropriate for Diabetes.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            print("Try checking out other diet plans")
            print()
            diet(name)
        elif choice == 8:
            with open("cardiac_diet.json", "r") as file:
                d = json.load(file)
            day = input("Specify the day of the week: ").lower()
            print("\nHere's the diet plan appropriate for Cardiac patients.")
            print("Hope you enjoy your meal!")
            for a, b in d.items():
                if day == a.lower():
                    print("For", a)
                    for c, d in b.items():
                        print(c, ":")
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
    print('\nWelcome to the tracker section')
    print('1.Calories burnt tracker\n2.Sleep tracker\n3.Water tracker\n4.Weight tracker\n5.Return to main menu')
    try:
        option = int(input("What would you like to do?").strip())
        if option == 1:
            calories(name)
        elif option == 2:
            sleep(name)
        elif option == 3:
            water(name)
        elif option == 4:
            weight_tracker(name)
        elif option == 5:
            print('You are being redirected to main menu\n')
            menu(name)
        else:
            print("Invalid option")
            print("Try again")
            analysis(name)
    except ValueError:
        print("Please enter an integer")
        analysis(name)


def weight_tracker(name):
    with open("names.json", "r") as file:
        json_obj = json.load(file)
    for i in range(len(json_obj)):
        if json_obj[i]["name"] == name:
            d = json_obj[i]
            break
    print("\nYour Current Weight is", d["weight"], "kgs")
    print("Your Target Weight is", d["target_weight"], "kgs")
    if int(d["weight"]) == int(d["target_weight"]):
        print("Congratulations, you've achieved your target weight.")
        print("You have done a really good job.Keep going!!!")
    elif int(d["weight"]) > int(d["target_weight"]):
        print("Try out workout plans and diet plans to reduce weight")
        print("You can do it.Come on!!!")
    elif int(d["weight"]) < int(d["target_weight"]):
        print("Try out workout plans and diet plans to gain weight")
        print("You can do it.Come on!!!\n")
    print("Try other trackers\n")
    analysis(name)


def calories(name):
    try:
        option = int(input("\n1.Calories burnt by walking\n2.Calories burnt by running\n3.Calories burnt by swimming\n4.Calories burnt by cycling\n5.Total calories burnt\n6.Return to tracker section\nChoose an option:").strip())
        if option == 1:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            s = float(input("Enter the speed in km/h:"))
            t = int(input("Enter the total time of walking(in min):"))
            d["cal_walking"] = str(int(t * (0.035 * (int(d["weight"]))) + (pow((s * (5 / 18)), 2) / ((int(d["height"])) / 100) * 0.029 * int(d["weight"]))))
            print("Number of calories burnt by walking are:", d["cal_walking"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 2:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            s = float(input("Enter the speed (in km/h):"))
            t = int(input("Enter the total time of running (in min):"))
            d["cal_running"] = str(int(s * t))
            print("Number of calories burnt by running are:", d["cal_running"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 3:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            laps = int(input("Enter the number of laps:"))
            d["cal_swimming"] = str(laps * 17)
            print("Number of calories burnt by swimming are:", d["cal_swimming"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 4:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            s = float(input("Enter the speed (in km/h):"))
            t = int(input("Enter the total time of cycling (in min):"))
            d["cal_cycling"] = str(int(s * (t / 60) * 32))
            print("Number of calories burnt by cycling are:", d["cal_cycling"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 5:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            total_calories = int(d["cal_walking"]) + int(d["cal_running"]) + int(d["cal_swimming"]) + int(
                d["cal_cycling"])
            print("The total number of calories burnt are:", total_calories)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 6:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            calories(name)
    except ValueError:
        print("Please enter an integer")
        calories(name)


def water(name):
    try:
        option = int(input("\n1.See\n2.Update\n3.Return to tracker section\nChoose an option:").strip())
        if option == 1:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            print("You have drunk", d["water"], "glasses of water today\n")
            if int(d["water"]) < 6:
                print("Drink",(6-int(d["water"])),"more glasses of water to meet required amount")
            else:
                print("Hurray!You reached your goal")
            print("Back to water tracker")
            water(name)
        elif option == 2:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            n = int(input("How many glasses of water did you drink? "))
            d["water"] = str(n)
            print("You have drunk", d["water"], "glasses of water today\n")
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            if int(d["water"]) < 6:
                print("Drink",(6-int(d["water"])),"more glasses of water to meet required amount")
            else:
                print("Hurray!You reached your goal")
            print("Back to water tracker")
            water(name)
        elif option == 3:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            water(name)
    except ValueError:
        print("Please enter an integer")
        water(name)


def sleep(name):
    try:
        option = int(input("\n1.See\n2.Update\n3.Return to tracker section\nChoose an option:").strip())
        if option == 1:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            print("You had", d["sleep"], "hours of sleep today\n")
            if int(d["age"]) in range(12,16):
                if int(d["sleep"]) < 10:
                    print("You need to sleep",(10-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            elif int(d["age"]) in range(16,19):
                if int(d["sleep"]) < 8:
                    print("You need to sleep",(8-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            else:
                if int(d["sleep"]) < 7:
                    print("You need to sleep",(7-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            print("Back to sleep tracker")
            sleep(name)
        elif option == 2:
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            n = int(input("How many hours did you sleep today? "))
            d["sleep"] = str(n)
            print("You had", d["sleep"], "hours of sleep today\n")
            json_obj.append(d)
            del json_obj[i]
            with open("names.json", "w") as file:
                json.dump(json_obj, file)
            with open("names.json", "r") as file:
                json_obj = json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"] == name:
                    d = json_obj[i]
                    break
            if int(d["age"]) in range(12,16):
                if int(d["sleep"]) < 10:
                    print("You need to sleep",(10-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            elif int(d["age"]) in range(16,19):
                if int(d["sleep"]) < 8:
                    print("You need to sleep",(8-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            else:
                if int(d["sleep"]) < 7:
                    print("You need to sleep",(7-int(d["sleep"])),"more hours.")
                else:
                    print("Good job! You have got enough sleep today.")
            print("Back to sleep tracker")
            sleep(name)
        elif option == 3:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            sleep(name)
    except ValueError:
        print("Please enter an integer")
        water(name)


def logout(name):
    with open("names.json", "r") as file:
        json_obj = json.load(file)
    for i in range(len(json_obj)):
        if json_obj[i]["name"] == name:
            d = json_obj[i]
            break
    d["day"] = str(int(d["day"]) + 1)
    d["cal_walking"] = "0"
    d["cal_running"] = "0"
    d["cal_swimming"] = "0"
    d["cal_cycling"] = "0"
    d["sleep"] = "0"
    d["water"] = "0"
    json_obj.append(d)
    del json_obj[i]
    with open("names.json", "w") as file:
        json.dump(json_obj, file)

def first_page():
    try:
        option = int(input("\n1.Login\n2.Registration\n3.Exit out of the app\nChoose an option:").strip())
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
    except ValueError:
        print("Please enter an integer")
        first_page()


first_page()
