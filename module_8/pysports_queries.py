import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysport_User",
    "password": "password",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("TEAMS")
for team in teams: 
        print("  team ID: {} team name: {} mascot: {}\n".format(team[0], team[1], team[2]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor.fetchall()

print ("players")

for player in players:
        print("  player ID: {} first name: {}  last Name: {}   id: {}\n".format(player[0], player[1], player[2], player[3]))
