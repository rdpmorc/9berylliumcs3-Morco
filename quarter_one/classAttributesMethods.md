# Class Attributes and Methods
## Previous Design
Link to my previous activity:
https://github.com/rdpmorc/9berylliumcs3-Morco/blob/64835d368472480e9eda46a0e5111beb1cc8d124/quarter_one/classObjectUML.md

## Design Revision
Added new properties and methods to classObjectUML.

## Visibility Decisions
| Attribute | Data Type | Visibility |                    Reason                    |
|-----------|-----------|------------|----------------------------------------------|
|itemName   |string     |Public      |It shows the students the lost item.          |
|placeFound |string     |Public      |It shows the students where the item was found. |
|ownerName  |string     |Private     |It keeps the owner of the item private, only visible to the school. |
|dateFound  |int        |Public      |It shows the students when the item was found. |
|claimed    |boolean    |Private     |It shows the school whether the item has been claimed or not. |
|dateClaimed|int        |Private     |It shows the school when the item has been claimed. |
