from BirthdaysList import BirthdayList

if __name__ == '__main__':

    MONTHS = ('Sty','Lut','Mar','Kwi','Maj','Cze','Lip','Sie','Wrz','Paź','Lis','Gru')

    while True:
        numberOfBirthDays = input("Podaj ile dni urodzeń należy wygenerować (do 100 dni): ")
        if (numberOfBirthDays.isdecimal() and (0 < int(numberOfBirthDays) <= 100)):
            numberOfBirthDays: int = int(numberOfBirthDays)
            break
        else:
            print('Podaj poprawną liczbę urodzeń')

    print('Oto ',numberOfBirthDays,'liczba urodzin')

    birthdaysList = BirthdayList()

    birthdays = birthdaysList.getBirthdays(numberOfBirthDays)

    for i,birthday in enumerate(birthdays):
        if i > 0:
            print(',', end=' ')
        monthName = MONTHS[birthday.month - 1]
        dateText = f'{monthName} {birthday.day}'
        print(dateText, end = ' ')

    print('''
    
    ''')
    print('Oto te urdzoiny które się powtarzały')
    birthdayMatched = birthdaysList.getMatch()
    if birthdayMatched != None:
        monthName = MONTHS[birthdayMatched.month - 1]
        dateText = f'{monthName} {birthdayMatched.day}'
        print('Kilka osób ma urodziny', dateText)
    else:
        print('Nikt nie ma urodzin w tym samym dniu')


    print('Generowanie',numberOfBirthDays,' urodzin 100 000 razy')
    input('Naciśnij Enter jeśli chcesz kontynuować...')
    succFind = 0

    for i in range(100_000):
        if i % 10_000 == 0:
            print('Wykonanano',i,' symulacji')

        birthdaysList.clearBirhdays()
        birthdaysList.getBirthdays(numberOfBirthDays)
        birthdayMatchedA = birthdaysList.getMatch()

        if birthdayMatchedA != None:
            succFind = succFind + 1

    probability = round((succFind / 100_000) * 100,2)
    print('istnieje', probability, '% szans że w losowej grupie urodzin o ilość', numberOfBirthDays, 'znajduje się więcej niż jedne takie same urodziny, tych samych powtórzeń okazało się w ',succFind,' razy')
