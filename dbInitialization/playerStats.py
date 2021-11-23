class PlayerStats():
    def __init__(self, playerID=None, seasonID=None, gamesPlayed=0, goals=0, assists=0, points=0, wins=0, shutouts=0):
        self.__playerID = playerID
        self.__seasonID = seasonID
        self.__gamesPlayed = gamesPlayed
        self.__goals = goals
        self.__assists = assists
        self.__points = points
        self.__wins = wins
        self.__shutouts = shutouts

    @property
    def playerID(self):
        return self.__playerID

    @property
    def seasonID(self):
        return self.__seasonID

    @property
    def gamesPlayed(self):
        return self.__gamesPlayed

    @property
    def goals(self):
        return self.__goals

    @property
    def assists(self):
        return self.__assists

    @property
    def points(self):
        return self.__points

    @property
    def wins(self):
        return self.__wins

    @property
    def shutouts(self):
        return self.__shutouts