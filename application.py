import sqlite3
from contextlib import closing
import os
from flask import Flask, render_template, redirect, request, abort, flash, session, url_for, escape, jsonify, json
import imghdr
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from apscheduler.schedulers.background import BackgroundScheduler
import updatePoolTeams
from statsCollector import collectStats
import db
from user import User
import random
from pytz import utc
from updatePoolTeams import updateTeams


# db = SQLAlchemy
DB_NAME = "hockeyPool.db"

def updateStats():
    number = random.randint(0, 25)
    print(number)

# cron job to run at 3AM NST (6:30 AM UTC) every morning. This will ping the NHL API to grab the player stats and
# update standings
cron = BackgroundScheduler(daemon=True)
cron.add_job(collectStats, 'cron', day_of_week='mon-sun', hour=6, minute=30, timezone=utc)
cron.start()

app = Flask(__name__)
app.config['SECRET_KEY'] = "thdhshsh sshsrhrsdhs"
app.config['DATABASE'] = "hockeyPool.db"
app.config["UPLOAD_PATH"] = "static/images"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jfif', '.jpeg']
# app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
# db.init_app(app)
# conn = sqlite3.connect("hockeyPool.db", check_same_thread=False)
# app = create_app()
#
# if __name__ == "__main__":
#     app.run(debug=True)



