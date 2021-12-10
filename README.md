# CP1895-CourseProject-FlaskWebApplication
CP1895 Course Project  -Flask Web Application - Box Hockey Pool

## Description:
This plugin was designed as the course project of CP1895: Advanced Python. This Python/Flask application will allow users to select a hockey team based off of "boxes" of options and allow them to see their team's stats as they compare to other user's teams. 

# Download & Installation
## Step 1:
- Download the files in the git repo https://github.com/hutch2323/CP1895-CourseProject-FlaskWebApplication or [click here](https://github.com/hutch2323/CP1895-CourseProject-FlaskWebApplication/archive/refs/heads/main.zip)
- Unzip the downloaded folder and all following files to your Python project.
- Note: All files located within [dbInitialization](https://github.com/hutch2323/CP1895-CourseProject-FlaskWebApplication/tree/main/dbInitialization) are not required for use. These are scripts that were ran to get initial information for players/teams from the NHL API
  
## Step 2:
In your Python Project, navigate to the terminal and run the following command in your virtual environment. This will use the [requirements.txt](https://github.com/hutch2323/CP1895-CourseProject-FlaskWebApplication/blob/main/requirements.txt). This will install all the modules used in the flask project.
```console
pip install flask
pip3 install -r requirements.txt
```

## Step 3:
From the terminal, run these commands to start the flask application.
```console
$env:Flask_APP="application"
$env:Flask_ENV="development"
flask run
```


# Using The Application:
Now that the application has been installed and is running, we will go over the instructions on how to use it.

## Sign Up
To get started with The Hockey Pool, you must first sign up and create an account. This option can be found in the upper right hand corner of the webpage.

## Step 1:
Click Login/Sign Up
![signUp](https://user-images.githubusercontent.com/59344045/145639851-2808ff3d-0b85-4037-81f6-c58e3e057fce.png)

## Step 2:
Click Sign Up <br>
![signUp2](https://user-images.githubusercontent.com/59344045/145639932-d62b93a5-3d05-4afa-95fb-d46318923a90.png)

## Step 3:
Fill out the signup form and submit
![signUp3](https://user-images.githubusercontent.com/59344045/145639962-6f19d738-33c3-4786-aa9e-e91d1e76f122.png)

## Login
Now that the account has been created, you'll be automatically redirected back to the login page. Fill out the information and click 'Login'.
![login](https://user-images.githubusercontent.com/59344045/145640077-e139dffc-23c6-4f23-a510-31d5c85893ea.png)

## Create Team

## Step 1:
Find the 'Create Team' link in the tool bar <br>
![createTeam0](https://user-images.githubusercontent.com/59344045/145640219-4248512f-e4f7-4f57-ad9b-e057c3754fc1.png)

## Step 2:
Fill out all information on the form. You must make a selection for all 21 groups <br>
![createTeam1](https://user-images.githubusercontent.com/59344045/145640267-7f84fa1e-e438-473b-8b8e-f5f73b05aa43.png)

## Step 3:
Click the 'Submit' button at the bottom of the form to create your team <br>
![createTeam2](https://user-images.githubusercontent.com/59344045/145640310-ea35da0a-9e90-4833-bbe7-cb79dfac6968.png)

## View Standings

## Step 1:
After you've successfully created your team, you will be automatically directed to the Team Standings page <br>
![viewStandings2](https://user-images.githubusercontent.com/59344045/145640390-462fda06-1bbd-4aa1-bec4-76be52ce60cd.png)

## Step 2:
Alternatively, you can select the 'Team Standings' link in the navigation bar above <br>
![viewStandings1](https://user-images.githubusercontent.com/59344045/145640437-f13e23ee-e883-422c-b7c1-cfe49e82f13c.png)

## View Team

## Step 1:
To view your team, click on your username (in the upper right-hand corner) and select 'View Team' from the drop-down <br>
![viewTeam1](https://user-images.githubusercontent.com/59344045/145640487-b932e7c1-77f9-4b72-960a-308873101a3c.png)

## Step 2:
Once this is clicked (or if the team name is clicked directly in the 'Team Standings' page, you will be brought to your team page <br>
![viewTeam2](https://user-images.githubusercontent.com/59344045/145640535-f0472a86-ff0d-4de8-b622-909b321a4480.png)
![viewTeam3](https://user-images.githubusercontent.com/59344045/145640542-dc9e27f3-2be9-412e-9a12-fa6dbce2bd29.png)

# Acknowledgements
Special thanks to [dword4](https://github.com/dword4) and their documentation of the NHL API at https://github.com/dword4/nhlapi
