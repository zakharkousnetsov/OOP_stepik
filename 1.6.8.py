# https://stepik.org/lesson/701975/step/9?unit=702076

class Cart:

    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        #return self.goods.append(gd.name+': '+str(gd.price))
        #self.goods.append(f'{gd.name}: {gd.price}')
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{item.name}: {item.price}' for item in self.goods]
        #return self.goods

class Table :
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

tv1 = TV('tv1', 555)
tv2 = TV('tv2', 666)
table1 = TV('table1', 222)
nb1 = Cup('lenovo', 777)
nb2 = Cup('hp', 999)
cup1 = Cup('ggg', 12)


cart = Cart()
for item in [tv2, tv2, table1, nb1, nb2, cup1]:
    cart.add(item)

print(cart.get_list())
cart.remove(3)
print(cart.get_list())