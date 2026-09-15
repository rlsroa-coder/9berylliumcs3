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

## Association
#### Relationship: Garage manages vehicles
Elaboration: A garage's utmost purpose is to store or in other words manage the vehicle. So a manages "HAS-A" relationship is present. The garage object doesn't just describe vehicles, it actually keeps a working list of the real vehicle objects parked in it. This lets the garage report on, count, and summarize the vehicles it holds any time by going straight to the source objects.

## Multiplicity 
#### Multiplicity: 1 : 1, 1**: 1, etc.
Exposition: One garage can hold zero, one, or many vehicles depending on how many are currently parked there, so the many side has to allow for zero. An empty garage is still a valid garage btw up through its capacity. A vehicle, in this simple design, belongs to one garage at a time, which is why the garage side relationship is fixed to 1.

## UML Class Diagram
- [Object Class Diagram](https://canva.link/54zia8glnbp1l0q)

## Python Implementation
- [Python Implementation](
