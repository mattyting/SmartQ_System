import os
import time
from random import randint
from datetime import datetime, timedelta
rdate = datetime.today()
t24 = int(rdate.strftime("%H%M"))  
t = 0
avti = { 800:"08:00 AM",  83: "08:20 AM",  840: "08:40 AM",
         900:"09:00 AM",  93: "09:20 AM",  940: "09:40 AM",
        1000:"10:00 AM", 103: "10:20 AM", 1040: "10:40 AM",
        1100:"11:00 AM", 113: "11:20 AM", 1140: "11:40 AM",
        1300:"01:00 PM", 133: "01:20 PM", 1340: "01:40 PM",
        1400:"02:00 PM", 143: "02:20 PM", 1440: "02:40 PM",
        1500:"03:00 PM", 153: "03:20 PM", 1540: "03:40 PM"}
otime = avti.keys()
otime = tuple(otime)
allpsc = []
pnumid,pstatus = {},{}
pnumid,pstatus = dict(pnumid),dict(pstatus)
allnam,allage,allbir,allgen,alladd,allcel,allpnu,allpsc = [],[],[],[],[],[],[],[]
def mode():
    os.system('cls')
    while True:
        os.system('cls')
        print(" ".center(1700))
        print(" "*67+"╔════════════════════════════╗")
        print(" "*67+"║         Main Menu          ║")
        print(" "*67+"╟────────────────────────────╢")
        print(" "*67+"║ [1] Patient Mode           ║")
        print(" "*67+"║ [2] Admin Mode             ║")
        print(" "*67+"║ [3] Exit                   ║")
        print(" "*67+"╚════════════════════════════╝")
        try:
            ch = int(input(" "*67+"Enter number of your Choice: "))  
            if ch == 1:
                os.system('cls')
                patient_mode()
                os.system('cls')
            elif ch == 2:
                os.system('cls')
                admin_mode()
                os.system('cls')
            elif ch == 3:
                break
            else:
                print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(" "*67+"┃        Ivalid choice       ┃") 
                print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                time.sleep(1.25)
        except ValueError:
            print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(" "*67+"┃  Please Enter Number Only  ┃") 
            print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            time.sleep(1.25)
def patient_mode():
    while True:
        os.system('cls')
        print(" ".center(1700))
        print(" "*67+"╔════════════════════════════╗")
        print(" "*67+"║        Patient Mode        ║")
        print(" "*67+"╟────────────────────────────╢")
        print(" "*67+"║ [1] Add Patient in Queue   ║")
        print(" "*67+"║ [2] View Patient Schedule  ║")
        print(" "*67+"║ [3] Back to Main Menu      ║")
        print(" "*67+"╚════════════════════════════╝")
        try:
            ch = int(input(" "*67+"Enter number of your Choice: "))
            if ch == 1:
                os.system('cls')
                add_patient_in_queue()
                os.system('cls')
            elif ch == 2:
                os.system('cls')
                view_patient_schedule()
                os.system('cls')
            elif ch == 3:
                break
            else:
                print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(" "*67+"┃        Ivalid choice       ┃") 
                print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                time.sleep(1.25)
        except ValueError:
            print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(" "*67+"┃  Please Enter Number Only  ┃") 
            print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            time.sleep(1.25)
    return
def in_info(question):
    while True:
        res = input(question).title()
        if question == " "*52+"Name"+(" "*18)+": " or question == " "*52+"Address"+(" "*15)+": ":
            if res.isdigit():
                print(" "*52+"Please Use Letters")
            else:
                break
        if question == " "*52+"Age"+(" "*19)+": ":
            if res.isdigit():
                if int(res) > 130:
                    print(" "*52+"Invalid age")
                else:
                    res == res
                    break
            else:
                print(" "*52+"Please Use numbers")
        elif question == " "*52+"Phone Number"+(" "*10)+": ":
            if res.isdigit():
                if len(res) != 11:
                    print(" "*52+"Invalid number")
                else:
                    res == res
                    break
            elif res == "":
                print(" "*52+"Please Fill in")   
        elif question == " "*52+"Gender(M/F)"+(" "*11)+": ":
            if res.isalpha():
                if res == 'Male' or res == 'Female'  or res == 'M' or res == 'F':
                    if res == 'M':
                        res = "Male"
                        break
                    elif res == 'F':
                        res = "Female"
                        break
                else:
                    print(" "*52+"Invalid Gender")
            else:
                print(" "*52+"Please Use Letters ")
        elif question == " "*52+"Birthdate(YYYY-MM-DD) : ":
            if res[0:4].isdigit() and int(res[0:4]) > 1900  and int(res[0:4]) < 2025 and (res[4:5] == " "or res[4:5] =='/'or res[4:5] == '-') and res[5:7].isdigit() and int(res[5:7]) >= 1 and int(res[5:7])  <= 12 and (res[4:5] == " "or res[4:5] =='/'or res[4:5] == '-') and res[8:10].isdigit() and int(res[8:10]) >= 1 and int(res[8:10])  <= 31:
                res = res[0:4]+"-"+res[5:7]+"-"+res[8:10]
                break
            else:
                print(" "*52+"Invalid Date")
        elif question == "":
            print(" "*52+"Please fill in")
    return res
