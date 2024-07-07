import json
def menu(name):
    with open("names.json","r") as file:
        check=json.load(file)
    for i in check:
        if i["name"]==name:
            if i["weight"]<i["target_weight"]:
                with open("weight_gain.json","r") as file:
                    d=json.load(file)
                day=input("Specify the day of the week: ").lower()
                print("Here's the nutritionist recommended diet plan for you.")
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
            elif i["weight"]>i["target_weight"]:
                with open("weight_loss.json","r") as file:
                    d=json.load(file)
                print("Here's the nutritionist recommended diet plan for you.")
                print("Hope you enjoy your meal!")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break
            else:
                with open("balanceddiet.json","r") as file:
                    d=json.load(file)
                print("Here's the nutritionist recommended diet plan for you.")
                print("Hope you enjoy your meal!")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":")
                        for e in d:
                            print(e)
                        print()
                    print()
                    break

menu("Sanjeeva Sanku")
