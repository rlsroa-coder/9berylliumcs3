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
- [Test Run](https://docs.google.com/document/d/1METHRPSMOhQRKkbiLGVgqdsNz3pzPHF-M6MwJ12PhmQ/edit?usp=sharing)

## Object Diagram
- [Class Diagram](https://canva.link/6igpuhwhdvdyhuw_)

## Analysis

### Why did you make your chosen attribute private?
Making price and mileage private guards against bad data inputs. Unchecked access allows external code to set invalid prices or tamper with mileage records. Forcing access through defined methods guarantees that every update meets validation rules.

### Which method changes the state of your object?
State changes rely on drive(distance) and applyDiscount(percent). Drive increases mileage by distance, while applyDiscount updates price. Both methods run safety checks on incoming arguments before saving state.

### How did your two objects demonstrate that instances are independent?
Object 1 and Object 2 confirmed separate instance storage. Updating Object 1 changed its mileage to 150.0 and price to 45.0. Object 2 preserved the base state of 0.0 mileage and 20 price, confirming an isolated scope. 
<!--isolated scope is like a boundary that prevents code inside something from directly accessing it, let alone modify it.--->

### What is the difference between your class diagram and your object diagram?
Class Diagram is the template on where the object bases on. It contains the variables that the object diagram will give definition to. Object Diagram is where the named/defined variables are presented.
