import json
import requests
import db
from nhlTeams import NHLTeam

def main():
    db.connect()
    teams = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

    # remove previously stored teams
    db.removeNHLTeams()

    for team in teams.json()["teams"]:
        print(str(team["id"]) + " - " + team["name"] + " (" + team["abbreviation"] + ")")
        nhlTeam = NHLTeam(team["id"], team["name"], team["abbreviation"])
        db.addNHLTeamToDB(nhlTeam)

    db.close()

if __name__ == "__main__":
    main()