# home page of the application
@app.route("/")
def index():
    return render_template("index.html", username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    # db.close()

def userTeam():
    while (True):
        try:
            db.connect()
            username = None
            teamInPool = False
            if "username" in session:
                username = session["username"]
                if (db.checkForUserInPool(username)):
                    teamInPool = True
            return teamInPool
        except sqlite3.ProgrammingError:
            db.close()

def getUserInfo():
    username = None
    if "username" in session:
        username = session["username"]
    return username

def getUserPermission():
    permission = None
    if "permission" in session:
        permission = session["permission"]
    return permission

@app.route("/login")
def login():
    if "username" not in session:
        return render_template("login.html", username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    return redirect(url_for('index'))

@app.route("/login", methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if db.checkForUser(username):
            user = db.getUserInfo(username)
            if check_password_hash(user.password, password):
                session['username'] = user.username
                session['permission'] = user.permission
                return redirect(url_for('index'))
            else:
                flash("Invalid password", category="error")
        else:
            flash("Invalid username or user does not exist", category="error")


    return render_template("login.html", username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    # db.close()

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("logout.html", username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())

@app.route("/signUp")
def signUp():
    if "username" not in session:
        return render_template("signUp.html", username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    return redirect(url_for('index'))

@app.route("/signUp", methods=['GET', 'POST'])
def getSignupData():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(username) < 4:
            flash("Username must be greater than 3 characters.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif len(lastName) < 2:
            flash("Last name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passswords don\'t match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least than 7 characters.", category="error")
        else:
            if not db.checkForUser(username):
                if not db.checkForEmail(email):
                    user = User(username=username, password=generate_password_hash(password1), firstName=firstName,
                                    lastName=lastName, emailAddress=email)

                    db.connect()
                    db.addNewUser(user)
                    flash("Account created!", category="success")
                    return redirect(url_for("login"))
                else:
                    flash("Email address already exists.", category="error")
            else:
                flash("Username already exists.", category="error")

    # return render_template("login")

# route that handles the display of player/team options for a user creating a new hockey pool team
@app.route("/players")
def players():
    db.connect()

    playerSelections = db.getPlayersFromDB()

    teams = {}
    db.getTeamAbbrevations(teams)
    #db.close()
    return render_template("players.html", playerSelections=playerSelections, teams=teams, username=getUserInfo(),
                           permission=getUserPermission(), teamInPool=userTeam())
    # db.close()

# this handles the page where a user can create a hockey pool team. It will retrieve the submitted information and add
# it to the database
@app.route("/players", methods = ['GET', 'POST'])
def getPoolTeamData():
    uploaded_file = request.files["teamLogo"]
    teamName = request.values["teamName"]
    blockValues = []
    for i in range(21):
        blockValues.append(request.values["block"+str(i+1)])
    filename = secure_filename(uploaded_file.filename)
    username = session["username"]
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]: # or file_ext != validate_image(uploaded_file.stream): --> Taken out (can't get it to work)
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        db.addPoolTeam(teamName, username, blockValues, uploaded_file.filename)
    #db.close()
    updatePoolTeams.caclulateStandings()
    return redirect(url_for('index'))
    # db.close()

# page that displays the team standings of all teams in the hockey pool
@app.route("/teamStandings")
def teamStandings():
    while True:
        try:
            db.connect()
            teamStandings = db.getTeamStandings()
            return render_template("teamStandings.html", teamStandings=teamStandings, username=getUserInfo(),
                                   permission=getUserPermission(), teamInPool=userTeam())
        except sqlite3.ProgrammingError:
            db.close()
    # db.close()

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
    db.connect()
    poolTeamIDs = db.getPoolTeamIDs()
    if teamID in poolTeamIDs:
        team = teamID
    playerStats = []
    selectedTeam = db.getPoolTeamByID(teamID)
    for player in selectedTeam.roster:
        playerStats.append(db.getPlayerStatsToDisplayWithID(player))

    return render_template("teamStats.html", teamID=teamID, selectedTeam=selectedTeam, playerStats=playerStats,
                           username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    # db.close()

@app.route("/admin")
def admin():
    if "permission" in session:
        if session["permission"] == "admin":
            db.connect()
            poolTeams = db.getPoolTeams()
            users = db.getUsers()
            return render_template("admin.html", poolTeams=poolTeams, users=users, username=getUserInfo(),
                                   permission=getUserPermission(), teamInPool=userTeam())
    return redirect(url_for('index'))

@app.route("/modifyUser/<username>")
def modifyUser(username):
    if ("permission" in session) and (session["permission"] == "admin"):
        db.connect()
        user = db.getUserInfo(username)
        return render_template("modifyUser.html", userToModify=user, username=getUserInfo(),
                               permission=getUserPermission(), teamInPool=userTeam())
    elif "username" in session:
        if session["username"] == username:
            db.connect()
            user = db.getUserInfo(session["username"])
            return render_template("modifyUser.html", userToModify=user, username=getUserInfo(),
                                   permission=getUserPermission(), teamInPool=userTeam())

    return redirect(url_for('index'))

@app.route("/modifyUser/<username>", methods = ['GET', 'POST'])
def modifingUser(username):
    db.connect()
    originalUserData = db.getUserInfo(username)
    if request.method == 'POST':
        usernameForm = request.form.get("username")
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        print("Password1 = " + password1)
        password2 = request.form.get("password2")
        permission = request.form.get("permission")

        # if len(username) < 4:
        #     flash("Username must be greater than 3 characters.", category="error")
        # elif len(email) < 4:
        #     flash("Email must be greater than 3 characters.", category="error")
        # elif len(firstName) < 2:
        #     flash("First name must be greater than 1 character.", category="error")
        # elif len(lastName) < 2:
        #     flash("Last name must be greater than 1 character.", category="error")
        # elif password1 != password2:
        #     flash("Passswords don\'t match.", category="error")
        # elif len(password1) < 7:
        #     flash("Password must be at least than 7 characters.", category="error")
        # else:
        if (originalUserData.username == usernameForm) or (not db.checkForUser(usernameForm)):
            if (originalUserData.emailAddress == email) or (not db.checkForEmail(email)):
                user = User(username=usernameForm, password=generate_password_hash(password1), firstName=firstName,
                            lastName=lastName, emailAddress=email, permission=permission)
                if password1 == "":
                    db.modifyUserNoPassword(username, user)
                else:
                    db.modifyUser(username, user)

                if (originalUserData.username != user.username):
                    db.modifyPoolTeamUser(originalUserData.username, user)
                return redirect(url_for("admin"))
            else:
                flash("Email address already exists.", category="error")
        else:
            flash("Username already exists.", category="error")


@app.route("/modifyTeam/<team>")
def modifyTeam(team):
    if "permission" in session:
        if session["permission"] == "admin":
            db.connect()
            playerSelections = db.getPlayersFromDB()
            teams = {}
            db.getTeamAbbrevations(teams)
            poolTeam = db.getPoolTeamByTeamName(team)
            return render_template("modifyTeam.html", playerSelections=playerSelections, teams=teams, poolTeam=poolTeam,
                                   username=getUserInfo(), permission=getUserPermission(), teamInPool=userTeam())
    return redirect(url_for('index'))

@app.route("/modifyTeam/<team>", methods = ['GET', 'POST'])
def modifingTeam(team):
    originalTeamName = team
    print(originalTeamName)
    uploaded_file = request.files["teamLogo"]
    teamName = request.values["teamName"]
    blockValues = []
    for i in range(21):
        blockValues.append(request.values["block" + str(i + 1)])
    filename = secure_filename(uploaded_file.filename)
    username = session["username"]
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config[
            "UPLOAD_EXTENSIONS"]:  # or file_ext != validate_image(uploaded_file.stream): --> Taken out (can't get it to work)
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        db.updatePoolTeam(originalTeamName, teamName, username, blockValues, uploaded_file.filename)
    # db.close()
    return redirect(url_for('admin'))

@app.route("/admin", methods = ['GET', 'POST'])
def getAdminCommand():
    db.connect()
    try:
        teamNameModify = request.values["teamModify"]
        updatePoolTeams.updateTeams()
        return redirect(url_for('modifyTeam', team=teamNameModify))
    except KeyError:
        pass

    try:
        teamNameDelete = request.values["teamRemoval"]
        db.deletePoolTeam(teamNameDelete)
        updatePoolTeams.updateTeams();
        return redirect(url_for('admin'))
    except KeyError:
        pass

    try:
        usernameModify = request.values["userModify"]
        return redirect(url_for('modifyUser', username=usernameModify))
    except KeyError:
        pass

    try:
        usernameDelete = request.values["userRemoval"]
        db.deleteUser(usernameDelete)
        db.removeUserPoolTeam(usernameDelete)
        updatePoolTeams.updateTeams();
        return redirect(url_for('admin'))
    except KeyError:
        pass

# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)

# @app.route('/background_process')
# def background_process():
#     try:
#         team = request.args.get('teamSelection', 0, type=str)
#         return jsonify(teamName=team.teamName, username=team.userName)
#     except Exception as e:
#         return str(e)