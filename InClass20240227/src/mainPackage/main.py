#main.py
from VehiclePackage.VehicleClass import *

if __name__ == "__main__":
    # instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor
    myCorvette.printType()      # invoke the method on the object
    
    
    # invoke the getter for maximum soeed, stire tge return value in a variable
    # print that to the console
    max_speed = myCorvette.getSpeed()
    print("Max speed:", max_speed)
    
    
    # instantiate another Vehicle object. You can name it
    myMalibu = Vehicle("Car") # myMalibu is an object of type Vehicle
    myMalibu.printType()
    
    
    # I want a list of 3 vehicles: Car, Boat, Space Ship
    # Pick the names and properties
    # Some friendly output to demonstrate what we just did
    myVehicles = [ Vehicle("Chevy Malibu", 170), Vehicle("sailboat", 20), Vehicle("Falcon Heavy" , 4000)]
    # iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())