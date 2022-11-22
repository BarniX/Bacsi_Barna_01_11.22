from os import system
from functions import *


választás = ''

while választás != '0':
    választás=menu()
    if választás == '1':
        pass
    elif választás == '2':
        pass
    elif választás == '3':
        pass
    elif választás == '4':
        while len(lapjaid) != 0 and len(ellenfellapjai) != 0:
            print("Előző lap: ",elozolap)
            print("Lapjaid: "," ".join(lapjaid))
            #print("Lapjai: "," ".join(ellenfellapjai))
            if tudoklerakni():
                lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                if lap in lapjaid:
                    lapjaid.remove(lap)
                    elozolap = lap
                else:
                    print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
                    while lap in lapjaid:
                        lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                        if lap in lapjaid:
                            lapjaid.remove(lap)
                            elozolap = lap
                        else:
                            print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
            botlap = botlerakas()
            if botlap != None:
                elozolap = botlap
        if len(lapjaid) == 0:
            print("\nGratulálok, te nyertél!!!!!!!!!!!!!!!!")
        else:
            print("\nSajnáljuk, de vesztettél. :(")
    elif választás == '5':
        pass