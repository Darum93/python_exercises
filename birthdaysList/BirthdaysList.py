import datetime
import random


class BirthdayList:
    def __init__(self):
        self.birthdays = []


    def getBirthdays(self, numberOfChoice):
        startOfYear = datetime.date(2001, 1, 1)

        for i in range(numberOfChoice):
            randomBirthday = datetime.timedelta(random.randint(0, 364))
            self.birthdays.append(startOfYear + randomBirthday)

        return self.birthdays

    def getMatch(self):

        if len(self.birthdays) == len(set(self.birthdays)):
            return None

        for a, birthdayA in enumerate(self.birthdays):
            for b, birthdayB in enumerate(self.birthdays[a + 1 :]):
                if birthdayA == birthdayB:
                    return  birthdayA

    def clearBirhdays(self):
        self.birthdays = []

