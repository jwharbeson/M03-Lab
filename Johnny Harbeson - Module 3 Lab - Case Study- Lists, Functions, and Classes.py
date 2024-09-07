# Module 3 Lab - Case Study: Lists, Functions, and Classes
# Johnny W. Harbeson V0.0.1

# class Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# subclass Automobile inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display the automobile information
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main app logic to take user input
def main():
    vehicle_type = "car"

    # Ask for user input
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an instance of Automobile with the provided data
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output the data in a formatted manner
    print("\nCar details:")
    car.display_info()

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
