import db

def main():
    db.connect()

    players = db.getPlayersFromDB()

    for player in players:
        playerStats = db.getPlayerStatsToDisplay(player)
        if playerStats[4] != "G":
            print(str(playerStats[0]) + " " + playerStats[1] + " " + playerStats[2] + " " + playerStats[3] + " " +
                  playerStats[4] + " " + str(playerStats[5]) + " " + str(playerStats[6]) + " " + str(playerStats[7])
                  + " " + str(playerStats[8]))
        else:
            print(str(playerStats[0]) + " " + playerStats[1] + " " + playerStats[2] + " " + playerStats[3] + " " +
                  playerStats[4] + " " + str(playerStats[5]) + " " + str(playerStats[9]) + " " +
                  str(playerStats[10]))

    db.close()

if __name__ == "__main__":
    main()