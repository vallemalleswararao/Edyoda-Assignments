class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its high energy and agility.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its strong and muscular build.")


# Create Dog object and demonstrate functionality
dog = Dog("Max", 5, "Brown")
dog.description()
dog.get_info()

print()

# Create JackRussellTerrier object and demonstrate functionality
jack_russell = JackRussellTerrier("Rocky", 3, "White with brown patches")
jack_russell.description()
jack_russell.get_info()
jack_russell.special_ability()

print()

# Create Bulldog object and demonstrate functionality
bulldog = Bulldog("Spike", 4, "Fawn")
bulldog.description()
bulldog.get_info()
bulldog.special_ability()