from BirthdaysList import BirthdayList


def lotOfTry():
    print('ok')
    return None




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

    birthdaysList = BirthdayList(numberOfBirthDays)

    birthdays = birthdaysList.getBirthdays()

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
    monthName = MONTHS[birthdayMatched.month - 1]
    dateText = f'{monthName} {birthdayMatched.day}'
    print(dateText, end=' ')


