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
#### Multiplicity: 1:0..*
Exposition: One garage can hold zero, one, or many vehicles depending on how many are currently parked there, so the many side has to allow for zero. An empty garage is still a valid garage btw up through its capacity. A vehicle, in this simple design, belongs to one garage at a time, which is why the garage side relationship is fixed to 1.

## UML Class Diagram
<img width="662" height="373" alt="image" src="https://github.com/user-attachments/assets/5dd1cd81-e5ef-4d7b-89c7-48fd39cfd563" />


## Python Implementation
- [Python Implementation 2](classImplementation2.py)

## Test Run
<img width="683" height="357" alt="image" src="https://github.com/user-attachments/assets/f868b723-ac00-473d-8f9a-257753353388" />
<img width="685" height="244" alt="image" src="https://github.com/user-attachments/assets/1c2e386a-bb79-4493-9c8c-345a559b7aa2" />
<img width="685" height="226" alt="image" src="https://github.com/user-attachments/assets/ed554057-3f87-4b1e-9f13-43db77c5cd66" />


## Object Class Diagram
<img width="663" height="376" alt="image" src="https://github.com/user-attachments/assets/e4a01458-ee3e-41dc-be1d-853710daa820" />


## Analysis
#### What is the association between your two classes?
The garage manages the vehicle objects. A garage keeps a private list called vehicles, and every added vehicle by addVehicle() adds to the list. In the test run, garage manages vehicle1,vehicle2,and vehicle3.

#### What multiplicity did you choose and why?
I chose 1:0..* which means one garage can manage many vehicles. This fits well since a garage can hold any amount of vehicles less than or equal to their capacity. 1:1 isn't the best option since a garage can hold many more.

#### How did you implement the relationship in python?
The garage class stores the relationship in a private attribute, self.__vehicles, initialized as an empty list. The addVehicle(vehicle) method appends the actual Vehicle object passed into it to that list, and getVehicles() returns the list so other code can loop through the real, related objects.

#### Why did you store an object reference instead of copying its data?
Storing the object reference means the garage is always looking at the vehicle's current, live state instead of a frozen snapshot. In the test run, vehicle1.drive(150.0) was called directly on the vehicle object after it was added to the garage, and when the garage printed its summary afterward, it correctly showed the updated mileage of 150.0 km proving garage1.__vehicles holds the actual vehicle1 object, not a copy of its earlier data.

#### If your relationship uses many, why is a list appropriate?
A list is appropriate because the number of vehicles a garage holds can grow or shrink and isn't fixed in advance. A list can hold as many Vehicle object references as needed, in the order they were added, and supports the loop in getSummary() that reads each vehicle's live data. The list literally contains Vehicle objects (vehicle1, vehicle2, vehicle3), not strings or numbers copied from them.
