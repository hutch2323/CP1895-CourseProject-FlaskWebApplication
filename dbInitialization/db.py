import os
import sys
import sqlite3
from contextlib import closing
from dbInitialization.nhlTeams import NHLTeam
from dbInitialization.players import Player
from dbInitialization.poolTeams import PoolTeam

conn = None
DB_FILENAME = "../hockeyPool.db"

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = DB_FILENAME
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + DB_FILENAME

        conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def addNHLTeamToDB(team):
    sql = '''INSERT INTO nhlTeams (teamID, teamName, abbreviation)
                  VALUES (?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (team.teamID, team.teamName, team.abbreviation))
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def removeNHLTeams():
    sql = '''DELETE FROM nhlTeams'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getNHLTeamID(abbreviation):
    sql = '''SELECT teamID
                    FROM nhlTeams
                    WHERE abbreviation = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (abbreviation,))
            result = c.fetchone()
            team = makeTeamWithID(result)
            return team
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getAllNHLTeamIDs():
    sql = '''SELECT teamID
                FROM nhlTeams'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            results = c.fetchall()
        teams = []
        for row in results:
            teams.append(makeTeamWithID(row))
        return teams
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def makeTeamWithID(row):
    return NHLTeam(teamID=row["teamID"])

def addPlayerToDB(player):
    sql = '''INSERT INTO players (playerID, teamID, firstName, lastName, position, blockID)
                      VALUES (?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.playerID, player.teamID, player.firstName, player.lastName, player.position, player.blockID))
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def removePlayersFromDB():
    sql = '''DELETE FROM players'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getPlayersFromDB():
    sql = '''SELECT *
                FROM players'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            results = c.fetchall()
        players = []
        for row in results:
            players.append(makePlayer(row))
        return players
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def removePlayerStats():
    sql = '''DELETE FROM playerStats'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def addPlayerStats(player):
    sql = '''INSERT INTO playerStats (playerID, seasonID, gamesPlayed, goals, assists, points, wins, shutouts)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.playerID, player.seasonID, player.gamesPlayed, player.goals, player.assists,
                            (player.points + player.wins + player.shutouts*2), player.wins, player.shutouts))
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def isPlayer(player):
    sql = '''SELECT *
                    FROM Player
                    WHERE playerID = ? AND position <> "G"'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.playerID,))
            result = c.fetchone()
            if result:
                return True
            else:
                return False
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getPlayerStatsToDisplay(player):
    sql = '''Select p.blockID, p.firstName, p.lastName, t.abbreviation, p.position, ps.gamesPlayed,
	            ps.goals, ps.assists, ps.points, ps.wins, ps.shutouts
             From playerStats ps join players p
	            on ps.playerID = p.playerID
	         join nhlTeams t
	            on p.teamID = t.teamID
             Where p.playerID = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.playerID,))
            result = c.fetchone()
        return result
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def makePlayer(row):
    return Player(playerID=row["playerID"], teamID=row["teamID"], firstName=row["firstName"], lastName=row["lastName"],
                  position=row["position"], blockID=row["blockID"])

def getPoolTeams():
    try:
        with closing(conn.cursor()) as c:
            query = '''Select * From poolTeams'''
            c.execute(query)
            results = c.fetchall()
            teamsInPool = []
            for result in results:
                teamRoster = [result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
                              result[11], result[12], result[13], result[14], result[15], result[16], result[17],
                              result[18], result[19], result[20], result[21], result[22], result[23]]
                teamsInPool.append(
                    PoolTeam(teamID=result[0], teamName=result[1], username=result[2], teamLogo=result[24], roster=teamRoster))
            return teamsInPool
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getPlayerPoints(playerID):
    try:
        with closing(conn.cursor()) as c:

            query = '''Select points From playerStats
                        Where playerID = ?;'''
            c.execute(query, (playerID,))
            results = c.fetchone()
        return results[0]
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getTeamStats(teamID):
    try:
        with closing(conn.cursor()) as c:
            query = '''Select teamID, points, pointsYesterday, rank, rankYesterday
                        From standings
                        Where teamID = ?'''
            c.execute(query, (teamID,))
            # teamStandings = []
            results = c.fetchall()
            for row in results:
                return [row[0], row[1], row[2], row[3], row[4]]
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def removeTeamStats():
    sql = '''DELETE FROM standings'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def setTeamStats(teamStats):
    sql = '''INSERT INTO standings (teamID, points, pointsYesterday, rank, rankYesterday)
                          VALUES (?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4]))
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)
        sys.exit()

def getTeamStandings():
    sql = '''Select pt.teamID, pt.teamName, s.points, s.pointsYesterday, s.rank, s.rankYesterday
                     From poolTeams pt join standings s
                        on pt.teamID = s.teamID
                    Order by s.points DESC'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            results = c.fetchall()
            standings = []
            for result in results:
                standings.append((result[0], result[1], result[2], result[3], result[4], result[5]))
            return standings
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)

def getPoolTeamIDs():
    sql = '''Select teamID from poolTeams'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql)
            results = c.fetchall()
            poolTeams = []
            for result in results:
                poolTeams.append(result[0])

            return poolTeams
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)

def hasTeamStats(teamID):
    sql = '''Select * from standings
                where teamID = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (teamID,))
            results = c.fetchone()
            if(results):
                return True
            else:
                return False
    except sqlite3.OperationalError as e:
        print("Error: Database could not be read. Program closing")
        print(e)