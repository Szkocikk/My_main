# class Player_Character:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def run(self):
#         print('run')
#
#     def speak(self):
#         print(f'my name is {self._name1}, and I am {self._age} yo')
#
# player1 = Player_Character('adrei', 100)
# player1.name = '!!!'
# player1.speak = 'Booo'
#
# print(player1.speak)

class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
wizard2 = Wizard('Robi', 80)
wizard1.attack()
wizard2.attack()