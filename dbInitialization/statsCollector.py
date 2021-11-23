import db
import requests
from playerStats import PlayerStats

SEASON_ID = 20212022

def main():
    db.connect()
    players = db.getPlayersFromDB()
    playerStats = []

    db.removePlayerStats()
    for player in players:
        stats = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(player.playerID) +
                                   '/stats?stats=statsSingleSeason&season=' + str(SEASON_ID))

        try:
            info = stats.json()["stats"][0]["splits"][0]["stat"]
            if player.position != "G":
                playerStats.append(PlayerStats(playerID=player.playerID, seasonID=SEASON_ID, gamesPlayed=info["games"],
                                               goals=info["goals"], assists=info["assists"], points=info["points"]))
            else:
                playerStats.append(PlayerStats(playerID=player.playerID, seasonID=SEASON_ID, gamesPlayed=info["games"],
                                               wins=info["wins"], shutouts=info["shutouts"]))
        except IndexError:
            playerStats.append(PlayerStats(playerID=player.playerID, seasonID=SEASON_ID))
            continue

    for player in playerStats:
        db.addPlayerStats(player)

    print("Stats added")

    db.close()

if __name__ == "__main__":
    main()