import Room

class Home:
    def __init__(self):
        self.rooms = [Room.Bathroom(), Room.Bedroom(), Room.Garden(), Room.DiningRoom()]
        self.current_room = self.rooms[3]