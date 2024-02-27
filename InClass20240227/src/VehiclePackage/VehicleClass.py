
'''
Vehicle Class
This class models a vehicle on a used car  lot
Change Order: we need to add maximum speed to the model
Change Order: need a way to 'read' the maximum speed from the model
Change Order: Some developers need to use the constructor without having to provide a max speed
'''
    # Constructor. It's called when we instantiate an object of Vehicle type
class Vehicle:
    def __init__(self, type, max_speed = None):
        '''
        @Param type:  the kind of vehicle
        @Param max_speed: maximum speed of the vehicle, defaults to None
        '''
        
        self.type = type;
        self.max_speed = max_speed   # save a copy in the current object
    def getSpeed(self):
        return self.max_speed
        # An instance method.  it operates on an instance of the Vehicle class
    def printType(self):
        print(self.type);
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass