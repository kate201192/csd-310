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

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

players = cursor.fetchall()

for player in players:
        print("  player id: {}  first name: {} last name: {}  team name: {}".format(player[0], player[1], player[2], player[3]))
