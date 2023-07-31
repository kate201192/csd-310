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

def show_players(cursor, title):

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
      
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    player_data = ("Smeagol", "Shire Folk", 1)

    cursor.execute(add_player, player_data)

    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")


finally:
    db.close()


