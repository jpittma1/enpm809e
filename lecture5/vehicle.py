class Vehicle:
    pass
    def __init__(self, color, fuel_type):
        # initialize attributes here
        self.color = color
        self.fuel_type = fuel_type
        
    def drive_forward(self):
    # write body of the method
        pass
    
    def check_blindspot(self):
    # write body of the method
        pass
    
    def __str__(self):
        return f"Color: {self.color}, Fuel_type: {self.fuel_type}"


if __name__ == "__main__":
    blue_car = Vehicle("blue", "gas")
    blue_car.drive_forward()
    red_car = Vehicle("red", "diesel")
    red_car.drive_forward()
    red_car.check_blindspot()
    print(blue_car)
    print(red_car)