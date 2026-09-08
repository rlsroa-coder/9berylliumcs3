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

  def get_price(self):
    """Return the current (possibly discounted) price."""
    return self.__price


  def get_summary(self):
   """Return a human - readable summary of this vehicle's state"""
   return (f"{self.name} | speed: {self.speed} km/h "
           f"{self.__price} | mileage: {self.__mileage}"
           f"safety:{self.__safetyRating}")

if __name__ == "__main__":
  object1 = Vehicle("City Bus", speed = 90, price = 75.0, safetyRating = "High")
  object2 = Vehicle("Motor Bike", speed = 130, price = 25.0, safetyRating = "Medium")

  print("---BEFORE---")
  print("Object 1:" ,object1.get_summary())
  print("Object 2:" ,object2.get_summary())

  print("\nPerforming actions on object 1") #I used \n to make the output not looked cramped
  object1.drive(150)
  object1.applyDiscount(10)
  
  print("\n---AFTER---")
  print("Object 1:" ,object1.get_summary())
  print("Object 2:" ,object2.get_summary())





        
