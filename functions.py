from os import system
import random

lapjaid = []
ellenfellapjai = []
elozolap = ""
kezdolapok = 8

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Lapok kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása (szabályos játékmenet')
    print('4 - Játék elindítása (végtelen számú lapokkal')
    print('5 - Játék elindítása (csak számos lapokkal')
    return input('Válassz egy menüpontot: ')

def lap_generalas():
    szam = str(random.randint(0,9))
    szin = random.randint(1,4)
    if szin == 1:
        return "P" + szam
    elif szin == 2:
        return "Z" + szam
    elif szin == 3:
        return "S" + szam
    elif szin == 4:
        return "K" + szam

def kez():
    for lap in range(kezdolapok):
        lapjaid.append(lap_generalas())
        ellenfellapjai.append(lap_generalas())

def botlerakas():
    for lap in ellenfellapjai:
        if lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            ellenfellapjai.remove(lap)
            return lap
    else:
        ellenfellapjai.append(lap_generalas())
        print("Az ellenfél lapot húzott")
        return None

def tudoklerakni():
    for lap in lapjaid:
        if elozolap == "":
            return True
        elif lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            return True
    else:
        lapjaid.append(lap_generalas())
        print("Kaptál egy lapot, mert nem tudtál mit lerakni!")
        return False