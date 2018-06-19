#!/usr/bin/python3
#
# "she-bang" line is a directive to the web server: where to find python
#
# filename: miniFacebook.py
# author: Carole (Chia Jung) Sung
# date: Apr 6 2018
# description: A simple version of the classic!
#


import MySQLdb as db    # the mysql database API 
import time
import cgi  
import cgitb; cgitb.enable()# web debugging package; always import it into your web apps

# print out the HTTP headers right away, before we do any other statements
print ("Content-Type: text/html")
print ()# blank line

################################################################################
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """   
    ## NOTE: You will need to specify your connection to the database
    # Your username is your BU username and your password is the
    # first four numbers of your BUID.
    # For example, if your BUID is 'U123-45-6789',
    # your password is set to be '1234' (no quotes). 
    # change the db name to use your username, e.g. cs108_azs_miniFB
    conn = db.connect(host="localhost",
                  user="carole07", 
                  passwd="6832",
                  db="cs108_carole07_miniFB")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print("""
    <html>
    <head>
    <title>%s</title>
    <body>
    <h1>%s</h1>

    <p>
    """ % (title, title))

################################################################################
def doHTMLTail():

    print("""
    <p>
    <hr>
    This page was generated at %s.<br>
    <a href="./miniFacebook2.py"> Return to main page.</a>
    </body>
    </html>

    """ % time.ctime())

################################################################################
def debugFormData(form):
    """
    A helper function which will show us all of the form data that was
    sent to the server in the HTTP form.
    """
    
    print ("""
    <h2>DEBUGGING INFORMATION:</h2>
    <p>
    Here are the HTTP form fields:

    <table border=1>
        <tr>
            <th>key name</th>
            <th>value</th>
        </tr>
    """)
    
    # form behaves like a python dict
    keyNames = form.keys()
    # note that there is no .values() method -- this is not an actual dict

    ## use a for loop to iterate all keys/values
    for key in keyNames:

        ## discover: do we have a list or a single MiniFieldStorage element?
        if type(form[key]) == list:

            # print out a list of values
            values = form.getlist(key)
            print ("""
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, str(values)))

        else:
            # print the MiniFieldStorage object's value
            value = form[key].value
            print ("""
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, value))
        
    print ("""
    </table>
    <h3>End of HTTP form data.</h3>
    <hr>
    """)
    
################################################################################
def getAllUsers():
    """
    Middleware function to get all users from the profiles table.
    Returns a list of tuples of (profileid, lastname, firstname).
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT profileID, lastname, firstname
    FROM profiles
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getAllUsers():

################################################################################
def getOneProfile(profileid):
    """
    Middleware function to retrieve one profile record from the database.
    Returns a list containing one tuple.
    """
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM profiles
    WHERE profileID=%s
    """

    # execute the query
    parameters = (int(profileid), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getOneProfile(profileid):


################################################################################
def showAllUsers(data):
    """
    Presentation layer function to display a table containing all users' lastnames
    and first names.
    """

    ## create an HTML table for output:
    print("""
    <h2>User List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """)
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (profileid, lastname, firstName) = row

        print("""
      <tr>
        <td><a href="?profileid=%s">%s</a></td>
        <td><a href="?profileid=%s">%s</a></td>
      </tr>
        """ % (profileid, lastname, profileid, firstName,))
        

    print("""
    </table>
    <p>
    <a href="?createNew=0">Add a new profile</a>
    <p>
    """)
    print("Found %d users.<br>" % len(data))

## end: def showAllUsers(data):
    

################################################################################
def showProfilePage(data):
    """
    Presentation layer function to display the profile page for one user.
    """

    ## show profile information
    (profileid, lastname, firstName, email, activities) = data[0]
    
    print("""
    <h2>%s %s's Profile Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>Email</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Activities</td>
            <td>%s</td>
        </tr>
    </table>
    <form>
        <input type="text" name="statusUpdate">
        <input type="hidden" name="profileID" value=%s>
        <input type="submit" name="Submit" value="Update Status">
    </form>
    """% (firstName, lastname, email, activities, profileid))

## end: def showProfilePage(data):
    
##########################################
    
def getStatusMessagesForUser(profileid):
    '''Connects to the database, run a query to select all status messages
    (including the timestamp) for the user identified by profileID, and return
    the list of records.'''

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM status
    WHERE profileID=%s
    """

    # execute the query
    parameters = (int(profileid), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

#################################

def showStatusMessagesForUsers(data):
    '''displays a series of status messages (and timestamps) for a single user.'''

    print("""
    <h2>Statuses</h2>
    <p>
    <table border=1>
    """)

    for row in data:

        # each iteration of this loop creates on row of output:
        (profileid, datetime, message) = row

        print("""
      <tr>
        <td>%s</td>
        <td>%s</td>
      </tr>
        """ % (datetime, message))
    
    print("""
    </table>
    """)
    
#################################
def postStatusMessage(profileID, message):
    '''create the SQL to insert a record to the status table.'''
    
    # connect to database
    conn, cursor = getConnectionAndCursor()
    tm=time.localtime()
    timestamp = '%04d-%02d-%02d %2d:%02d:%02d' % tm[0:6]
    # build SQL
    sql = """
    INSERT INTO status (profileID,datetime,message) VALUES (%s,%s,%s)
    """

    # execute the query
    parameters = (profileID,timestamp,message,)
    cursor.execute(sql,parameters)
    conn.commit()

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data
######################
def showAddProfileForm():
    '''Display an HTML form to add a new user.'''
    print("""

    <form>
    <table style="width:80%">
        <tr>
	    <td><b>Last Name:</b></td>
	    <td><input type="text" name="lastName"></td>
        </tr>
        <tr>
	    <td><b>First Name:</b></td>
	    <td><input type="text" name="firstName"></td>
        </tr>
        <tr>
	    <td><b>Email:</b></td>
	    <td><input type="text" name="email"></td>
        </tr>
        <tr>
	    <td><b>Activities:</b></td>
	    <td><input type="text" name="activities"></td>
        </tr>
        <tr>
            <td><input type="submit" name="createNewUser" value="Submit">
        </tr>
    </table>
    </form>""")

####################
def addProfile(lastname, firstname, email, activities):
    '''Middleware function which encapsulates the SQL to insert a new profile
    to the database.'''
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    INSERT INTO profiles (profileID,lastname,firstname,email,activities) VALUES (0,%s,%s,%s,%s)
    """

    # execute the query
    parameters = (lastname,firstname,email,activities,)
    cursor.execute(sql,parameters)
    conn.commit()

    # clean up
    conn.close()
    cursor.close()
    
    



################################################################################
if __name__ == "__main__":

    # get form field data
    form = cgi.FieldStorage()
    
    doHTMLHead("MiniFacebook")
    if "profileid" in form:
        # decision-logic to determine whether to show one profile,
        # or else show the list of all users.
        profileid = form["profileid"].value
        data = getOneProfile(profileid)
        showProfilePage(data)
        data = getStatusMessagesForUser(profileid)
        showStatusMessagesForUsers(data)
        
    elif "profileID" in form and "statusUpdate" in form:
        profileid = form["profileID"].value
        status = form["statusUpdate"].value
        postStatusMessage(profileid, status)
        data = getOneProfile(profileid)
        showProfilePage(data)
        data = getStatusMessagesForUser(profileid)
        showStatusMessagesForUsers(data)

    elif "createNew" in form:      
        showAddProfileForm()
    elif "lastName" in form and "firstName" in form and "email" in form and "activities" in form:
        last = form["lastName"].value
        first = form["firstName"].value
        email = form["email"].value
        activities = form["activities"].value
        addProfile(last,first,email,activities)
        data = getAllUsers()
        showAllUsers(data) 
    else:

    # default case: show all profiles
        data = getAllUsers()
        showAllUsers(data) 
        
        


    doHTMLTail()    





