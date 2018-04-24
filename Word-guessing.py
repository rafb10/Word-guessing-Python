import random

LICZBA_GIER = 5
def los(nazwa_pliku):
    plik = open(nazwa_pliku)
    wiersze = 0
    for lines in plik:
        wiersze+=1
    nr_kategorii = random.randint(1,wiersze)
    plik = open(nazwa_pliku)
    i = 0
    while i < nr_kategorii:
        line = plik.readline()    #string
        i+=1
    line = line.split(' ')   #lista
    line[-1] = line[-1].rstrip()
    nr_wyrazu = random.randint(1,len(line)-1)   
    plik.close
    return (line[0], line[nr_wyrazu])



printer = lambda wyraz: print('      ',wyraz)



def zgadywanie_wyrazu():
    krotka = los('Kategorie_slowa.txt')
    punkty = 11
    a = 2
    while a != '9':
        print("Aby wylosować kategorię i wyraz do odgadnięcia wpisz '9'",'\n','\n')
        a = input()
    wyraz = krotka[1]
    odgadniete = ['-']
    list_wyraz = list(wyraz)
    print("Wylosowałeś kategorię ", krotka[0],'\n')
    litera = 'A'
    while(litera.isalpha()):
        punkty -=1
        wyraz = krotka[1]
        for lit in list_wyraz:
            if not(lit in odgadniete):
                wyraz = wyraz.replace(lit,'-')
        printer(wyraz)
        if punkty < 2:
            print("///////Wyczerpałeś limit podpowidzi///////",'\n')
            print("Spróbuj zgadnąć odpowiedź aby zdobyć 1 punkt")
            break
        print("Odgadnij literę (wpisuj tylko DUŻE LITERY) lub naciśnij 2 aby odgadnąć wyraz", '\n')
        litera = input()
        odgadniete.append(litera)
    print("Podaj odpowiedź (Użyj tylko DUŻYCH LITER)")
    odp = input()
    if odp == krotka[1]:
        print("PRAWIDŁOWA ODPOWIEDŹ!!!",'\n',"Uzyskales ",punkty,"punkty/ów za ten wyraz")
    else:
        print("ZŁA ODPOWIEDŹ ","PRAWIDŁOWA ODPOWIEDŹ TO ",krotka[1],'\n')
        print("Uzyskales 0 punktów za ten wyraz")
        punkty = 0
    return punkty



def gra(liczba_gier):
    suma_punktow = 0
    i = 0
    while i < liczba_gier:
        suma_punktow += zgadywanie_wyrazu()
        print('\n','\n')
        i +=1
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("KONIEC GRY      UZYSKAŁEŚ ",suma_punktow,"PUNKTY/ÓW W TEJ GRZE")
    A = input()

gra(LICZBA_GIER)

          
        

    
