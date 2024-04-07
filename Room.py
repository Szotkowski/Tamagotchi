class Room:
    def __init__(self):
        self.background = None
        self.name = None

class Bathroom(Room):
    def __init__(self):
        super().__init__()
        self.background = 'bathroom.bmp'
        self.name = 'Bathroom'

class Bedroom(Room):
    def __init__(self):
        super().__init__()
        self.background = 'bedroom.bmp'
        self.name = 'Bedroom'

class Garden(Room):
    def __init__(self):
        super().__init__()
        self.background = 'garden.bmp'
        self.name = 'Garden'
        
class DiningRoom(Room):
    def __init__(self):
        super().__init__()
        self.background = 'diningroom.bmp'
        self.name = 'Dining Room'