import json
def workout(name):
    with open("names.json","r") as file:
        check=json.load(file)
    for i in check:
        if i["name"]==name:
            if i["active"] == "Little or No Activity":
                with open("beginner.json","r") as file:
                    d=json.load(file)
                print("Here's a beginner friendly workout for you.")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":",d)
                    print()
            elif i["active"] == "Lightly Active":
                with open("beginner.json","r") as file:
                    d=json.load(file)
                print("Here's a beginner friendly workout for you.")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":",d)
                    print()
            if i["active"] == "Moderately Active":
                with open("intense.json","r") as file:
                    d=json.load(file)
                print("Here's a beginner friendly workout for you.")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":",d)
                    print()
            elif i["active"] == "Very Active":
                with open("intense.json","r") as file:
                    d=json.load(file)
                print("Here's a beginner friendly workout for you.")
                for a,b in d.items():
                    print(a)
                    for c,d in b.items():
                        print(c,":",d)
                    print()

workout("kota deepthi")
