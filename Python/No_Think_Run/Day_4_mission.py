from abc import ABC, abstractmethod

class Vehicle(ABC):
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("자동차 시동 걸기")

class Bike(Vehicle):
    def start(self):
        print("자전거 폐달 밟기")

class Bus(Vehicle):
    def start(self):
        print("버스 운전 시작")

vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()