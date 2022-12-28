import random

class Vehicle:
    def _init_(self):
        self.passengers = 0

class Car(Vehicle):
    def _init_(self, ID):
        super()._init_()
        self.seating_capacity = 5
        self.ID = ID

class Bus(Vehicle):
    def _init_(self):
        super()._init_()
        self.seating_capacity = 25
        self.standing_capacity = 15

car1 = Car(1)
car2 = Car(2)
bus = Bus()

while True:
    user_input = input("Enter A, B, C or any other character to exit: ")
    if user_input == "A":
        if car1.passengers < car1.seating_capacity:
            car1.passengers += 1
            print("Alloted seat in car", car1.ID)
        elif car2.passengers < car2.seating_capacity:
            car2.passengers += 1
            print("Alloted seat in car", car2.ID)
        else:
            print("No seats available in the cars")
    elif user_input == "B":
        if bus.passengers < bus.seating_capacity:
            bus.passengers += 1
            print("Alloted sitting seat in bus")
        elif bus.passengers < bus.seating_capacity + bus.standing_capacity:
            bus.passengers += 1
            print("Alloted standing seat in bus")
        else:
            print("No seats available in the bus")
    elif user_input == "C":
        if bus.passengers > 0:
            if random.uniform(0, 1) < 0.6:
                bus.passengers -= 1
                print("Removed passenger from bus")
                continue
        if car1.passengers > 0:
            if random.uniform(0, 1) < 0.2:
                car1.passengers -= 1
                print("Removed passenger from car", car1.ID)
                continue
        if car2.passengers > 0:
            if random.uniform(0, 1) < 0.2:
                car2.passengers -= 1
                print("Removed passenger from car", car2.ID)
                continue
        print("No passengers to remove")
    else:
        break