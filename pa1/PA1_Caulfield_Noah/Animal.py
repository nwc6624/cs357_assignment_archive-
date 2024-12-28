''' Name:Noah Caulfield
    2/12/2023
    CS 257
'''
class Animal:
    """
    Constructor for the Amimal.
    Every animal has a location and name
    """
    def __init__(self, name, location):
        self.location = location
        self.name = name

    def __str__(self):
        """Method used to print the name o the animal and its location
        """
        return f"{type(self).__name__} at location {self.location}"

    def _move(self, new_location):
        """ Method to set the new location
        """
        self.location = new_location

    def _get_location(self):
        """ Method to return the location
        """
        return self.location

    def get_class_name(self):
        """ Method to return the class name
        """
        return type(self).__name__

    def speak(self):
        """Method that allows the animal to speak
        """
        print("\tIt says: *Silence...*")

