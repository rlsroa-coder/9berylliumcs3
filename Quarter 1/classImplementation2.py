class Vehicle:
  """A simple dimple model of a mode of transportation"""
  def __init__(self, name, speed, price, safetyRating):
    self.name  = name
    self.speed = speed
    self.__price        = price
    self.__mileage      = 0.0
    self.__safetyRating = safetyRating

  def drive(self, distance):
    """Drive the vehicle a given distance, updating total mileage"""
    if distance <= 0:
      print(f"{self.name}: distance must be a positive. No mileage added.")
      return
    self.__mileage += distance
    print(f"{self.name}: traveled {distance} km.")

  def applyDiscount(self, percent):
    """Apply a percentage discount to the private price, safely."""
    if not (0 <= percent <=100):
      print(f"{self.name}: invalid discount percent, price unchanged") 
      return
    self.__price = round(self.__price * (1 - percent / 100), 2)
    print(f"{self.name}: {percent}% discount applied.")

  def getPrice(self):
    """Return the current (possibly discounted) price."""
    return self.__price


  def getSummary(self):
   """Return a human - readable summary of this vehicle's state"""
   return (f"{self.name} | speed: {self.speed} km/h "
           f"{self.__price} | mileage: {self.__mileage}"
           f"safety:{self.__safetyRating}")

if __name__ == "__main__":
  object1 = Vehicle("City Bus", speed = 90, price = 75.0, safetyRating = "High")
  object2 = Vehicle("Motor Bike", speed = 130, price = 25.0, safetyRating = "Medium")

  print("---BEFORE---")
  print("Object 1:" ,object1.getSummary())
  print("Object 2:" ,object2.getSummary())

  print("\nPerforming actions on object 1") #I used \n to make the output not looked cramped
  object1.drive(150)
  object1.applyDiscount(10)
  
  print("\n---AFTER---")
  print("Object 1:" ,object1.getSummary())
  print("Object 2:" ,object2.getSummary())

#I copy pasted the previous code into this new python file

class Garage:
  def __init__(self, garageName, capacity):
    self.garageName= garageName
    self.capacity= capacity
    self.__vehicles= []

  def addVehicle(self, vehicle):
    if len(self.__vehicles) < self.capacity:
      self.__vehicles.append(vehicle)
      print(f" + {vehicle.name} added to {self.garageName}")
    else:
      print(" Yo yo the garage is full ")

  def getVehicleCount(self):
    return len(self.__vehicles)

  def getVehicles(self):
    return self.__vehicles
    # This returns the names and the other one returns the no. of vehicles

  def getSummary(self):
    lines = [f"Garage: {self.garageName} ({len(self.__vehicles)}/{self.capacity} vehicles)"]
    for v in self.__vehicles:
      lines.append(f"    -> {v.getSummary()}")
    return "\n".join(lines)


if __name__ == "__main__":
 
    print("--- BEFORE RELATIONSHIP ---")
    garage1 = Garage("Downtown Garage", 5)
    vehicle1 = Vehicle("Toyota Vios", 180.0, 900000.0, "5-Star")
    vehicle2 = Vehicle("Honda Civic", 200.0, 1200000.0, "5-Star")
    vehicle3 = Vehicle("Ford Ranger", 170.0, 1500000.0, "4-Star")
 
    print(garage1.getSummary())
    print(vehicle1.getSummary())
    print(vehicle2.getSummary())
    print(vehicle3.getSummary())
 
    print("\n--- BUILDING RELATIONSHIP ---")
    garage1.addVehicle(vehicle1)
    garage1.addVehicle(vehicle2)
    garage1.addVehicle(vehicle3)
 
    print("\n--- AFTER RELATIONSHIP ---")
    vehicle1.drive(150.0)
    vehicle2.applyDiscount(10)
 
    print(f"Related object(s) for {garage1.garageName}:")
    for v in garage1.getVehicles():
        print(f"   -> {v.getSummary()}")
 
    print(f"\nTotal vehicles in {garage1.garageName}: {garage1.getVehicleCount()}")
 
  
