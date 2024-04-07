class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 5
        self.health = 10
        self.mood = 5
        self.image = None

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if value < 0:
            self._hunger = 0
        elif value > 10:
            self._hunger = 10
        else:
            self._hunger = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 10:
            self._health = 10
        else:
            self._health = value

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        if value < 0:
            self._mood = 0
        elif value > 10:
            self._mood = 10
        else:
            self._mood = value

    def eat(self):
        self.hunger -= 1
        self.health = min(self.health + 1, 10)
        self.mood = min(self.mood + 1, 10)

    def sleep(self):
        self.health = min(self.health + 4, 10)
        self.mood = 10
        self.hunger = min(self.hunger + 2, 10)

    def play(self):
        self.mood = min(self.mood + 1, 10)
        self.hunger = min(self.hunger + 1, 10)
    
    def wash(self):
        self.health = max(self.health - 1, 0)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image ='dog.bmp'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'cat.bmp'

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'bird.bmp'

class Troll(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'troll.bmp'