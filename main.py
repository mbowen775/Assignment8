# class for Bird
class Bird:
    # __int__ method which sets the name of the bird
    def __init__(self, name):
        self.name = name
        # initialize other variables as None
        self.type = None
        self.sound = None

    # method to set type of the bird
    def setType(self, type):
        # set the type of the bird
        self.type = type

    # method to set sound of the bird
    def setSound(self, sound):
        # set sound of the bird
        self.sound = sound


# Take input for bird 1 name from console
bird_name = input("Enter name of Bird 1: ")
# create instance of bird 1
b1 = Bird(bird_name)

# take input for bird 1 type
bird_type = input("Enter type of Bird 1: ")
# set type using set method
b1.setType(bird_type)

# take input for bird 1 sound
bird_sound = input("Enter sound of Bird 1: ")
# set sound
b1.setSound(bird_sound)

# dir(Object) lists all the methods and attributes
# displaying only methods defined in class
method_list = [m for m in dir(b1) if m.startswith('_') is False]
print("List of attributes and methods: ", method_list)
# print list of attributes and its values of b1
print("Values of attributes: ", vars(b1))


print()


# Take input for bird 2 name from console
bird_name = input("Enter name of Bird 2: ")
# create instance of bird 2
b2 = Bird(bird_name)

# take input for bird 2 type
bird_type = input("Enter type of Bird 2: ")
# set type using set method
b2.setType(bird_type)

# take input for bird 1 sound
bird_sound = input("Enter sound of Bird 2: ")
# set sound
b2.setSound(bird_sound)

# dir(Object) lists all the methods and attributes
# displaying only methods defined in class
method_list = [m for m in dir(b2) if m.startswith('_') is False]
print("List of attributes and methods: ", method_list)
# print list of attributes and its values of b1
print("Values of attributes: ", vars(b2))
