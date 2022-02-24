class Animal:
    def __init__(self, animal_name):
        self.name(animal_name)

    @property
    def name(self):
        return self._animal_name

    @name.setter
    def name(self, animal_name):
        self._animal_name = animal_name

x = Animal('lkdwf')

print()