import random

NUMBER_OF_GAMES = 5
def drawing(file_name):
    file = open(file_name)
    rows = 0
    for lines in file:
        rows+=1
    category_number = random.randint(1,rows)
    file = open(file_name)
    i = 0
    while i < category_number:
        line = file.readline()    #string
        i+=1
    line = line.split(' ')   #lista
    line[-1] = line[-1].rstrip()
    word_number = random.randint(1,len(line)-1)   
    file.close
    return (line[0], line[word_number])



printer = lambda word: print('      ',word)



def wordGuessing():
    tupl = drawing('Kategorie_slowa.txt')
    points = 11
    a = 2
    while a != '9':
        print("Aby wylosować kategorię i wyraz do odgadnięcia wpisz '9'",'\n','\n')
        a = input()
    word = tupl[1]
    guessed = ['-']
    list_word = list(word)
    print("Wylosowałeś kategorię ", tupl[0],'\n')
    letter = 'A'
    while(letter.isalpha()):
        points -=1
        word = tupl[1]
        for let in list_word:
            if not(let in guessed):
                word = word.replace(let,'-')
        printer(word)
        if points < 2:
            print("///////Wyczerpałeś limit podpowidzi///////",'\n')
            print("Spróbuj zgadnąć odpowiedź aby zdobyć 1 punkt")
            break
        print("Odgadnij literę (wpisuj tylko DUŻE LITERY) lub naciśnij 2 aby odgadnąć wyraz", '\n')
        letter = input()
        guessed.append(letter)
    print("Podaj odpowiedź (Użyj tylko DUŻYCH LITER)")
    answer = input()
    if answer == tupl[1]:
        print("PRAWIDŁOWA ODPOWIEDŹ!!!",'\n',"Uzyskales ",points,"punkty/ów za ten wyraz")
    else:
        print("ZŁA ODPOWIEDŹ ","PRAWIDŁOWA ODPOWIEDŹ TO ",tupl[1],'\n')
        print("Uzyskales 0 punktów za ten wyraz")
        points = 0
    return points



def game(number_of_games):
    sum_of_points = 0
    i = 0
    while i < number_of_games:
        sum_of_points += wordGuessing()
        print('\n','\n')
        i +=1
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("KONIEC GRY      UZYSKAŁEŚ ",sum_of_points,"PUNKTY/ÓW W TEJ GRZE")
    A = input()

game(NUMBER_OF_GAMES)

          
        
        

    
