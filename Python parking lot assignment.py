import random


class ParkingLot:
    
    def __init__(self, total_area, spot_breadth, spot_length):
        #initialize inital values and calculate squarefoot areas respectively
        self.total_area = total_area
        self.spot_area = spot_breadth * spot_length
        
        #create parking lot array with emty values
        self.available_spots = self.total_area // self.spot_area
        
        #create array of empty values for available spots
    def create_parkinglot_list(self):
        parking_lot = []
        for i in range(self.available_spots):
            parking_lot.append(0)
        return parking_lot
        

#assing list of empty values (spots) to a variable

parking_lot = ParkingLot(2000,8,12).create_parkinglot_list()


class Car:
    # Create a car object with a 7digit license plate
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        # magic method to output the license plate on printing the object
        return f"License plate: {self.license_plate}"

    def park(self, parking_lot, spot):
        # function with a recursive call to park the current car in the spot if spot already occupied check new spot
        if parking_lot[spot] == 0:
            parking_lot[spot] = self.license_plate
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot}")
        else:
            print(f"Car with license plate {self.license_plate} cannot be parked in spot {spot}")
            if 0 in parking_lot:  # checking if any empty spots in the parking lot
                for i in range(len(parking_lot)):
                    if parking_lot[i] == 0:
                        spot = i
                        return self.park(parking_lot, spot)  # recursive call of function
            else:
                print("Parking lot is full")

        
def park_cars(cars_list):
    for car in cars_list:
        spot = random.randrange(0, len(parking_lot))
        selected_car = Car(car)
        print()
        print(selected_car)
        selected_car.park(parking_lot, spot)


# list of cars
cars = [1238452, 5736491, 9221984, 5632819, 6327982, 5631412, 5834654, 1332355, 8974565, 8977463, 9874532, 9084321,
        1315921, 8934651, 3984567, 1912348, 6745917]

# calling main method
park_cars(cars)

# print parking lot to see available & occupied spaces
print()
print("parked or available spots in parking lot")
print(parking_lot)
