# Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
#
# add(self, eng, rus) - для добавления новой связки английского и русского слова
# (если английское слово уже существует, то новое русское слово добавляется как синоним для перевода,
# например, go - идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно,
# например:  add('go', 'идти'), add('go', 'идти');
# remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский
# (метод должен возвращать список из русских слов, соответствующих переводу английского слова,
# даже если в списке всего одно слово).
#
# Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator,
# т.е. связки хранить локально внутри экземпляров классов класса Translator.

class Translator:
    'это класс'
    dct = {}

    def add(self, eng, rus):
        if not eng in Translator.dct.keys():
            Translator.dct[eng] = [rus]
        elif rus not in Translator.dct[eng]:
            Translator.dct[eng].append(rus)

        return Translator.dct

    def remove(self, eng):
        if eng in Translator.dct:
            del Translator.dct[eng]
        return Translator.dct

    def translate(self, eng):
        return ' '.join(Translator.dct[eng])

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(tr.translate('go'))
