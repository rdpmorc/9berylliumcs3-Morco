# Advanced Class Relationships

## Previous Activities
[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)

## Existing System Description:

## Inheritance Relationship
Parent: Student
Child: ClaimingStudent
Explanation: A ClaimingStudent IS-A Student because it represents a student who has an additional feature of
managing lost items that they have claimed.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship: Aggregation

Explanation: ClaimingStudent aggregates LostItem objects through its claimedItems list. The LostItem objects can exist independently because they are created before they are added to the student's list. Therefore, the LostItem does not completely depend on the ClaimingStudent.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
