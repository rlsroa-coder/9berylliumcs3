# Class Attributes and Methods

## Previous Design
- [ClassObjectUML.md](Quarter%201/classObjectUML.md)

## Design Revision
Changes from my previous design:
- Narrowed the class from a general "Transportation" concept down to a concrete "Vehicle" class so it could be turned into a working code
- Combined the properties into four concrete, typed attributes namely: name, speed, price, and safetyRating.
- Renamed the methods into drive(distance), applyDiscount(percent), getPrice(), and getSummary().
- Added a mileage attribute so that drive() would have a real, meaningful attribute to update.

## Visibility Desicions

| Attribute | Data Type |  Visibility | Reason                                                                                                                          |
| :---      | :---      |  :---       | :---                                                                                                                            |
| name      | string    | Public      | The vehicle's name is safe for any part of the program to read or display without restraint                                     |
| speed     | float     | Public      | Top speed is descriptive info, not sensitive data, so outside code can read or set it freely                                    |
| price     | float     | Private     | Price should only change through a controlled method (applyDiscount()) so it can never be set to an invalidate or negative value|
| mileage   | float     | Private     | Mileage should only ever increase through drive(), never be set directly, so the object's history of travel stays accurate      |

## Updated UML Class Diagram

+-------------------------------------------+

|                Vehicle                    |

+-------------------------------------------+

| +name    :  string                        | 

| +speed   :  float                         |

| -price   :  float                         | 

| -mileage :  float                         | 

+-------------------------------------------+

| +__init__(name, speed, price, safetRating)|

| +drive(distance : float)                  |

| +applyDiscount(percent : float)           |

| +getPrice()                               |

| +getSummary()                             |

+-------------------------------------------+

| Veh     | icle |
| --:     | :--       |
| +name   | string    |
| +speed  | float     |
| -price  | float     |
| -mileage| float     |

| <!--  -->|
| :--      |
| +__init__(name, speed, price, safetRating) |
| +drive(distance : float) 
| +applyDiscount(percent : float)  |
| +getPrice()  |
| +getSummary()    |                         

## Python Implementation
- [View Python Source](github.com/rlsroa-coder/9berylliumcs3/blob/main/Quarter%201/classObjectUML.md)

## Test Run
- [Test Run]()

## Object Diagram
- [Class Diagram](https://canva.link/6igpuhwhdvdyhuw_)

## Analysis
