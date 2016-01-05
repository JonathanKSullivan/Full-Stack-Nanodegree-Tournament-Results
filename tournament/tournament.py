#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    con= connect()
    cur = con.cursor()
    sql="DELETE FROM Matches"
    cur.execute(sql)
    con.commit()
    con.close()

def deletePlayers():
    """Remove all the player records from the database."""
    con= connect()
    cur = con.cursor()
    sql="DELETE FROM PLAYERs"
    cur.execute(sql)
    con.commit()
    con.close()
    


def countPlayers():
    """Returns the number of players currently registered."""
    con= connect()
    cur = con.cursor()
    sql="SELECT COUNT(*) FROM PLAYERS"
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    con.close()
    return result[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    con= connect()
    cur = con.cursor()
    name= name.replace("'", "")
    sql="INSERT INTO PLAYERS (name, wins, matches) VALUES ('"+name+"',0,0);"
    cur.execute(sql)
    con.commit()
    con.close()
    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    con= connect()
    cur = con.cursor()
    sql="SELECT * FROM PLAYERS"
    cur.execute(sql)
    result= cur.fetchall()
    con.commit()
    con.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    con= connect()
    cur = con.cursor()
    sql="INSERT INTO MATCHES (WINNER, LOSER) VALUES ("+str(winner)+", "+str(loser)+")"
    cur.execute(sql)
    sql="SELECT WINS, MATCHES FROM PLAYERS WHERE ID ="+str(winner)
    cur.execute(sql)
    result = cur.fetchall()[0]
    wins= result[0] +1
    matches= result[1] + 1
    sql="UPDATE Players SET WINS="+str(wins)+", MATCHES="+str(matches)+" WHERE ID="+str(winner)
    cur.execute(sql)
    sql="SELECT MATCHES FROM PLAYERS WHERE ID ="+str(loser)
    cur.execute(sql)
    result = cur.fetchall()[0]
    matches= result[0]+1
    sql="UPDATE Players SET MATCHES="+str(matches)+" WHERE ID="+str(loser)
    cur.execute(sql)
    con.commit()
    con.close()
     
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    con= connect()
    cur = con.cursor()
    max_number = countPlayers()/2
    que = []
    pairs=[]
    for i in range(max_number):
        sql="SELECT id, name FROM Players where Wins="+str(i)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            if len(que)==0:
                que.append(row)
            else:
                pairs.append((row[0],row[1],que[0][0],que[0][1],))
                que=[]
        
    con.commit()
    con.close()
    return pairs

