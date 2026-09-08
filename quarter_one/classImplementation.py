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
