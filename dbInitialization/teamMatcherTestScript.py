import db

def main():
    db.connect()
    teamID = 2
    poolTeams = db.getPoolTeamIDs()

    if teamID in poolTeams:
        print("Match Found!")
    else:
        print("No match found!")
    # for poolTeam in poolTeams:
    #     if teamID == poolTeam:
    #         team = teamID
    db.close()

if __name__ == "__main__":
    main()