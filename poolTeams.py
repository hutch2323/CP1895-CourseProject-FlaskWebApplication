# adding a comment to test the commits
# Test #2 for committing

class PoolTeam:
    def __init__(self, teamID=0, teamName="", username="", roster=[], teamLogo=""):

        self.__teamID = teamID
        self.__teamName = teamName
        self.__username = username
        self.__roster = roster
        self.__teamLogo = teamLogo

    @property
    def teamID(self):
        return self.__teamID

    @teamID.setter
    def teamID(self, teamID):
        self.__teamID = teamID

    @property
    def teamName(self):
        return self.__teamName

    @teamName.setter
    def teamName(self, teamName):
        self.__teamName = teamName

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def roster(self):
        return self.__roster

    @roster.setter
    def roster(self, roster):
        self.__roster = roster

    @property
    def teamLogo(self):
        return self.__teamLogo

    @teamLogo.setter
    def teamLogo(self, teamLogo):
        self.__teamLogo = teamLogo