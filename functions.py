from os import system
import random

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Lapok kiírása')
    print('2 - Útmutató')
    print('3 - Játék elindítása (szabályos játékmenet)')
    print('4 - Játék elindítása (végtelen pakli)')
    print('5 - Játék elindítása (fekete lapok nélkül)')
    return input('Válassz egy menüpontot: ')

def utmutato_menu():
    system('cls')
    print('0 - Kilépés a főmenübe')
    print('1 - Lapmagyarázat')
    print('2 - Játékmenet szabályai')
    print('3 - Kezdés információk')
    return input('Válassz ki egy menürészt vagy lépj vissza a főmenübe (0): ')

def lapkiiras(pakli):
    print('Lapok a pakliban: ',' '.join(pakli))
    input('Továbblépés billentyűlenyomással...')



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

def kez(kezdolapok):
    lapok = []
    for lap in range(kezdolapok):
        lapok.append(lap_generalas())
    return lapok

def botlerakas(ellenfellapjai, elozolap):
    for lap in ellenfellapjai:
        if lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            ellenfellapjai.remove(lap)
            return lap
    else:
        ellenfellapjai.append(lap_generalas())
        print("Az ellenfél lapot húzott")
        return None

def tudoklerakni(lapjaid, elozolap):
    for lap in lapjaid:
        if elozolap == "":
            return True
        elif lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            return True
    else:
        lapjaid.append(lap_generalas())
        return False



def lap_generalas_feketevel():
    szam = str(random.randint(0,9))
    szin = random.randint(1,13)
    if szin == 1 or szin == 2 or szin == 3:
        return "P" + szam
    elif szin == 4 or szin == 5 or szin == 6:
        return "Z" + szam
    elif szin == 7 or szin == 8 or szin == 9:
        return "S" + szam
    elif szin == 10 or szin == 11 or szin == 12:
        return "K" + szam
    elif szin == 13:
        return "F+4"

def kez_feketevel(kezdolapok):
    lapok = []
    for lap in range(kezdolapok):
        lapok.append(lap_generalas_feketevel())
    return lapok

def botlerakas_feketevel(ellenfellapjai, elozolap, bothuzott, lapjaid):
    global huztal
    for lap in ellenfellapjai:
        if bothuzott != 'igen' and lap != "F+4" and lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            ellenfellapjai.remove(lap)
            return lap
        elif bothuzott != 'igen' and lap == 'F+4':
            lapjaid.append(lap_generalas_feketevel())
            lapjaid.append(lap_generalas_feketevel())
            lapjaid.append(lap_generalas_feketevel())
            lapjaid.append(lap_generalas_feketevel())
            ellenfellapjai.remove(lap)
            huztal = 'igen'
            print('Húznod kellett négy lapot.')
            return lap
    else:
        ellenfellapjai.append(lap_generalas_feketevel())
        print("Az ellenfél lapot húzott")
        return None

def tudoklerakni_feketevel(lapjaid, elozolap):
    for lap in lapjaid:
        if elozolap == "":
            return True
        elif elozolap == "F+4" or lap[0] == elozolap[0] or lap[1] == elozolap[1]:
            return True
    else:
        lapjaid.append(lap_generalas_feketevel())
        return False




