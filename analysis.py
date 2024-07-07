import json
def analysis(name):
    print('Welcome to the tracker section')
    print('1.Calories burnt tracker\n2.Sleep tracker\n3.Water tracker\n4.Return to main menu')
    try:
        option = int(input("What would you like to do? "))
        if option == 1:
            calories(name)
        elif option == 2:
            sleep(name)
        elif option == 3:
            water(name)
        elif option == 4:
            print('You are being redirected to main menu\n')
            menu(name)
        else:
            print("Invalid option")
            print("Try again")
            analysis(name)
    except:
        print("Please enter an integer")
        analysis(name)

def calories(name):
    try:
        option = int(input("\n1.Calories burnt by walking\n2.Calories burnt by running\n3.Calories burnt by swimming\n4.Calories burnt by cycling\n5.Total calories burnt\n6.Return to tracker section\nChoose an option: "))
        if option == 1:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            s = float(input("Enter the speed in km/h:"))
            t = int(input("Enter the total time of walking(in min):"))
            d["cal_walking"] = str(int(t*(0.035*(int(d["weight"]))) +( pow((s*(5/18)),2)/ ((int(d["height"]))/100)*(0.029)*int(d["weight"]))))
            print("Number of calories burnt by walking are:",d["cal_walking"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 2:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            s = float(input("Enter the speed (in km/h):"))
            t = int(input("Enter the total time of running (in min):"))
            d["cal_running"] = str(int(s*t))
            print("Number of calories burnt by running are:",d["cal_running"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 3:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            laps = int(input("Enter the number of laps:"))
            d["cal_swimming"] = str(laps*17)
            print("Number of calories burnt by swimming are:",d["cal_swimming"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 4:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            s = float(input("Enter the speed (in km/h):"))
            t = int(input("Enter the total time of cycling (in min):"))
            d["cal_cycling"] = str(int(s*(t/60)*32))
            print("Number of calories burnt by cycling are:",d["cal_cycling"])
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 5:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            total_calories = int(d["cal_walking"]) + int(d["cal_running"]) + int(d["cal_swimming"]) + int(d["cal_cycling"])
            print("The total number of calories burnt are:",total_calories)
            print("Back to calories burnt tracker")
            calories(name)
        elif option == 6:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            calories(name)
    except:
        print("Please enter an integer")
        calories(name)

def water(name):
    try:
        option = int(input("\n1.See\n2.Update\n3.Return to tracker section\nChoose an option: "))
        if option == 1:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            print("You have drunk",d["water"],"glasses of water today\n")
            print("Back to water tracker")
            water(name)
        elif option == 2:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            n=int(input("How many glasses of water did you drink? "))
            d["water"] = str(n)
            print("You have drunk",d["water"],"glasses of water today\n")
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to water tracker")
            water(name)
        elif option == 3:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            water(name)
    except:
        print("Please enter an integer")
        water(name)


def sleep(name):
    try:
        option = int(input("\n1.See\n2.Update\n3.Return to tracker section\nChoose an option: "))
        if option == 1:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            print("You had",d["sleep"],"hours of sleep today\n")
            print("Back to sleep tracker")
            sleep(name)
        elif option == 2:
            with open("names.json","r") as file:
                json_obj=json.load(file)
            for i in range(len(json_obj)):
                if json_obj[i]["name"]==name:
                    d=json_obj[i]
                    break
            n=int(input("How many hours did you sleep today? "))
            d["sleep"] = str(n)
            print("You had",d["sleep"],"hours of sleep today\n")
            json_obj.append(d)
            del json_obj[i]
            with open("names.json","w") as file:
                json.dump(json_obj,file)
            print("Back to sleep tracker")
            sleep(name)
        elif option == 3:
            print("\nTry other trackers")
            analysis(name)
        else:
            print("Invalid option")
            print("Try again")
            sleep(name)
    except:
        print("Please enter an integer")
        water(name)

analysis("Sanjeeva Sanku")
