''' Name:Noah Caulfield
    2/12/2023
    CS 357

'''

import random
from Animal import Animal
from Bear import Bear
from Fish import Fish

#
# random.seed(42)    # Change this number for your different tests.

class Ecosystem:
    ''' Constructor for the Ecosystem
        It initializes the river (a list with a given size)
        It calls the method to initialize the river with animals in random places
        '''   
    def __init__(self, river_size):
        self.river_size = river_size
        self.river = [None] * river_size
        self.initialize_random_ecosystem()

    def initialize_random_ecosystem(self):
        """ Method to randomly initialize the ecosystem
         Randomly picks a number between 1 and 4 to decide the number of Bears
        Randomly places the Bears in the river in empty positions
            Randomly picks a number between 1 and 4 to decide the number of Fish
            Randomly places the Fish in the river in empty positions
            """
        import random

        number_of_bears = random.randint(1, 4)
        number_of_fish = random.randint(1, 4)
        print(f"Initial number of bears: {number_of_bears}")
        print(f"Initial number of fish: {number_of_fish}")
      

        for i in range(number_of_bears):
            location = random.randint(0, self.river_size - 1)
            while self.river[location] is not None:
                location = random.randint(0, self.river_size - 1)
            self.river[location] = Bear(location)
            print(f"Bear assigned to position {location}")

        for i in range(number_of_fish):
            location = random.randint(0, self.river_size - 1)
            while self.river[location] is not None:
                location = random.randint(0, self.river_size - 1)
            self.river[location] = Fish(location)
            print(f"Fish assigned to position {location}")

    def show(self):
        """Method to show each position in the river and the animal each position contains
        """
        for i in range(self.river_size):
            print(f"{self.river[i]}")

    def simulate(self, iterations):
        """Method to simulate the Ecosystem movement
        It similates the ecosystem live depending on the number of iterations passe as argument
        In each iteration, it processes in order each animal
        It randomly picks an action (0=move, 1=stay)
        It moves the animal and do all the similation as defined in the scenario.
            It checks if the next position is empty to move the animal
            If the position is not empty, then it checks what type of animal is in the next position
        It decides what action to perform based on the type of animal in the next position
        """
        for iteration in range(iterations):
            print(f"\n~~~ Iteration {iteration + 1} ~~~~")
            for i in range(self.river_size):
                if self.river[i] is not None:
                    print(f"Processing Animal at location {i}")
                    self.river[i].speak()
                    choice = random.randint(0, 1)
                    if choice == 0:
                        self.river[i]._move(random.randint(0, self.river_size - 1))
                        print( )
