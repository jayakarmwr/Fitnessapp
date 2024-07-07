import json
def edit(name):
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
    flag = 0
    while m:
        print('\n1.Phone Number\n2.Password\n3.Gender\n4.Age\n5.Activity\n6.Height\n7.Weight\n8.Target Weight\n9.Return to Main Menu\n')
        try:
            option = int(input("\nChoose an option: "))
            if option == 1:
                d["phone_number"] = phone()
            elif option == 2:
                d["password"] = pwd()
            elif option == 3:
                d["gender"] = input('Enter your gender: ')
            elif option == 4:
                d["age"] = input('Enter your age: ')
            elif option == 5:
                d["active"] = activity()
            elif option == 6:
                d["height"] = input('Enter your height in cm: ')
            elif option == 7:
                d["weight"] = input('Enter your current weight in kgs: ')
            elif option == 8:
                d["target_weight"] = input('Enter your target weight: ')
            elif option == 9:
                json_obj.append(d)
                del json_obj[i]
                with open("names.json","w") as file:
                    json.dump(json_obj,file)
                print("You are being redirected to Main Menu")
                m = False
                menu(name)
            else:
                print("Invalid option")
                print("Try again")
                edit(name)
        except:
            print("Please enter an integer")
            edit(name)


