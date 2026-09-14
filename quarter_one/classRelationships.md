# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Lost Item
Description: The LostItem class represents an item found within the school campus. It stores information such as the item's name, where and when it was found, its owner, and whether it has already been claimed.

## New Related Class
Class: Student
Description: The Student class represents a student who may claim one or more lost items. It stores the student's name, student ID, and section, and it can display the student's information.

## Association
Relationship: Student HAS-A / claims Lost Item.
Explanation: A Student can be associated with lost items that they have claimed.

## Multiplicity
Multiplicity: Student 1 ───────── 0..* lostItem
Explanation: One student can claim zero or more lost items.
