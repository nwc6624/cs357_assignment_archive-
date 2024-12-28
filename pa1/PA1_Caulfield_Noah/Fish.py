''' Name:Noah Caulfield
    2/12/2023
    CS 357
'''

from Animal import Animal


class Fish(Animal):
    """Constructor for the Fish
    This constructor initializes the features of the parent class
    Assigns "Fish" as the name of the animal
    """
    def __init__(self, location):
        super().__init__("Fish", location)

