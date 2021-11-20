import os
import sys
import sqlite3
from contextlib import closing
from nhlTeams import NHLTeam

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

        conn = sqlite3.connect(DB_FILE)
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
