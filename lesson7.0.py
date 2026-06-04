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
    name = "Mercedes"
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