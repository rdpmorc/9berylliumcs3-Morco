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
