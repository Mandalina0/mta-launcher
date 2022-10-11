# Multi Theft Auto - Server Launcher

This is designed launcher for connecting your MTA servers. This coding for Roleplay servers but if you doing necessary edits you can using it on your freeroam servers.
To put it simply, the program runs and open the login screen. This screen includes a username and a password input. Username and password information is taken from your database. 
When the correct combination is entered, the main screen appears. This screen include a button that write "Connect to server". When clicked this button, program give a code.
At the same time this code processed on user account information. When the user enters the game, there are three input on the screen that appears. Username, Password and
a Login ID, When the code given in the launcher, username and password are entered, the game is entered. Thanks to a new entry called Login ID added to the login screen, the 
use of the Launcher becomes necessary.



## Installing Required Libraries

- The library used to design the graphical user interface (GUI) in the project

```
pip install pyqt5
```

- Library used to provide MySql connection

```
pip install mysql.connector
```
İf you are using sqlite;
```
pip install sqlite3
```

- Library used for windows notification
```
pip install plyer
```


## Using

You can download the .py file and run it directly. You just need to have a python debugger for this. 
(Don't forget the editing database information on .py file. This program using Prose-MTA roleplay packet.)

It is a newly started project. I will actively update.
