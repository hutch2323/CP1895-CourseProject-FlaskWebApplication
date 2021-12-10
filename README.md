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


## Step 2:
After a team has been selected in Step 1, click the Proceed button.<br>
![button](https://user-images.githubusercontent.com/59344045/144542256-77937fc3-37d3-4c49-87f5-01a02650e3c1.png)

## Step 3:
Once the button is clicked, the plugin will initiate and a popup overlay will be displayed over the current content of the webpage. There is an "X" located in the upper right hand corner of the popup that must be clicked in order to close it. While the popup is open, another instance of the popup cannot be generated. It must be first closed and then restart the process. To prevent such actions, the Proceed button becomes disabled once the popup is launched and will only be re-enabled once it has been closed.<br>
![popup-demo1](https://user-images.githubusercontent.com/59344045/144542437-18d908cc-6cbd-437c-a5a4-ee24af03860a.png)
![popup-demo2](https://user-images.githubusercontent.com/59344045/144542443-87544fc0-66a6-4271-9f0d-d2d9ea988557.png)

# Acknowledgements
Special thanks to [dword4](https://github.com/dword4) and their documentation of the NHL API at https://github.com/dword4/nhlapi
