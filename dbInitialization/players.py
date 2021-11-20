class Player:
    def __init__(self, playerID=0, teamID=0, firstName="", lastName="", position="", blockID=0):
        self.__playerID = playerID
        self.__teamID = teamID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__position = position
        self.__blockID = blockID

    @property
    def playerID(self):
        return self.__playerID

    @playerID.setter
    def playerID(self, playerID):
        self.__playerID = playerID

    @property
    def teamID(self):
        return self.__teamID

    @teamID.setter
    def teamID(self, teamID):
        self.__teamID = teamID

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName):
        return self.__lastName

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def blockID(self):
        return self.__blockID

    @blockID.setter
    def blockID(self, blockID):
        self.__blockID = blockID