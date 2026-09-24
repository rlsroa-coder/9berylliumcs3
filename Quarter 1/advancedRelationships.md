# Advanced Class Relationships

## Previous Activities
- [Class Attributes](classRelationships.md)
- [Class Implementation 2](classImplementation2.py)

## Existing Desicription
Part 3 has two classes which is "Garage" and "Vehicle". Vehicle has name, speed, price, mileage and safetyRating; drive() and applyDiscount(). On the other hand, Garage has a list of the Vehicle references, capacity, addVehicle, and such. 

## Problem
If I want a different kind of subclass of a vehicle I would have to copy-paste all of Vehicle's attributes/methods into a new class. There is also no way to show one object having specific ownership to another object or using one in a short time.

## Inheritance Relationship
#### Parent: Vehicle
#### Child: Electric Vehicle
#### Explanation:
An electric vehicle IS-A vehicle inheriting the traits of a normal vehicle and adding new traits. Its new traits/attributes are rangeKm() and battery(); drive()/getSummary().

## Inheritance UML
<img width="666" height="375" alt="image" src="https://github.com/user-attachments/assets/1436d747-5238-4a6e-94ca-1c7789b4f565" />

## Composition/Aggregation
#### Relationship: 
Both
#### Explanation:
ElectricVehicle builds its own Battery inside __init__() since the battery has no life outside its vehicle, so if the vehicle is gone, the battery's gone. Garage instead gets handed a mechanic which already existed beforehand. This means that even if the garage were to be expunged, the mechanic will still exist.

## Advanced UML Diagram
<img width="670" height="376" alt="image" src="https://github.com/user-attachments/assets/4a4247d5-40c8-437c-9587-057a24d975e2" />

## Python Implementation
-[Python Implementation 3](classImplementation3.py)


## Test Run
<img width="1365" height="720" alt="image" src="https://github.com/user-attachments/assets/e5e02770-3980-4c85-a351-11b151125659" />
<img width="1365" height="719" alt="image" src="https://github.com/user-attachments/assets/5c9c7bd3-36b4-46d9-9512-20f87903afa8" />
<img width="1365" height="721" alt="image" src="https://github.com/user-attachments/assets/224fd9eb-9301-4d1b-be54-3776650eb6c1" />

## Object Diagram
<img width="664" height="376" alt="image" src="https://github.com/user-attachments/assets/df6a44c3-820d-418c-9294-4b75dda524da" />

## Analysis
1. #### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
   I used inheritance because an ElectricVehicle is still a Vehicle. It has the same name, speed, price and mileage, and it drives and takes discounts the same way. It only adds a battery and a range, so it made sense to build on Vehicle instead of starting over.

2. #### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
   ElectricVehicle calls super().__init__() for its setup, so I didn't rewrite what Vehicle already does. drive() and getSummary() also call the super() version first and then add the EV parts. applyDiscount(), getPrice(), getMileage() and getSafetyRating() are inherited, so I left them alone.

3. #### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
   The Battery is created inside the ElectricVehicle and only exists as long as the vehicle does, so that's composition. The Mechanic is created separately and then given to a Garage. If the garage is deleted, the mechanic is still there, so that's aggregation.

4. #### What is the difference between Association from Part III and the advanced relationship you implemented?
   In Part III, association only meant the classes were connected, like a Garage holding a list of Vehicles. Composition and aggregation add ownership, meaning who creates the object and what happens to it when the other is deleted. Inheritance is different because it's about one class reusing and extending another, not holding a reference to it.
   
5. #### How does your design follow the DRY principle?
   Vehicle's logic is written in one place and ElectricVehicle reuses it instead of copying it. The charging logic stays in Battery and the vehicle list stays in Garage, so nothing is repeated across classes.











