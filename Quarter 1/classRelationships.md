# Class Attributes : Association and Multipiclity

## Previous Work:
- [Part 1: Classes and Objects](classObjectUML.md)
- [Part 2: Attributes and Methods](classAttributesMethods.md)

## Existing Class
#### Class: ""Vehicle""
Description: Represents a single vehicle with a name, top speed, price, mileage, and safety rating. It exposes controlled behavior through drive() -- which increases mileage. And also applyDiscount() which reduces price. This keeps the price and mileage private so they can only change through permitted methods.

## New Related Class
#### Class: ""Garage""
Description: Represents a garage that stores and manages vehicle objects. It doesn't duplicate any vehicle's data but it keeps actual references to the vehicle object it manages.

## Associtaion
#### Relationship: Garage manages vehicles
Elaboration: A garage's utmost purpose is to store or in other words manage the vehicle. So a manages "HAS-A" relationship is present. The garage 
