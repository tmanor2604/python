class BandNameGenerator:
    def __init__(self) -> None:
        # Instance variables specific to each instance of a class
        # Instance variables maintain its state and allow each object to keep track of its data
        self.city = ""
        self.name = ""

    def welcome_message(self):
        # self -> Reference to the current instance of class
        print(f'Welcome to the Band Name Generator')

    def get_city_input(self):
        print(f'What\'s name of the city you grew up in?')
        self.city = input()

    def get_pet_name(self):
        print(f'What\'s name of your pet?')
        self.name = input()

    def generate_band_name(self):
        return f"Your Band Name can be {self.city} {self.name}"

    def run(self):
        self.welcome_message()
        self.get_city_input()
        self.get_pet_name()
        print(self.generate_band_name())

generator =  BandNameGenerator()
generator.run()





