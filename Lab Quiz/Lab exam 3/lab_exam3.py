# File: lab_exam3.py
# Name: Carole (Chia Jung) Sung
# Date: Mar 21 2018
# Details: Lab exam 3 for CS108

################################################################################
def encode(s):
    '''returns a list of ASCII codes for a given string s.'''
    lst = []
    for letter in s:
        lst.append(ord(letter))
    return lst

###############
def print_histogram(data):
    '''processes a dictionary the parameter data and creates a histogram
    illustrating the keys and their associated counts.'''
    keys = data.keys()
    for k in keys:
        print("%-15s"%(k),'*'*data[k])


################################################################################
import sqlite3
def build_database():
    '''A helper function to create a database file and populate some data.'''

    # open (create) the database
    conn = sqlite3.connect("./hockey.db")
    cur = conn.cursor()

    # drop tables if they already exist:
    try:
        sql = "DROP TABLE teams"
        cur.execute(sql)
    except:
        pass # don't worry about it!
    try:
        sql = "DROP TABLE players"
        cur.execute(sql)
    except:
        pass # don't worry about it!
    
    # create some teams:
    sql = "CREATE TABLE teams (teamid int, hometown string, teamname string)"
    cur.execute(sql)
    
    sql = '''INSERT INTO teams VALUES (1, "Boston", "Bruins")'''
    cur.execute(sql)
    
    sql = '''INSERT INTO teams VALUES (2, "Montreal", "Canadiens")'''
    cur.execute(sql)
    
    sql = '''INSERT INTO teams VALUES (3, "Toronto", "Maple Leafs")'''
    cur.execute(sql)
    
    sql = '''INSERT INTO teams VALUES (4, "Chicago", "Blackhawks")'''
    cur.execute(sql)


    # create some players:
    sql = '''CREATE TABLE players(playerid int, lastname string, firstname string, position string, teamid int)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (1, 'Marchand', 'Brad', 'LW', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (2, 'Chara', 'Zdeno', 'D', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (3, 'Subban', 'Malcolm', 'G', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (4, 'Bergeron', 'Patrice', 'C', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (5, 'Rask', 'Tuukka', 'G', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (6, 'McQuaid', 'Adam', 'D', 1)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (7, 'Desharnais', 'David', 'C', 2)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (8, 'Galchenyuk', 'Alex', 'C', 2)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (9, 'Price', 'Carey', 'G', 2)'''
    cur.execute(sql)
    
    sql = '''INSERT INTO players VALUES (11, 'Petry', 'Jeff', 'D', 2)'''
    cur.execute(sql)
    
    # commit the changes!
    conn.commit()
    conn.close()

################################################################################
def get_players_by_position(position):
    '''Executes a query against the hockey database, and returns a recordset
    containing the team name, team hometown, player last name, player firstname,
    of players that match the specified position.'''
    
    conn = sqlite3.connect("./hockey.db")
    cur = conn.cursor()

    # obtains a list of:
    # team name, team hometown, player last name, and player firstname
    # for all players matching the function parameter `position`
    sql='SELECT teamname,hometown,lastname,firstname,position FROM teams INNER JOIN players WHERE teams.teamid=players.teamid'
    cur.execute(sql)
    results = cur.fetchall()

 
    # clean up
    cur.close()
    conn.close()
    
    #return the data from the query:
    #return data
    lst = []
    for i in results:
        if i[4] == position:
            lst+=[(i[0],i[1],i[2],i[3])]

    return lst

################################################################################
#Test Cases:
print(encode('goodbye'))
print(encode('hello'))
print('\n')
data = {"reg. coffee": 9, "diet-coke": 4, "red bull": 11, "mocha latte": 7, "green tea": 2}
print_histogram(data)
print('\n')

##build_database()
print("get_players_by_position('D') returned", get_players_by_position('D'))
print("get_players_by_position('G') returned", get_players_by_position('G'))


