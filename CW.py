def keyword_definiotion(**kwargs):
    find = max(kwargs.values())

    print("najstarszy kot to", end = ' ')
    key_list = list(kwargs.keys())
    val_list = list(kwargs.values())
    xd = []
    i = 0
    while i < len(val_list):
        if int(val_list[i]) == find:
            xd.append(key_list[i])
            print(f'{key_list[i]},', end = ' ')
        i=i+1

    x = max(kwargs, key=kwargs.get) #ALTERNATYWA
    print(f'mający {find} lat.')


keyword_definiotion(Peanut = 3, Garfield = 6, Snickers = 6, hujek = 3)

# ---------------------- TO SAMO TYLKO OOP --------------------------------------

class cat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


    def keyword_definiotion(self, val="defualt", **kwargs):
        # self.val =
        kwargs = self.kwargs
        find_age = max(kwargs.values())

        print("najstarszy kot to", end = ' ')
        key_list = list(kwargs.keys())
        val_list = list(kwargs.values())
        xd = []
        i = 0
        while i < len(val_list):
            if int(val_list[i]) == find_age:
                xd.append(key_list[i])
                print(f'{key_list[i]},', end = ' ')
            i=i+1


        x = max(kwargs, key=kwargs.get) #ALTERNATYWA
        print(f'mający {find_age} lat.')


kocie_guwno = cat(Peanut = 3, Garfield = 6, Snickers = 6, hujek = 3)
# print(kocie_guwno.kwargs)
kocie_guwno.keyword_definiotion()