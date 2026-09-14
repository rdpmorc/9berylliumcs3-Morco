class LostItem:
    def __init__(self, itemName, placeFound, dateFound):
        self.itemName = itemName
        self.placeFound = placeFound
        self.__dateFound = dateFound
        self.ownerName = "Unknown"
        self.__claimed = False
        self.__dateClaimed = 0

    def claimItem(self, owner):
        self.ownerName = owner.studentName
        self.markAsClaimed()

    def addPlace(self, place):
        self.placeFound = place

    def addDate(self, date):
        self.__dateFound = date

    def markAsClaimed(self):
        self.__claimed = True
        self.__dateClaimed = 91426

    def displayInfo(self):
        print("Item:", self.itemName)
        print("Place Found:", self.placeFound)
        print("Owner:", self.ownerName)
        print("Claimed:", self.__claimed)


class Student:
    def __init__(self, studentName, studentID, section):
        self.studentName = studentName
        self.studentID = studentID
        self.section = section
        self.claimedItems = []

    def addClaimedItem(self, item):
        self.claimedItems.append(item)

    def displayInfo(self):
        print("Student:", self.studentName)
        print("Student ID:", self.studentID)
        print("Section:", self.section)
