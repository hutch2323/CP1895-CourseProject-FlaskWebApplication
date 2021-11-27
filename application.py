import sqlite3
from contextlib import closing
import os
from flask import Flask, render_template, redirect, request, abort, session, url_for, escape
import imghdr
from werkzeug.utils import secure_filename
from poolTeams import PoolTeam
import addNewPoolTeam
import db

app = Flask(__name__)
app.config['DATABASE'] = "hockeyPool.db"
app.config["UPLOAD_PATH"] = "static/images"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jfif', '.jpeg']

conn = sqlite3.connect("hockeyPool.db", check_same_thread=False)

# home page of the application
@app.route("/")
def index():
    return render_template("index.html")

# route that handles the display of player/team options for a user creating a new hockey pool team
@app.route("/players")
def players():
    db.connect()
    playerSelections = db.getPlayersFromDB()

    teams = {}
    db.getTeamAbbrevations(teams)
    #db.close()
    return render_template("players.html", playerSelections=playerSelections, teams=teams)

# this handles the page where a user can create a hockey pool team. It will retrieve the submitted information and add
# it to the database
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

        db.connect()
        db.addPoolTeam(teamName, username, blockValues, uploaded_file.filename)
    #db.close()
    addNewPoolTeam.addNewTeam()
    return redirect("/")

# page that displays the team standings of all teams in the hockey pool
@app.route("/teamStandings")
def teamStandings():
    db.connect()
    teamStandings = db.getTeamStandings()
    return render_template("teamStandings.html", teamStandings=teamStandings)

# function to validate the image that was uploaded when a user creates a pool team
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

# dynamic route that will display the players on a specified team. This is used by the standings page to link each team
# to it's roster
@app.route("/teamStats/<teamID>")
def teamStats(teamID):
    team = 4
    db.connect()
    poolTeamIDs = db.getPoolTeamIDs()
    if teamID in poolTeamIDs:
        team = teamID
    playerStats = []
    selectedTeam = db.getPoolTeamByID(teamID)
    for player in selectedTeam.roster:
        playerStats.append(db.getPlayerStatsToDisplayWithID(player))

    return render_template("teamStats.html", teamID=teamID, selectedTeam=selectedTeam, playerStats=playerStats)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)