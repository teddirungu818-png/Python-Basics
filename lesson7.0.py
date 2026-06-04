"""
OBJJECT ORIENTED PROGRAMMING (OOP):
- OOP is a programming paradigm(enables reusability through 'blueprints')
Concepts of OOP:
    -Encapsulation: bundling data and methods that operate on that data within one unit (class)
    -Inheritance: mechanism where a new class inherits properties and behaviors from an existing class
    -Polymorphism: ability of different classes to be treated as instances of the same class through a common interface
"""
# creating a blueprint for a vehicle
class Vehicle:
    # class attributes
    name = "Mercedes AMG GLE63"
    yom = 2023
    color = "dark green"
    engine = "v8"
    # methods(behaviours) = funtion inside a class is called a method
    def raceMode(self):
        print("Step on it")

    def cruiseMode(self):
        print("Swiish")

    def offroadMode(self):
        print("Offroad mode activated")

    def comfortMode(self):
        print("Relax and enjoy the ride")


vehicle_one = Vehicle()# initializing the class to create an object(instance) of the class
vehicle_two = Vehicle()# initializing the class to create an object(instance) of the class

print(vehicle_one.name)
print(vehicle_one.color)

vehicle_one.cruiseMode()
vehicle_two.comfortMode()

class Animal:
    def __init__(self, name, species, yob): # constructor method that initializes the attributes of the class
        self.name = name
        self.species = species
        self.__yob = yob #encapculation => making the attribute private by adding __ before the attribute name
        

  