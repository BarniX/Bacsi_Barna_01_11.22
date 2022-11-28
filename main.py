from os import system
from functions import *

kezdolapok = 8
lapjaid = []
ellenfellapjai = []
elozolap = ""
valasztas = ''

while valasztas != '0':
    valasztas=menu()
    if valasztas == '1':
        pass
    elif valasztas == '2':
        pass
    elif valasztas == '3':
        pass
    elif valasztas == '4':
        system('cls')
        lapjaid = kez_feketevel(kezdolapok)
        ellenfellapjai = kez_feketevel(kezdolapok)
        while len(lapjaid) != 0 and len(ellenfellapjai) != 0:
            #system('cls')
            print("Előző lap: ",elozolap)
            print("Lapjaid: "," ".join(lapjaid))
            print("Lapjai: "," ".join(ellenfellapjai))
            if tudoklerakni_feketevel(lapjaid, elozolap):
                lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                if lap in lapjaid:
                    lapjaid.remove(lap)
                    elozolap = lap
                elif lap in lapjaid and lap == "F+4":
                    
                    pass
                else:
                    print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
                    while not lap in lapjaid:
                        lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                        if lap in lapjaid:
                            lapjaid.remove(lap)
                            elozolap = lap
                        else:
                            print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
            else:
                print("Kaptál egy lapot, mert nem tudtál mit lerakni!")
            botlap = botlerakas_feketevel(ellenfellapjai, elozolap)
            if botlap != None:
                elozolap = botlap
        if len(lapjaid) == 0:
            print("\nGratulálok, te nyertél!!!!!!!!!!!!!!!!")
        else:
            print("\nSajnáljuk, de vesztettél. :(")
    elif valasztas == '5':
        system('cls')
        lapjaid = kez(kezdolapok)
        ellenfellapjai = kez(kezdolapok)
        while len(lapjaid) != 0 and len(ellenfellapjai) != 0:
            #system('cls')
            print("Előző lap: ",elozolap)
            print("Lapjaid: "," ".join(lapjaid))
            #print("Lapjai: "," ".join(ellenfellapjai))
            if tudoklerakni(lapjaid, elozolap):
                lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                if lap in lapjaid:
                    lapjaid.remove(lap)
                    elozolap = lap
                else:
                    print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
                    while not lap in lapjaid:
                        lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                        if lap in lapjaid:
                            lapjaid.remove(lap)
                            elozolap = lap
                        else:
                            print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
            else:
                print("Kaptál egy lapot, mert nem tudtál mit lerakni!")
            botlap = botlerakas(ellenfellapjai, elozolap)
            if botlap != None:
                elozolap = botlap
        if len(lapjaid) == 0:
            print("\nGratulálok, te nyertél! :D")
        else:
            print("\nSajnáljuk, de vesztettél. :(")