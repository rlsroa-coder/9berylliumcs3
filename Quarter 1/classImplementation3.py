class Vehicle:
  def __init__(self, name, speed, price, safetyRating):
    self.name  = name
    self.speed = speed
    self.__price        = price
    self.__mileage      = 0.0
    self.__safetyRating = safetyRating

  def drive(self, distance):
    if distance <= 0:
      print(f"{self.name}: distance must be positive. No mileage added.")
      return
    self.__mileage += distance
    print(f"{self.name}: traveled {distance} km.")

  def applyDiscount(self, percent):
    if not (0 <= percent <= 100):
      print(f"{self.name}: invalid discount percent, price unchanged")
      return
    self.__price = round(self.__price * (1 - percent / 100), 2)
    print(f"{self.name}: {percent}% discount applied.")

  def getPrice(self):
    return self.__price

  def getMileage(self):
    return self.__mileage

  def getSummary(self):
    return (f"{self.name} | speed: {self.speed} km/h | "
            f"price: {self.__price} | mileage: {self.__mileage} | "
            f"safety: {self.__safetyRating}")


class Mechanic:
  def __init__(self, name, specialty):
    self.name = name
    self.specialty = specialty

  def getSummary(self):
    return f"Mechanic: {self.name} ({self.specialty})"

  def performInspection(self, vehicle):
    print(f"{self.name} is inspecting {vehicle.name}...")
    mileage = vehicle.getMileage()
    status = "needs maintenance soon" if mileage > 100 else "looks fine"
    print(f"  -> Result: {vehicle.name} {status} (mileage: {mileage}).")


class Garage:
  def __init__(self, garageName, capacity, headMechanic=None):
    self.garageName = garageName
    self.capacity = capacity
    self.headMechanic = headMechanic
    self.__vehicles = []

  def addVehicle(self, vehicle):
    if len(self.__vehicles) < self.capacity:
      self.__vehicles.append(vehicle)
      print(f" + {vehicle.name} added to {self.garageName}")
    else:
      print(f" {self.garageName} is full, can't add {vehicle.name}")

  def getVehicleCount(self):
    return len(self.__vehicles)

  def getVehicles(self):
    return list(self.__vehicles)

  def getSummary(self):
    lines = [f"Garage: {self.garageName} ({len(self.__vehicles)}/{self.capacity} vehicles)"]
    if self.headMechanic is not None:
      lines.append(f"  Head mechanic: {self.headMechanic.name}")
    for v in self.__vehicles:
      lines.append(f"    -> {v.getSummary()}")
    return "\n".join(lines)


class Battery:
  def __init__(self, capacityKwh):
    self.capacityKwh = capacityKwh
    self.__chargeLevel = 100.0

  def useCharge(self, percent):
    self.__chargeLevel = max(0.0, self.__chargeLevel - percent)

  def recharge(self, percent):
    self.__chargeLevel = min(100.0, self.__chargeLevel + percent)

  def getChargeLevel(self):
    return self.__chargeLevel

  def getSummary(self):
    return f"Battery({self.capacityKwh}kWh) @ {self.__chargeLevel:.1f}% charge"


class ElectricVehicle(Vehicle):
  def __init__(self, name, speed, price, safetyRating, batteryCapacityKwh, rangeKm):
    super().__init__(name, speed, price, safetyRating)
    self.rangeKm = rangeKm
    self.battery = Battery(batteryCapacityKwh)

  def drive(self, distance):
    if distance <= 0:
      print(f"{self.name}: distance must be positive. No mileage added.")
      return
    percentUsed = (distance / self.rangeKm) * 100
    if percentUsed > self.battery.getChargeLevel():
      print(f"{self.name}: not enough charge to travel {distance} km.")
      return
    super().drive(distance)
    self.battery.useCharge(percentUsed)
    print(f"{self.name}: battery now at {self.battery.getChargeLevel():.1f}%.")

  def chargeBattery(self, percent):
    self.battery.recharge(percent)
    print(f"{self.name}: charged. Battery now at {self.battery.getChargeLevel():.1f}%.")

  def getSummary(self):
    baseSummary = super().getSummary()
    return (f"{baseSummary} | range: {self.rangeKm}km | "
            f"{self.battery.getSummary()}")


if __name__ == "__main__":
  print("=" * 70)
  print("TEST 0 - BASIC VEHICLE")
  print("=" * 70)

  bus = Vehicle("City Bus", speed=90, price=75.0, safetyRating="High")
  bike = Vehicle("Motor Bike", speed=130, price=25.0, safetyRating="Medium")

  print("---BEFORE---")
  print("Bus :", bus.getSummary())
  print("Bike:", bike.getSummary())

  print("\nPerforming actions on the bus")
  bus.drive(150)
  bus.applyDiscount(10)

  print("\n---AFTER---")
  print("Bus :", bus.getSummary())
  print("Bike:", bike.getSummary())

  print("\n" + "=" * 70)
  print("TEST 1 - INHERITANCE (ElectricVehicle IS-A Vehicle)")
  print("=" * 70)

  gasCar = Vehicle("Toyota Vios", 180.0, 900000.0, "5-Star")
  ev1 = ElectricVehicle(
      name="Tesla Model 3", speed=225.0, price=2200000.0,
      safetyRating="5-Star", batteryCapacityKwh=57.5, rangeKm=430
  )

  print("Regular Vehicle  :", gasCar.getSummary())
  print("ElectricVehicle  :", ev1.getSummary())
  print(f"\n{ev1.name} inherited name/speed/price/safetyRating from Vehicle,")
  print("and reused Vehicle.__init__() via super().__init__().")

  print("\nDriving the electric vehicle 120km (uses inherited AND overridden logic):")
  ev1.drive(120)
  print("getSummary() also reuses the parent version via super().getSummary().")

  print("\n" + "=" * 70)
  print("TEST 2a - COMPOSITION (ElectricVehicle creates & owns its Battery)")
  print("=" * 70)
  print(f"{ev1.name} contains: {ev1.battery.getSummary()}")
  ev1.chargeBattery(30)
  print("The Battery object was created inside ElectricVehicle.__init__().")
  print("It has no existence anywhere else in this system - if ev1 is deleted,")
  print("its Battery is deleted with it.")

  print("\n" + "=" * 70)
  print("TEST 2b - AGGREGATION (Garage receives an existing Mechanic)")
  print("=" * 70)

  mechanic1 = Mechanic("Jake Santos", "Engine & Electrical Repair")
  print("Mechanic created independently:", mechanic1.getSummary())

  garage1 = Garage("Downtown Garage", 5, headMechanic=mechanic1)
  garage1.addVehicle(gasCar)
  garage1.addVehicle(ev1)

  print("\n" + garage1.getSummary())
  print(f"\nGarage contains Mechanic: {garage1.headMechanic.getSummary()}")
  print("If garage1 were deleted, mechanic1 would still exist independently -")
  print("that's what makes this Aggregation instead of Composition.")

  print("\n" + "=" * 70)
  print("TEST 3 - DEPENDENCY (Mechanic USES-A Vehicle, temporarily)")
  print("=" * 70)
  gasCar.drive(150)
  mechanic1.performInspection(gasCar)
  mechanic1.performInspection(ev1)
  print("\nmechanic1 does not store a permanent reference to either vehicle -")
  print("it only used each one for the duration of performInspection().")

  print("\n" + "=" * 70)
  print("ALL TESTS COMPLETE")
  print("=" * 70)
