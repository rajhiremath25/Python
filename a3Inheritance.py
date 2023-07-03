class Vehicle():  # base class

    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am Vehicle")
        print("Mileage of Vehicle : ", self.mileage)
        print("Cost of Vehicle : ", self.cost)


vehicle = Vehicle(25, 2500000)
vehicle.show_details()


class Car(Vehicle):  # child class

    def __init__(self, mileage, cost, tyres, hp):  # over-riding init method of base class
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car(self):
        print("I am Car")
        print("No. of Tyres : ", self.tyres)
        print("Horse Power : ", self.hp)


car = Car(40, 300000, 4, 1500)
car.show_details()  # invoke base/ parent class method
car.show_car()  # invoke child class method
