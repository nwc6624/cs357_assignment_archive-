''' Name:Noah Caulfield
    2/12/2023
    CS 357
'''
from Animal import Animal

class Bear(Animal):
    """Constructor for the Bear
    This constructor initializes the features of the parent class
    Assigns "Bear" as the name of the animal
    """
    def __init__(self, location):
        super().__init__("Bear", location)

    def speak(self):
        print("\tIt says: Roarrrrrrr!")

