from os import system
from functions import *

bothuzott = ''
huztal = ''
kezdolapok = 8
lapjaid = []
ellenfellapjai = []
elozolap = ""
valasztas = ''
valasztas2 = ''
pakli = ['P0','P0','P1','P1','P2','P2','P3','P3','P4','P4','P5','P5','P6','P6','P7','P7','P8','P9','P9','S0','S0','S1','S1','S2','S2','S3','S3','S4','S4','S5','S5','S6','S6','S7','S7','S8','S8','S9','S9','K0','K0','K1','K1','K2','K3','K3','K4','K4','K5','K5','K6','K6','K7','K7','K8','K8','K9','K9','Z0','Z0','Z1','Z1','Z2','Z2','Z3','Z3','Z4','Z4','Z5','Z5','Z6','Z6','Z7','Z7','Z8','Z8','Z9','Z9']
pakli_f = ['P0','P0','P1','P1','P2','P2','P3','P3','P4','P4','P5','P5','P6','P6','P7','P7','P8','P9','P9','S0','S0','S1','S1','S2','S2','S3','S3','S4','S4','S5','S5','S6','S6','S7','S7','S8','S8','S9','S9','K0','K0','K1','K1','K2','K3','K3','K4','K4','K5','K5','K6','K6','K7','K7','K8','K8','K9','K9','Z0','Z0','Z1','Z1','Z2','Z2','Z3','Z3','Z4','Z4','Z5','Z5','Z6','Z6','Z7','Z7','Z8','Z8','Z9','Z9','F+4','F+4','F+4','F+4']

while valasztas != '0':
    valasztas=menu()
    if valasztas == '1':
        system('cls')
        lapkiiras(pakli)
    elif valasztas == '2':
        valasztas2 = ''
        while valasztas2 != '0':
            valasztas2 = utmutato_menu()
            if valasztas2 == '1':
                system('cls')
                print('-----Lapmagyarázat-----\n')
                print('\tP0 ------> Piros nullás\n\tK6 ------> Kék hatos\n\tF+4 ------> "Húzz fel négyet"')
                input('\nVissza az útmutatóba...')
            if valasztas2 == '2':
                system('cls')
                print('------Játékmenet------\n')
                print('1. Az nyer akinek legelőször elfogy minden lapja.\n2. Mindig te kezded a játékmenetet, azaz első körben bármilyen lapot lerakhatsz.\n\tMásodik körtől kezdve csak akkor tudsz lapot lerakni, hogyha megegyezik a lerakandó lap száma vagy színe az előző lapéval.\n3. A főmenü 4. és 3. pontjában lévő játékmódban vannak "F+4" nevezetű lapok, ennek a lapnak a lényege, ha lerakod ezt a lapot akkor az ellenfelednek fel kell húznia 4 lapot.\n Sok szerencsét a játékhoz!')
                input('\nVissza az útmutatóba...')
            if valasztas2 == '3':
                system('cls')
                print('---Információk a kezdésről---\n')
                print('A játékosok alap esetben 8 lappal indítanak, játékmódtól függően lehet akár 4 darab Piros négyesed is.')
                input('\nVissza az útmutatóba...')
    elif valasztas == '3':
        pass
    elif valasztas == '4':
        system('cls')
        lapjaid = kez_feketevel(kezdolapok)
        ellenfellapjai = kez_feketevel(kezdolapok)
        while len(lapjaid) != 0 and len(ellenfellapjai) != 0:
            #system('cls')
            bothuzott = ''
            print("Legfelső lap: ",elozolap)
            print("Lapjaid: "," ".join(lapjaid))
            #print("Lapjai: "," ".join(ellenfellapjai))
            print(f'\tA te lapjaid száma: {len(lapjaid)}db \tEllenfeled lapjainak száma: {len(ellenfellapjai)}db')
            #print('Lapjaid: ',lapjaid)
            #print('Ellenfél lapjai: ',ellenfellapjai)
            if tudoklerakni_feketevel(lapjaid, elozolap) and huztal != 'igen':
                lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                if lap in lapjaid and lap != "F+4":
                    lapjaid.remove(lap)
                    elozolap = lap
                elif lap in lapjaid and lap == "F+4":
                    ellenfellapjai.append(lap_generalas_feketevel())
                    ellenfellapjai.append(lap_generalas_feketevel())
                    ellenfellapjai.append(lap_generalas_feketevel())
                    ellenfellapjai.append(lap_generalas_feketevel())
                    lapjaid.remove(lap)
                    print('Az ellenfelednek húznia kellett négy lapot.')
                    bothuzott = 'igen'
                    elozolap = "F+4"
                else:
                    print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
                    while not lap in lapjaid:
                        lap = str(input("Adj meg egy lapot, amit le akarsz rakni: ").upper())
                        if lap in lapjaid and lap != "F+4":
                            lapjaid.remove(lap)
                            elozolap = lap
                        elif lap in lapjaid and lap == "F+4":
                            ellenfellapjai.append(lap_generalas_feketevel())
                            ellenfellapjai.append(lap_generalas_feketevel())
                            ellenfellapjai.append(lap_generalas_feketevel())
                            ellenfellapjai.append(lap_generalas_feketevel())
                            lapjaid.remove(lap)
                            print('Az ellenfelednek húznia kellett négy lapot.')
                            bothuzott = 'igen'
                            elozolap = "F+4"
                        else:
                            print("Nincs ilyen lapod, vagy nem tudsz ilyet lerakni!")
            else:
                if huztal == 'igen':
                    print('Húztál, ezért ebből a körből kimaradsz.') 
                else:
                    print("Kaptál egy lapot, mert nem tudtál mit lerakni!")
            huztal = ''
            if bothuzott != 'igen':
                botlap = botlerakas_feketevel(ellenfellapjai, elozolap, bothuzott, lapjaid)
                if botlap != None:
                    elozolap = botlap
            else:
                print('A bot húzott, ezért megint te jössz.')
            print('\n')
        if len(lapjaid) == 0:
            print("\nGratulálok, te nyertél!!!!!!!!!!!!!!!!")
        else:
            print("\nSajnáljuk, de vesztettél. :(")
        lapjaid = []
        ellenfellapjai = []
        input('Nyomj meg egy gombot...')
    elif valasztas == '5':
        system('cls')
        lapjaid = kez(kezdolapok)
        ellenfellapjai = kez(kezdolapok)
        while len(lapjaid) != 0 and len(ellenfellapjai) != 0:
            #system('cls')
            print("Legfelső lap: ",elozolap)
            print("Lapjaid: "," ".join(lapjaid))
            #print("Lapjai: "," ".join(ellenfellapjai))
            print(f'\tA te lapjaid száma: {len(lapjaid)}db \tEllenfeled lapjainak száma: {len(ellenfellapjai)}db')
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
                            break
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
        lapjaid = []
        ellenfellapjai = []
        input('Nyomj meg egy gombot...')
        