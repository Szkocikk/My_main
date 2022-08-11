# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# def get_oldest_cat(*args):
#     return max(args)
#
# peanut = Cat("Peanut", 3)
# garfield = Cat("Garfield", 5)
# snickers = Cat("Snickers", 1)
# print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")

#The same on Dictionery:


def keyword_definiotion(**kwargs):
    print('/////', max(kwargs, key=kwargs.get))

    # x = max(kwargs.items())
    print(kwargs)
    lista = list(kwargs.items())
    print(lista)
    print(lista[0])
    m = max(lista, key=lambda x: x[1])
    print(f'najstarszy kot to {m[0]}  mający {m[1]} lat')



# def get_oldest_cat(**kwargs):
#     return max(values(kwargs))

keyword_definiotion(Peanut = 3, Garfield = 5, Snickers = 5)

# print(f'The oldset cat is{get_oldest_cat(peanut.kwargs, garfield.kwargs, snickers.kwargs)} years old')
