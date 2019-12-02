class Octopus:
    count_animals = 0

    def __init__(self,age,name="Octavio"):
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name

if __name__ == '__main__':
     #2.2.2
     # o1 = Octopus(12,"o1)
     # o2 = Octopus(55,"o2")
     #
     # o1.birthday()
     #
     # print("o1 age",o1.get_age(),"o2 age",o2.get_age())

    #2.3.3
     o1 = Octopus(12)
     o2 = Octopus(55,"o2")
     print("o1 name", o1.get_name(), "o2 name", o2.get_name())

     o2.set_name("mmm")
     print("o1 name", o1.get_name(), "o2 name", o2.get_name())
     print("count_animals",o1.count_animals,o2.count_animals)