import sqlite3
from contextlib import closing
import os
from flask import Flask, render_template, redirect, request, abort
import imghdr
from werkzeug.utils import secure_filename
#from dbInitialization import db
from dbInitialization.players import Player
from poolTeams import PoolTeam

app = Flask(__name__)
app.config["UPLOAD_PATH"] = "static/images"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jfif', '.jpeg']

#conn = sqlite3.connect("images.db", check_same_thread=False)
conn = sqlite3.connect("hockeyPool.db", check_same_thread=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/players")
def players():
    with closing(conn.cursor()) as c:
        query = '''Select * From players'''
        c.execute(query)
        results = c.fetchall()
        playerSelections = []
        for result in results:
            playerSelections.append(
                Player(playerID=result[0], teamID=result[1], firstName=result[2], lastName=result[3],
                       position=result[4], blockID=result[5]))

    teams = {}
    grabTeamAbbrevations(teams)

    return render_template("players.html", playerSelections=playerSelections, teams=teams)

@app.route("/players", methods = ['POST'])
def getPoolTeamData():
    uploaded_file = request.files["teamLogo"]
    teamName = request.values["teamName"]
    blockValues = []
    for i in range(21):
        blockValues.append(request.values["block"+str(i+1)])
    filename = secure_filename(uploaded_file.filename)
    username = "test"
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]: # or file_ext != validate_image(uploaded_file.stream): --> Taken out (can't get it to work)
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        with closing(conn.cursor()) as c:
            query = '''Insert into poolTeams(teamName, username, player1, player2, player3, player4, player5, player6,
                            player7, player8, player9, player10, player11, player12, player13, player14, player15,
                            player16, player17, player18, player19, player20, player21, teamLogo)
                        Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            c.execute(query, (teamName, username, blockValues[0], blockValues[1], blockValues[2], blockValues[3],
                              blockValues[4], blockValues[5], blockValues[6], blockValues[7], blockValues[8],
                              blockValues[9], blockValues[10], blockValues[11], blockValues[12], blockValues[13],
                              blockValues[14], blockValues[15], blockValues[16], blockValues[17], blockValues[18],
                              blockValues[19], blockValues[20], uploaded_file.filename))
            conn.commit()

    return redirect("index")

@app.route("/poolTeams")
def poolTeams():

    with closing(conn.cursor()) as c:
        query = '''Select * From poolTeams'''
        c.execute(query)
        results = c.fetchall()
        teamsInPool = []
        for result in results:
            teamRoster = (result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
                          result[11], result[12], result[13], result[14], result[15], result[16], result[17],
                          result[18], result[19], result[20], result[21], result[22], result[23])
            teamsInPool.append(
                [PoolTeam(teamID=result[0], teamName=result[1], username=result[2], teamLogo=result[24]), teamRoster])

    with closing(conn.cursor()) as c:
        query = '''Select * From players'''
        c.execute(query)
        results = c.fetchall()
        playerDictonary = {}
        for result in results:
            player = Player(teamID=result[1], firstName=result[2], lastName=result[3], position=result[4], blockID=result[5])
            playerDictonary[result[0]] = player
    teams = {}
    grabTeamAbbrevations(teams)

    return render_template("poolTeams.html", teamsInPool=teamsInPool, teams=teams, playerDictonary=playerDictonary)

@app.route("/photos")
def photos():
    with closing(conn.cursor()) as c:
        query = '''Select  * From Images'''
        c.execute(query)
        results = c.fetchall()
        images = []
        for result in results:
            images.append((result[1], result[2])) #index 1 is the file name

    return render_template("photos.html", images=images)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/update", methods = ['POST'])
def getFormData():
    uploaded_file = request.files["file"]
    caption = request.values["caption"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]: # or file_ext != validate_image(uploaded_file.stream): --> Taken out (can't get it to work)
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        with closing(conn.cursor()) as c:
            query = '''Insert into Images(Filename, Caption)
                        Values(?, ?)'''
            c.execute(query, (uploaded_file.filename, caption))
            conn.commit()

    return redirect("photos")

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

def grabTeamAbbrevations(teams):
    with closing(conn.cursor()) as c:
        query = '''Select teamID, abbreviation From nhlTeams'''
        c.execute(query)
        results = c.fetchall()
        for result in results:
            teams[result[0]] = result[1]