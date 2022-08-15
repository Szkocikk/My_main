import datetime
from datetime import datetime, timedelta
import random
import sys


class Person:
    def __init__(self, first_name, last_name, born_date, gender, pesel='???'):
        self.first_name = first_name
        self.last_name = last_name
        self.born_date = born_date
        self.gender = gender
        self.pesel = pesel

    def pesel_generator(self, pesel=0, gender=0, *born_date):
        born_date = self.born_date
        gender = self.gender
        pesel = self.pesel
        pesel = born_date[2:4] + born_date[5:7] + born_date[8:]
        adding_number = random.randrange(100, 999, 1)
        pesel = str(pesel) + str(adding_number)
        if gender == 'M':
            adding_number = random.randrange(1, 9, 2)
            pesel = str(pesel) + str(adding_number)
        else:
            adding_number = random.randrange(0, 8, 2)
            pesel = str(pesel) + str(adding_number)
        adding_number = random.randrange(0, 9, 1)
        pesel = str(pesel) + str(adding_number)
        return print(f'Twój numer pesel to: {pesel}')

    def Check_date(self, *born_date):
        born_date = self.born_date
        if born_date[4] and born_date[7] != '-':
            print('błędne data urodzenia')
        elif born_date[0:4].isnumeric() != True:
            print('błędne data urodzenia')
        elif born_date[6:7].isnumeric() != True:
            print('błędne data urodzenia')
        elif born_date[9:].isnumeric()!= True:
            print('błędne data urodzenia')
        else:
            return
        sys.exit()

    def Years_old_person(self, *born_date):
        born_date = self.born_date
        current_date = datetime.now()
        date_time_obj = datetime.strptime(born_date, '%Y-%m-%d')
        Diff_dates = current_date - date_time_obj
        Diff_dates = str(Diff_dates)
        Max_index_date = 0
        for i in Diff_dates:
            if i == ' ':
                break
            Max_index_date = Max_index_date + 1
        Diff_dates = Diff_dates[0:Max_index_date]
        Diff_dates = int((float(Diff_dates))/365.2425)
        return print(f'Wiek: {Diff_dates} lat/lata')

    def all_in_one(self):
        Polaczek_1.Check_date()
        Polaczek_1.pesel_generator()
        Polaczek_1.Years_old_person()

Polaczek_1 = Person('Adam', 'Mik', '1998-01-10', 'M')
Polaczek_1.all_in_one()

