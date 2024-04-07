import pygame
import pygame_gui
import Animal
from Home import Home

class TamagotchiGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tamagotchi')
        self.running = True
        self.animal = None
        self.animal_array = []
        self.home = Home()
        self.window_surface = pygame.display.set_mode((700, 400))
        self.background = pygame.transform.scale(pygame.image.load(self.home.current_room.background), (700, 400))
        self.window_surface.blit(self.background, (0, 0))
        self.manager = pygame_gui.UIManager((700, 400), None)
        self.create_ui_elements()

    def create_ui_elements(self):
        self.black_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(290, 5, 150, 50), manager=self.manager)
        self.room_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(380-50, 10, 75, 50), text=self.home.current_room.name, manager=self.manager)
        self.eat_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(180-30, 370, 100, 30), text='Feed', manager=self.manager)
        self.sleep_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(280-30, 370, 100, 30), text='Sleep', manager=self.manager)
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(380-30, 370, 100, 30), text='Play', manager=self.manager)
        self.wash_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(480-30, 370, 100, 30), text='Wash', manager=self.manager)
        self.left_arrow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200), (50, 50)), text='<', manager=self.manager)
        self.right_arrow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 200), (50, 50)), text='>', manager=self.manager)

        self.add_animal_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 50, 150, 30), text='Add Animal', manager=self.manager)
        self.animal_type_dropdown = pygame_gui.elements.UIDropDownMenu(['Dog', 'Cat'], 'Choose animal type', pygame.Rect(200, 50, 150, 30), manager=self.manager)
        self.animal_name_text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(200, 100, 150, 30), manager=self.manager)

    def handle_add_animal(self):
        animal_type = self.animal_type_dropdown.selected_option
        animal_name = self.animal_name_text_entry.get_text()
        if animal_type == 'Dog':
            self.animal = Animal.Dog(animal_name)
        elif animal_type == 'Cat':
            self.animal = Animal.Cat(animal_name)
        
        self.update_ui_with_animal_info()

    def handle_add_animal(self):
        if self.animal is None:
            self.animal = Animal.Dog('Buddy')
            self.update_ui_with_animal_info()

    def update_ui_with_animal_info(self):
        self.black_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(5, 5, 150, 160), manager=self.manager)
        self.name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 10, 100, 30), text='Name: {}'.format(self.animal.name), manager=self.manager)
        self.age = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 40, 100, 30), text='Age: {}'.format(self.animal.age), manager=self.manager)
        self.hunger = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 70, 100, 30), text='Hunger: {}'.format(self.animal.hunger), manager=self.manager)
        self.health = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 100, 100, 30), text='Health: {}'.format(self.animal.health), manager=self.manager)
        self.mood = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 130, 100, 30), text='Mood: {}'.format(self.animal.mood), manager=self.manager)

        self.image = pygame.transform.scale(pygame.image.load(self.animal.image), (200, 200))
        self.window_surface.blit(self.image, (250, 100))
    
    def update_UI(self):
        if self.animal is not None:
            self.hunger.set_text('Hunger: {}'.format(int(self.animal.hunger)))
            self.health.set_text('Health: {}'.format(int(self.animal.health)))
            self.mood.set_text('Mood: {}'.format(int(self.animal.mood)))
            self.age.set_text('Age: {}'.format(int(self.animal.age)))
            self.image = pygame.transform.scale(pygame.image.load(self.animal.image), (200, 200))
            self.window_surface.blit(self.image, (250, 100))
            self.animal.age += 0.001
            self.animal.hunger += 0.0005
            self.animal.mood -= 0.0005

        
        self.room_name.set_text(self.home.current_room.name)
        self.background = pygame.transform.scale(pygame.image.load(self.home.current_room.background), (700, 400))
        self.window_surface.blit(self.background, (0, 0))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.left_arrow_button:
                        self.home.current_room = self.home.rooms[(self.home.rooms.index(self.home.current_room) - 1) % 4]
                    elif event.ui_element == self.right_arrow_button:
                        self.home.current_room = self.home.rooms[(self.home.rooms.index(self.home.current_room) + 1) % 4]
                    if event.ui_element == self.add_animal_button:
                        self.handle_add_animal()
                    if self.animal is not None:
                        if event.ui_element == self.eat_button:
                            self.animal.eat()
                        if event.ui_element == self.sleep_button:
                            self.animal.sleep()
                        if event.ui_element == self.play_button:
                            self.animal.play()
                        if event.ui_element == self.wash_button:
                            self.animal.wash()
                self.manager.process_events(event)
            self.update_UI()
            self.manager.update(pygame.time.Clock().tick(60) / 1200.0)
            if self.animal is not None:
                self.image = pygame.transform.scale(pygame.image.load(self.animal.image), (200, 200))
                self.window_surface.blit(self.image, (250, 100))
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

if __name__ == '__main__':
    game = TamagotchiGame()
    game.run()
