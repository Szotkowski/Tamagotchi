class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.food = 0
        self.health = 10
        self.mood = 0
        self.image = None

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, value):
        if value <= 0:
            self._food = 0
        elif value >= 10:
            self._food = 10
        else:
            self._food = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value <= 0:
            self._health = 0
        elif value >= 10:
            self._health = 10
        else:
            self._health = value

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        if value <= 0:
            self._mood = 0
        elif value >= 10:
            self._mood = 10
        else:
            self._mood = value

    def eat(self):
        self.food += 1
        self.mood += 1

    def sleep(self):
        self.health += 1
        self.food -= 1
        self.mood += 1

    def play(self):
        self.mood += 1
        self.food += 1
    
    def wash(self):
        self.health += 1

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image ='dog.bmp'

    def goOut(self):
        self.mood += 1

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'cat.bmp'
    
    def stratch(self):
        self.mood += 1

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'chicken.bmp'

    def removeEggs(self):
        self.mood += 1

class GuineaPig(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.image = 'guinea_pig.bmp'

    def scretch(self):
        self.mood += 1