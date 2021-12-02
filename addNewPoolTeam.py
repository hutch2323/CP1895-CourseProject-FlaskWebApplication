import db

def addNewTeam():
    db.connect()
    poolTeams = db.getPoolTeams()
    teamStandings = []
    for team in poolTeams:
        # if team doesn't exist in the standings, add it:
        if not db.hasTeamStats(team.teamID):
            pointsYesterday = 0
            points = 0

            for player in team.roster:
                points += db.getPlayerPoints(player)
            print(team.teamName + " - " + str(points) + " points.")

            teamStats = [team.teamID, points, points, 0, 0]
            db.setTeamStats(teamStats)
            teamStandings.append(teamStats)
        else:
            teamStats = db.getTeamStats(team.teamID)
            teamStandings.append(teamStats)

    teamStandings.sort(key=lambda x: x[1], reverse=True)
    print("Team Standings")
    count = 1
    for team in teamStandings:
        team[3] = count
        # if the team was just added, set yesterday's ranking to their first ranking
        if team[4] == 0:
            team[4] = count
        count += 1

    print(teamStandings)

    db.removeTeamStats()
    for team in teamStandings:
        db.setTeamStats(team)

    db.close()
    print("Standings updated after new team added")
    return

def main():
    addNewTeam()

if __name__ == "__main__":
    main()