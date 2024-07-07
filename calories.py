#cal tracking
import json
with open("names.json","r") as file:
    json_obj=json.load(file)
    d=json_obj[0]
total_cal_burnt=0
cal1=0
cal2=0
cal3=0
cal4=0
if(d["weight"]>d["target_weight"]):
    print("1.calories burnt by walking")
    print("2.calories burnt by swimming")
    print("3.calories burnt by cycling")
    print("4.calories burnt by running")
    n=int(input("Enter your choice:"))

    if (n==1):
        n=int(input("Enter the distance in km :"))
        s=float(input("Enter the speed in km/h:"))
        t=int(input("Enter the total time of walking(in min):"))
        cal1=t*(0.035*(int(d["weight"]))) +( pow((s*(5/18)),2)/ ((int(d["height"]))/100)*(0.029)*int(d["weight"]))
        total_cal_burnt=total_cal_burnt+cal1
        print("The total cal burnt by walking is: %.3f"%cal)
    if(n==2):
        s=int(input("Enter the number of laps:"))
        cal2=s*17
        print("The total cal burnt by swimming is: %.3f"%cal)
        total_cal_burnt=total_cal_burnt+cal2
    if(n==3):
        s=float(input("Enter the speed in km/h:"))
        t=int(input("Enter time in min:"))
        d=s*t
        cal3=d*32
        total_cal_burnt=total_cal_burnt+cal3
        print("The total cal burnt by cycling is: %.3f"%cal)
    if(n==4):
        s=float(input("Enter the speed in km/h:"))
        t=int(input("Enter time in min:"))
        d=s*t
        cal4=d*60
        total_cal_burnt=total_cal_burnt+cal4
        print("The total cal burnt by running is: %.3f"%cal)
d["total_cal_burnt"]=total_cal_burnt
d["cal_walking"]=cal1
d["cal_swimming"]=cal2
d["cal_cycling"]=cal3
d["cal_running"]=cal4

json_obj.append(d)
with open("names.json","a") as file:
    json.dump(json_obj,file)
