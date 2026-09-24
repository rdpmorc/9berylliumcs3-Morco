class LostItem:
    def __init__(self, itemName, placeFound, dateFound, ownerName, dateClaimed, claimed):
        self.itemName = itemName
        self.__placeFound = placeFound
        self.__dateFound = dateFound
        self.ownerName = ownerName
        self.__claimed = claimed
        self.__dateClaimed = dateClaimed

    def addPlace(self, place):
        self.__placeFound = place

    def changeDateFound(self, date):
        self.__dateFound = date

    def markAsClaimed(self):
        self.__claimed = True

    def claimItem(self, owner, date):
        self.markAsClaimed()
        self.ownerName = owner
        self.__dateClaimed = date

    def displayInfo(self):
        print(f"Item Name: {self.itemName}")
        print(f"Owner: {self.ownerName}")
        print(f"Place Found: {self.__placeFound}")
        print(f"Date Found: {self.__dateFound}")
        print(f"Status: {self.__claimed}")
        print(f"Date Claimed: {self.__dateClaimed}")


class Student:
    def __init__(self, studentName, studentID, section):
        self.studentName = studentName
        self.studentID = studentID
        self.section = section

    def displayInfo(self):
        print(f"Student Name: {self.studentName}")
        print(f"Student ID: {self.studentID}")
        print(f"Section: {self.section}")


class ClaimingStudent(Student):
    def __init__(self, studentName, studentID, section):
        super().__init__(studentName, studentID, section)
        self.claimedItems = []

    def addClaimedItem(self, item):
        self.claimedItems.append(item)

    def displayInfo(self):
        super().displayInfo()
        print(f"Claimed Items: {len(self.claimedItems)}")

# CREATE OBJECTS :

student1 = ClaimingStudent(
    "Juan Dela Cruz",
    "2026-001",
    "CS3"
)

item1 = LostItem(
    "Black Wallet",
    "School Canteen",
    90926,
    "Unknown",
    0,
    False
)

item2 = LostItem(
    "Blue Umbrella",
    "School Library",
    91026,
    "Unknown",
    0,
    False
)

item3 = LostItem(
    "Scientific Calculator",
    "Room 204",
    91126,
    "Unknown",
    0,
    False
)


# TEST 1 — INHERITANCE :

print("TEST 1: INHERITANCE")

student1.displayInfo()

print("\nInherited attributes:")
print(f"Student Name: {student1.studentName}")
print(f"Student ID: {student1.studentID}")
print(f"Section: {student1.section}")


# TEST 2 — AGGREGATION :

print("\nTEST 2: AGGREGATION")

print("Adding existing LostItem objects to ClaimingStudent...")

student1.addClaimedItem(item1)
student1.addClaimedItem(item2)
student1.addClaimedItem(item3)

item1.claimItem(student1.studentName, 91426)
item2.claimItem(student1.studentName, 91426)
item3.claimItem(student1.studentName, 91426)

print("\nClaiming Student:")
student1.displayInfo()

print("\nRelated Lost Items:")

for item in student1.claimedItems:
    print(f"- {item.itemName}")
