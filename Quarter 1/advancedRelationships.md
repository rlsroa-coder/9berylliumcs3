# Advanced Class Relationships

## Previous Activities
- [Class Attributes](classRelationships.md)
- [Class Implementation 2](classImplementation2.py)

## Existing Desicription
Part 3 has two classes which is "Garage" and "Vehicle". Vehicle has name, speed, price, mileage and safetyRating; drive() and applyDiscount(). On the other hand, Garage has a list of the Vehicle references, capacity, addVehicle, and such. 

## Problem
If I want a different kind of subclass of a vehicle I would have to copy-paste all of Vehicle's attributes/methods into a new class. There 
is also no way to show one object having specific ownership to another object or using one in a short time.

## Inheritance Relationship

