class NHLTeam:
    def __init__(self, teamID=0, teamName="", abbreviation=""):
        self.__teamID = teamID
        self.__teamName = teamName
        self.__abbreviation = abbreviation

    @property
    def teamID(self):
        return self.__teamID

    @property
    def teamName(self):
        return self.__teamName

    @property
    def abbreviation(self):
        return self.__abbreviation