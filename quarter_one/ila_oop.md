# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
The sari sari store can apply encapsulation to protect the product information like product name, price and stock. A `ProductName` object can keep the information private and protected, and we can modify the information using functions such as `addStock()`, `removeStock()`, and many more. This way the data is protected from unauthorized modifications.

### 2. Abstraction
Abstraction can be applied in keeping complicated processes from the store owner. Complex processes like checking the stock, logging a purchase, calculating prices, and many more can be completed without having to show the owner how it works internally. This can be done using functions like `sell()`, `checkStock()`, and many more. This makes the system easier to use and clean to look at.

### 3. Inheritance
Inheritance allows a class to acquire the properties of another class. The sari sari store can use a general `Product` class which contains basic information like name and price. Other specific classes like `FoodProduct`, `DrinkProduct`, or `MiscProduct` can inherit these basic properties while adding their own unique property. This helps keep objects organized and easy to locate.

### 4. Polymorphism
Polymorphism can be useful in the system as it allows different types of products (e.g. `ProductName`) to use the same function (e.g. `productInfo()`) but display different outputs. Let's say we have a function called `productInfo()` for the two product classes `FoodProduct` and `DrinkProduct`. One can display the net weight and the other can display its volume. This allows the system to be more flexible to use.

## Reflection
Encapsulation would be most useful in improving the inventory system. It helps protect the important data while making the process of modifying the data easier through the use of different functions.

