class PlayerCharacter:
    membership = True

    def __init__(self, name='anonmous', age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = age
        else:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('kuta')
player2 = PlayerCharacter('uo')
player2.attack = 50

print(player1.name)
print(player2)
# print(player1.shout())
