import csv
import sys
from players import Player
from nhlTeams import NHLTeam
import db
import requests

def getPlayersFromFile(players):
    db.connect()
    fileName = "players.csv"
    try:
        with open(fileName, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].split()
                player = Player(firstName=name[0], lastName=name[1], teamID=db.getNHLTeamID(row[1]).teamID, blockID=row[2])
                players.append(player)
    except FileNotFoundError:
        print("Error: File Not Found. Exiting Program")
        sys.exit()
    except Exception as e:
        print("Unexpected error has occured. Exiting Program")
        print(type(e), e)
        sys.exit()
    db.close

def getPlayerInfo(players):
    for player in players:
        playerMatch = False
        playerInfo = requests.get('https://statsapi.web.nhl.com/api/v1/teams/' + str(player.teamID) + '/roster')
        for info in playerInfo.json()["roster"]:
            if (player.firstName + " " + player.lastName) == info["person"]["fullName"]:
                player.playerID = info["person"]["id"]
                player.position = info["position"]["abbreviation"]
                playerMatch = True

        if not playerMatch:
            print(player.firstName + " " + player.lastName + " has no match")
            playerInfo = requests.get('https://statsapi.web.nhl.com/api/v1/teams/' + str(player.teamID) + '?expand=team.roster&season=20202021')
            for info in playerInfo.json()["teams"][0]["roster"]["roster"]:
                if (player.firstName + " " + player.lastName) == info["person"]["fullName"]:
                    player.playerID = info["person"]["id"]
                    player.position = info["position"]["abbreviation"]
                    playerMatch = True
                    print(player.firstName + " " + player.lastName + " now matched")

            if not playerMatch:
                print(player.firstName + " " + player.lastName + " still has no match")

def addPlayersToDB(players):
    db.connect()
    db.removePlayersFromDB()
    for player in players:
        db.addPlayerToDB(player)
    db.close()

def main():
    players = []
    getPlayersFromFile(players)
    getPlayerInfo(players)
    addPlayersToDB(players)
    # playerIDs = []
    # for player in players:
    #     playerIDs.append(player.playerID)
    #     # print(player.playerID, player.teamID, player.firstName, player.lastName, player.position, player.blockID)
    #
    # if len(playerIDs) == len(set(playerIDs)):
    #     print("No duplicates")
    # else:
    #     print("Duplicates")



if __name__ == "__main__":
    main()