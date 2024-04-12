import pickle
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
        self.current_animal_index = 0
        self.home = Home()
        self.window_surface = pygame.display.set_mode((700, 400))
        self.background = pygame.transform.scale(pygame.image.load(self.home.current_room.background), (700, 400))
        self.manager = pygame_gui.UIManager((700, 400), None)
        self.create_ui_elements()
        self.custom_function_dog = None
        self.custom_function_cat = None
        self.custom_function_chicken = None
        self.custom_function_guinea_pig = None
        try:
            self.load_animal_data('animals.pkl')
            if len(self.animal_array) > 0:
                self.animal = self.animal_array[self.current_animal_index]
                self.update_ui_with_animal_info()
        except FileNotFoundError:
            pass

    def create_ui_elements(self):
        self.black_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(375-80, 5, 110, 60), manager=self.manager)
        self.room_name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(380-80, 10, 100, 50), text=self.home.current_room.name, manager=self.manager)
        self.eat_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(180-30, 370, 100, 30), text='Feed', manager=self.manager)
        self.sleep_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(280-30, 370, 100, 30), text='Sleep', manager=self.manager)
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(380-30, 370, 100, 30), text='Play', manager=self.manager)
        self.wash_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(480-30, 370, 100, 30), text='Wash', manager=self.manager)
        self.left_arrow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200), (50, 50)), text='<', manager=self.manager)
        self.right_arrow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 200), (50, 50)), text='>', manager=self.manager)
        self.switch_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(580-30, 300, 150, 50), text='Switch animal', manager=self.manager)

        self.animal_name_text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(550, 10, 150, 30), manager=self.manager)
        self.animal_name_text_entry.set_text("Enter name")
        self.animal_type_dropdown = pygame_gui.elements.UIDropDownMenu(['Choose animal type', 'Dog', 'Cat', 'Chicken', 'Guinea pig'], 'Choose animal type', pygame.Rect(550, 60, 150, 30), manager=self.manager)
        self.add_animal_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(550, 110, 150, 30), text='Add Animal', manager=self.manager)

    def handle_add_animal(self):
        try:
            animal_type = self.animal_type_dropdown.selected_option
            animal_name = self.animal_name_text_entry.get_text().strip()
            if animal_type and animal_type != 'Choose animal type' and animal_name:
                if animal_type == 'Dog':
                    self.animal = Animal.Dog(animal_name)
                elif animal_type == 'Cat':
                    self.animal = Animal.Cat(animal_name)
                elif animal_type == 'Chicken':
                    self.animal = Animal.Chicken(animal_name)
                elif animal_type == 'Guinea pig':
                    self.animal = Animal.GuineaPig(animal_name)
                else:
                    self.animal = Animal.Dog(animal_name)
                self.animal_array.append(self.animal)
                self.current_animal_index = len(self.animal_array) - 1
                self.update_ui_with_animal_info()
            else:
                self.animal_name_text_entry.rect_colour = (255, 0, 0)
                print("Please select a valid animal type and provide a name.")
        except Exception as e:
            print("Error:", e)

    def update_ui_with_animal_info(self):
        if self.animal:
            self.black_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(5, 5, 200, 160), manager=self.manager)
            self.name = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 10, 190, 30), text='Name: {}'.format(self.animal.name), manager=self.manager)
            self.age = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 40, 100, 30), text='Age: {}'.format(int(self.animal.age)), manager=self.manager)
            self.food = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 70, 100, 30), text='food: {}'.format(int(self.animal.food)), manager=self.manager)
            self.health = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 100, 100, 30), text='Health: {}'.format(int(self.animal.health)), manager=self.manager)
            self.mood = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 130, 100, 30), text='Mood: {}'.format(int(self.animal.mood)), manager=self.manager)
            if self.custom_function_dog:
                self.custom_function_dog.kill()
            if self.custom_function_cat:
                self.custom_function_cat.kill()
            if self.custom_function_chicken:
                self.custom_function_chicken.kill()
            if self.custom_function_guinea_pig:
                self.custom_function_guinea_pig.kill()
            if isinstance(self.animal, Animal.Dog):
                self.custom_function_dog = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(320-40, 330, 140, 40), text='Go out', manager=self.manager)
            elif isinstance(self.animal, Animal.Cat):
                self.custom_function_cat = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(320-40, 330, 140, 40), text='Scratch', manager=self.manager)
            elif isinstance(self.animal, Animal.Chicken):
                self.custom_function_chicken = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(320-40, 330, 140, 40), text='Remove eggs', manager=self.manager)
            elif isinstance(self.animal, Animal.GuineaPig):
                self.custom_function_guinea_pig = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(320-40, 330, 140, 40), text='Scratch', manager=self.manager)

            self.image = pygame.transform.scale(pygame.image.load(self.animal.image), (200, 200))
            self.window_surface.blit(self.image, (250, 100))
            self.manager.draw_ui(self.window_surface)

    def update_UI(self):
        self.manager.update(pygame.time.Clock().tick(60) / 1200.0)
        self.room_name.set_text(self.home.current_room.name)
        self.background = pygame.transform.scale(pygame.image.load(self.home.current_room.background), (700, 400))
        self.window_surface.blit(self.background, (0, 0))
        if self.animal:
            self.image = pygame.transform.scale(pygame.image.load(self.animal.image), (200, 200))
            self.window_surface.blit(self.image, (250, 100))
            self.food.set_text('Food: {}'.format(int(self.animal.food)))
            self.health.set_text('Health: {}'.format(int(self.animal.health)))
            self.mood.set_text('Mood: {}'.format(int(self.animal.mood)))
            self.age.set_text('Age: {}'.format(int(self.animal.age)))
            self.animal.age += 0.001
            self.animal.food -= 0.0005
            self.animal.mood -= 0.0005
            if self.animal.food < 1 or self.animal.mood < 1:
                self.animal.health -= 0.001
            if self.animal.health < 1:
                self.killAnimal(self.animal)
        else:
            try:
                self.image = None
                self.name.kill()
                self.age.kill()
                self.food.kill()
                self.health.kill()
                self.mood.kill()
            except:
                pass
        self.manager.draw_ui(self.window_surface)
        pygame.display.update()

    def killAnimal(self, animal):
        self.animal_array.remove(animal)
        self.update_ui_with_animal_info()
        self.animal = None
        self.switch_animal()

    def switch_animal(self):
        try:
            self.current_animal_index = (self.current_animal_index + 1) % len(self.animal_array)
            self.animal = self.animal_array[self.current_animal_index]
            self.update_ui_with_animal_info()
        except:
            pass

    def save_animal_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.animal_array, file)

    def load_animal_data(self, filename):
        with open(filename, 'rb') as file:
            self.animal_array = pickle.load(file)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.save_animal_data('animals.pkl')
                    pygame.quit()
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.left_arrow_button:
                        self.home.current_room = self.home.rooms[(self.home.rooms.index(self.home.current_room) - 1) % 4]
                    elif event.ui_element == self.right_arrow_button:
                        self.home.current_room = self.home.rooms[(self.home.rooms.index(self.home.current_room) + 1) % 4]
                    if event.ui_element == self.add_animal_button:
                        self.handle_add_animal()
                    if self.animal:
                        if event.ui_element == self.eat_button:
                            self.animal.eat()
                        if event.ui_element == self.sleep_button:
                            self.animal.sleep()
                        if event.ui_element == self.play_button:
                            self.animal.play()
                        if event.ui_element == self.wash_button:
                            self.animal.wash()
                        if event.ui_element == self.switch_button:
                            self.switch_animal()
                        if event.ui_element == self.custom_function_dog and isinstance(self.animal, Animal.Dog):
                            self.animal.goOut()
                        if event.ui_element == self.custom_function_cat and isinstance(self.animal, Animal.Cat):
                            self.animal.stratch()
                        if event.ui_element == self.custom_function_chicken and isinstance(self.animal, Animal.Chicken):
                            self.animal.removeEggs()
                        if event.ui_element == self.custom_function_guinea_pig and isinstance(self.animal, Animal.GuineaPig):
                            self.animal.scretch()
                self.manager.process_events(event)
            self.update_UI()

if __name__ == '__main__':
    try:
        game = TamagotchiGame()
        game.run()
    except:
        pass