#
# Created by Berke Akyıldız on 20/September/2019
#
import datetime

core = int(input("Enter current core mmr:\n"))
support = int(input("Enter current support mmr:\n"))
file = open("mmr.txt", "a+")

boolean = True
coreChange = 0
supportChange = 0
while(boolean):
    write = ""
    inp = int(input("Enter 1 for core, 2 for support:\n"))

    if inp == 1:
        match = input("Enter w for win, l for lose:\n")
        hero = input("Enter hero name:\n")
        if match == "w":
            change = int(input("Enter current mmr:\n"))
            mmr = change - core
            coreChange += mmr
            core = change
            supportChange += 10
            support += 10
            write = "+" + str(mmr) + "  CORE  WIN  with " + hero + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


        elif match == "l":
            change = int(input("Enter current mmr:\n"))
            mmr = core - change
            coreChange -= mmr
            core = change
            supportChange -= 10
            support -= 10
            write = "-" + str(mmr) + "  CORE  LOSE  with " + hero + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    elif inp == 2:
        match = input("Enter w for win, l for lose:\n")
        hero = input("Enter hero name:\n")
        if match == "w":
            change = int(input("Enter current mmr:\n"))
            mmr = change - support
            supportChange += mmr
            support = change
            coreChange += 10
            core += 10
            write = "+" + str(mmr) + "  SUPPORT  WIN  with " + hero + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        elif match == "l":
            change = int(input("Enter current mmr:\n"))
            mmr = support - change
            supportChange -= mmr
            support = change
            coreChange -= 10
            core -= 10
            write = "-" + str(mmr) + "  SUPPORT  LOSE  with " + hero + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    else:
        boolean = False
    print(supportChange)
    print(coreChange)

    file.write("--------------------------------\n" + write + "\n")
    curMmr = "CURRENT MMR:   CORE: " + str(core) + " SUPPORT: " + str(support) + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n"
    changeToday = "TODAY CHANGE:   CORE: " + str(coreChange) + " SUPPORT: " + str(supportChange) + " " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n"
    print(write + "\n")

file.write(curMmr + "\n--------------------------------\n")
file.write(changeToday)
print(curMmr)
file.close()
