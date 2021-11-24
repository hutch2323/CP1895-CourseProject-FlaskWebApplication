import db

def main():
    db.connect()
    poolTeams = db.getPoolTeams()

    teamStandings = []
    for team in poolTeams:
        pointsYesterday = 0
        points = 0

        for player in team.roster:
            points += db.getPlayerPoints(player)
        print(team.teamName + " - " + str(points) + " points.")

        teamStats = db.getTeamStats(team.teamID)

        if len(teamStats) == 0:
            teamStats = [team.teamID, points, points, 0, 0]
            db.setTeamStats(teamStats)
        else:
            teamStats[2] = teamStats[1]
            teamStats[4] = teamStats[3]
            teamStats[1] = points
            teamStandings.append(teamStats)

        print(teamStats)

    teamStandings.sort(key=lambda x: x[1], reverse=True)
    print("Team Standings")
    count = 1
    for team in teamStandings:
        team[4] = team[3]
        team[3] = count
        count += 1

    print(teamStandings)

    db.removeTeamStats()
    for team in teamStandings:
        db.setTeamStats(team)

    print("Standings updated")
    db.close()

if __name__ == "__main__":
    main()