def ge_pnu():
    pid = ""
    for i in range(4):
        rnum=str(randint(0,9))
        pid+=rnum
    return pid
def ge_psc():       
    global rdate
    global t
    global t24
    if len(allpsc) == 0: #if wala pa naka una sa karon na time
        while t < len(otime) and otime[t] < t24:
            t += 1
        if t >= len(otime):
            rdate = rdate + timedelta(days=1)
            t = 0
        sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
        t += 1
        return sch
    elif len(allpsc) != 0: #if naa nay ga una and mag based sa ga una og sa oras sheshhhhh     
        lst = allpsc[-1][11:]
        lst_key = None
        for k, v in avti.items(): #ari akong gi kuha ang last nga time og akoa sab gi kuha kong unsa iyaang key 
            if v == lst:
                lst_key = k
                break
        if lst_key is not None and otime.index(lst_key) < len(otime) - 1: #compare an key sa last
            t = otime.index(lst_key) + 1
            sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
            t += 1
            return sch
        else:
            rdate = rdate + timedelta(days=1)
            t = 0
            sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
            t += 1
            return sch
def add_patient_in_queue():
    i=0
    while True:
        os.system('cls')
        print(" "*50+"╔══════════════════════════════════════════════════════════╗")
        print(" "*50+"║                     Book Appointment                     ║")
        print(" "*50+"╚══════════════════════════════════════════════════════════╝")
        inna = in_info(" "*52+"Name"+(" "*18)+": ")
        inag = in_info(" "*52+"Age"+(" "*19)+": ")
        inge = in_info(" "*52+"Gender(M/F)"+(" "*11)+": ")
        inbi = in_info(" "*52+"Birthdate(YYYY-MM-DD) : ")
        ince = in_info(" "*52+"Phone Number"+(" "*10)+": ")
        inad = in_info(" "*52+"Address"+(" "*15)+": ")
        p_info = [inna,inag,inge,inbi,ince,inad]
        label = ["Name:","Age:","Gender:","Birthdate:","Phone Num:","Address:"] 
        while True:   
            os.system('cls') 
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+"║                     Book Appointment                     ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
            for e_info in p_info:
                print(" "*50+"│ "+label[i]+(" "*(11-len(label[i])))+"│ "+e_info+(" "*(43-len(e_info)))+"│")
                i+=1
            i=0
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+"║            [1]Re Fillup             [2]Submit            ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
            try:
                ch = int(input(" "*52+"Enter your choice: "))
                if ch == 1:
                    break
                elif ch == 2:
                    break
                else:                        
                    print(" "*50+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                    print(" "*50+"┃                      Ivalid choice                       ┃") 
                    print(" "*50+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                    time.sleep(1.25)
            except ValueError:
                print(" "*50+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(" "*50+"┃                 Please Enter Number Only                 ┃") 
                print(" "*50+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                time.sleep(1.25)
        if ch == 1:
                continue
        elif ch == 2:
                break
    gepn = ge_pnu()
    geps = ge_psc()
    pnumid.update({gepn:[inna,inag,inge,inbi,ince,inad,geps]})
    pstatus.update({gepn:[geps,inna,inag,inge,inbi,ince,inad,"Pending"]})
    allnam.append(inna)
    allage.append(inag)
    allbir.append(inbi) 
    allgen.append(inge)
    alladd.append(inad)
    allcel.append(ince)
    allpnu.append(gepn)
    allpsc.append(geps)
    print(" "*50+"╔══════════════════════════════════════════════════════════╗")
    print(" "*50+"║                Patient Booked Successfully               ║")
    print(" "*50+"║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║")
    print(" "*50+f"║ Save your Patient Number : {gepn}                          ║")
    print(" "*50+f"║ Your Schedule            : {geps}           ║")
    print(" "*50+"╚══════════════════════════════════════════════════════════╝")
    input(" "*52+"Press Enter to Proceed")
    os.system('cls')
def view_patient_schedule():
    print(" "*50+"╔══════════════════════════════════════════════════════════╗")
    print(" "*50+"║                   View Patient Schedule                  ║")
    print(" "*50+"╚══════════════════════════════════════════════════════════╝")
    entry = input(" "*52+"Enter Your Patient Number: ")
    if entry in allpnu:
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+f"║ Patient Number: {entry}                                     ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
            print(" "*50+"│ Name      : "+pstatus.get(entry)[1]+(" "*(45-len(pstatus.get(entry)[1])))+"│")
            print(" "*50+"│ Age       : "+pstatus.get(entry)[2]+(" "*(45-len(pstatus.get(entry)[2])))+"│")
            print(" "*50+"│ Gender    : "+pstatus.get(entry)[3]+(" "*(45-len(pstatus.get(entry)[3])))+"│")
            print(" "*50+"│ Birthdate : "+pstatus.get(entry)[4]+(" "*(45-len(pstatus.get(entry)[4])))+"│")
            print(" "*50+"│ Phone Num : "+pstatus.get(entry)[5]+(" "*(45-len(pstatus.get(entry)[5])))+"│")
            print(" "*50+"│ Address   : "+pstatus.get(entry)[6]+(" "*(45-len(pstatus.get(entry)[6])))+"│")
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+"║ Your Schedule : "+pstatus.get(entry)[0]+(" "*(41-len(pstatus.get(entry)[0])))+"║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
    else:
        print(" "*50+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" "*50+"┃                 Patient number not found                 ┃") 
        print(" "*50+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        time.sleep(1.25)
    input(" "*52+"Press Enter to proceed")
def admin_mode():
    while True:
        os.system('cls')
        print(" ".center(1700))
        print(" "*67+"╔════════════════════════════╗")
        print(" "*67+"║         Admin Mode         ║")
        print(" "*67+"╟────────────────────────────╢")
        print(" "*67+"║ [1] View Patient Queue     ║")
        print(" "*67+"║ [2] Check Patient          ║")
        print(" "*67+"║ [3] Back to Main Menu      ║")
        print(" "*67+"╚════════════════════════════╝")
        try:
            ch = int(input(" "*67+"Enter number of your Choice: "))
            if ch == 1:
                os.system('cls')
                view_patients_queue()
                os.system('cls')
            elif ch == 2:
                os.system('cls')
                view_next()
                os.system('cls')
            elif ch == 3:
                break 
            else:
                print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(" "*67+"┃        Ivalid choice       ┃") 
                print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                time.sleep(1.25)
        except ValueError:
            print(" "*67+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(" "*67+"┃  Please Enter Number Only  ┃") 
            print(" "*67+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            time.sleep(1.25)
    return
def view_patients_queue():
    s=0
    space = [22, 32, 4, 7, 12, 13, 36, 11]    
    print(" "*3+"╔"+("═"*152)+"╗")
    print(" "*3+"║"+(" "*69)+"Patient Queue"+(" "*70+"║"))
    print(" "*3+"╟"+("─"*152)+"╢")
    print(" "*3+"║ Health Check Schedule ┃"+(" "*14)+"Name"+(" "*15)+"┃ Age ┃ Gender ┃  Birthdate  ┃ Phone number ┃"+(" "*15)+"Address"+(" "*15)+"┃   Status   ║")
    print(" "*3+"╟"+("─"*152)+"╢")
    for r in pstatus.values():
        for c in r:
            if space[s] == 11:
                print("┃ "+c+(" "*(space[s] -len(c)))+"║",end="")
            elif space[s] == 22:
                print(" "*3+"║ "+c+(" "*(space[s] -len(c))),end="")
            else:
             print("┃ "+c+(" "*(space[s] -len(c))),end="")
            s+=1
        s=0
        print()
    print(" "*3+"╚"+("═"*152)+"╝")
    input(" "*5+"Press Enter to Proceed")
def view_next():
    ch = 0
    i = 0
    label = ["Name:","Age:","Gender:","Birthdate:","Phone Num:","Address:","Schedule:"]
    while True:
        if len(allpnu) != 0:
            os.system('cls') 
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+f"║ Patient Number: {allpnu[0]}                                     ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
            for info in pnumid.get(allpnu[0]):
                print(" "*50+"┃ "+label[i]+(" "*(11-len(label[i])))+"┃ "+info+(" "*(44-len(info)))+"┃")
                i+=1
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+"║      [1] Exit      [2]Unattended      [3] Attended       ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")
            ch=int(input(" "*52+"  Enter your choice: "))
            if ch == 1:
                break
            elif ch == 2:
                pstatus.get(allpnu[0])[7] = "Unattended"
                allpnu.remove(allpnu[0])
            elif ch == 3:
                pstatus.get(allpnu[0])[7] = "Attended"
                allpnu.remove(allpnu[0])
            i=0
        else:
            os.system('cls')
            print(" ".center(2000))
            print(" "*50+"╔══════════════════════════════════════════════════════════╗")
            print(" "*50+"║                Currently No Next Patient                 ║")
            print(" "*50+"╚══════════════════════════════════════════════════════════╝")                                      
            input(" "*52+"Enter to proceed")
            break
#Done
if __name__ == '__main__':
    mode()