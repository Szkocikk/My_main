import random
import sys


class Card(object):

    def __init__(self, color=False, value=False):
        self.color = color
        self.value = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):

        if color != False:
            x = color.capitalize()
            color = x

        if color == 'Pik':
            self.__color = 'Pik'
        elif color == 'Kier':
            self.__color = 'Kier'
        elif color == 'Trefl':
            self.__color = 'Trefl'
        elif color == 'Karo':
            self.__color = 'Karo'
        elif color == False:
            random_list = ['Pik', 'Karo', 'Trefl', 'Kier']
            draw_lots = random.choice(random_list)
            self.__color = draw_lots
        else:
            print('Value Error')
            raise SystemExit

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        if value != False:
            schowek = value.capitalize()
            value = schowek

        if value == 'Jopek':
            self.__value = 'Jopek'
        elif value == 'Dama':
            self.__value = 'Dama'
        elif value == 'Król':
            self.__value = 'Król'
        elif value == 'As':
            self.__value = 'As'
        elif value == False:
            random_value = ['Jopek', 'Dama', 'Król', 'As', 'Twoja stara']
            draw_value = random.choice(random_value)
            self.__value = draw_value
        else:
            print('Value Error')
            raise SystemExit

    def Print_final(self):
        Przetasowanie_1.color
        Przetasowanie_1.value
        return print(f'wylosowana karta: {self.value} {self.color}')


Przetasowanie_1 = Card('Pik', 'Król')

Przetasowanie_1.Print_final()
