# Python objects are digital representations of things
# that can interact with one another

# Objects are collections of data that we use to
# characterize things

# Examples - A car is a object/ "Thing"
# characteristics of a car: engine, tires, battery, seats,
# color, model, doors

#when we want to make an object, we need to use a class
# class keyword = object maker

# the class name ALWAYS is capitalized / Pascal Case
# this code tells the computer how the object works and what it does

class Car:
    def __init__(self,color, make, model, year, door_num, doorLock, gear):
    # Attributes - characteristics. ways to describe our object with
    # data. this data can be interacted with.
        self.color = "Black"
        self.make = "Ferrari"
        self.model = "Enzo"
        self.year = 2027
        self.door_num = 2
        self.doorLock = Flase
        self.gear = "p"
    
    # Methods - A function (*that exists inside of an object)
    # this function is used EXCLUSIVELY with the object
    # this fucntion serves to give the object specific actions

    def door_lock(self,doorLock):
        # when button is clicked, lock or unlock car doors
        if self.doorLock == True
            print("Lock the doors")
        else:
            print("unlock doors")

    def gearShift():
        # when