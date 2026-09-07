# SG4 - Understanding Classes and Objects
## Lost Item
## The Lost Item class represents a lost item that was found within the school campus. It stores different important information about the lost item and helps the school track whether it has been claimed or not.
## Properties
| Property | Data Type |            Description            |
|----------|-----------|-----------------------------------|
|itemName  |string     |The item's name.                   |
|placeFound|string     |Where it was found.                |
|ownerName |string     |Name of its owner. (if possible)   |
|claimed   |boolean    |Whether the item has been claimed. |
## Methods
|          Method          |               Description           |
|--------------------------|-------------------------------------|
|claimItem(owner: string)  |Records the person claiming the item.|
|addPlace(place: string)   |Updates where the item was found.    |
|markAsClaimed()           |Changes the item status to claimed.  |
|displayInfo()             |Displays the item's properties.      |
## Class Diagram
<img width="1920" height="1080" alt="oopAct" src="https://github.com/user-attachments/assets/4a93622e-d3ed-40ad-967a-19424a42a647" />
## Design Explanation
### Why did you choose this class?
### - I chose the Lost Item class because students, like me, often lose their personal belongings at school. A simple system with this class could help schools with the management of lost items and make it easier to return them to their owners in an orderly manner.
### Which property is the most important? Why?
### - The claimed property is the most important because it tells the system whether a lost item has already been returned to its rightful owner. This prevents an item from being accidentally given to another person.
### Which method is the most useful? Why?
### - The claimItem(owner: string) method is the most useful because its main purpose is to record the name of the student who has claimed the item. It directly helps complete the process of returning one's lost item.
