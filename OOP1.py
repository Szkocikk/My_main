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
    pass

class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())