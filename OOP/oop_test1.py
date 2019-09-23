class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # @staticmethod 
    def __private1(param="param"):
    	print('In private static method', param)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# Parrot._Parrot__private1()
blu.__private1()

# access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Blu is a {}".format(blu.species))
# print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))