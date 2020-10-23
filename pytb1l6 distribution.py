import time
import os

def opnieuw():
    os.system("cls")
    print("fabriek[]\ndistributie[]\nwinkel[]\nwilt u opnieuw beginnen?   Y/N")

def leeg():
    print("fabriek[]\ndistributie[]\nwinkel[]")

def doe_winkel(fabriek,distributie,winkel):
    winkel.append("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))
    time.sleep(1)
    winkel.remove("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))


def doe_distributie(fabriek,distributie,winkel):
    distributie.append("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))
    time.sleep(1)
    distributie.remove("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))
    doe_winkel(fabriek,distributie,winkel)

def doe_fabriek():
    fabriek = []
    distributie = []
    winkel = []
    fabriek.append("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))
    time.sleep(1)
    fabriek.remove("motor")
    os.system("cls")
    print("fabriek" + str(fabriek) + "\ndistributie" + str(distributie) + "\nwinkel" + str(winkel))
    doe_distributie(fabriek,distributie,winkel)

def alles():
    doe_fabriek()
    os.system("cls")
    print("fabriek[]\ndistributie[]\nwinkel[]\nwilt u opnieuw beginnen?   Y/N")


os.system("cls")
leeg()
print("wilt u beginnen?    Y/N")

ans = input()
if ans.lower() == "y":
    alles() 
else:
    exit()

opnieuw()
while True:
    ans1 = input()
    if ans1.lower() == "y":
        alles()
        continue
    else:
        os.system("cls")
        break