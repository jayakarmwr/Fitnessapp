import json
def logout(name):
    with open("names.json","r") as file:
        json_obj=json.load(file)
    for i in range(len(json_obj)):
        if json_obj[i]["name"]==name:
            d=json_obj[i]
            break
    d["day"]=str(int(d["day"])+1)
    d["cal_walking"] = "0"
    d["cal_running"] = "0"
    d["cal_swimming"] = "0"
    d["cal_cycling"] = "0"
    d["sleep"] = "0"
    d["water"] = "0"
    json_obj.append(d)
    del json_obj[i]
    with open("names.json","w") as file:
        json.dump(json_obj,file)
logout("Sanjeeva")
