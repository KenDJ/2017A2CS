import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00

ThisCar = CarRecord()
ThisCar.EngineSize = 2500
ThisCar.VehicleID = 10086
ThisCar.Registration = 5630
ThisCar.DateOfRegistration = 2000/2/23
ThisCar.PurchasePrice = 12.25

CarFile = open('Cars.DAT','wb')
for i in range(100):
    pickle.dump(ThisCar, CarFile)

CarFile.close()

CarFile = open('Cars.DAT','rb')

Car = []

for i in range(5):
    Car.append(pickle.load(CarFile))

CarFile.close()

for i in range(5):
    print(Car[i].VehicleID, Car[i].EngineSize, Car[i].DateOfRegistration, Car[i].PurchasePrice)


