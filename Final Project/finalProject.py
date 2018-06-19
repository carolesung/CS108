#!/usr/bin/python3

# File: finalProject.py
# Name: Carole (Chia Jung) Sung
# Date: April 29 2018
# Description: Final project of CS108


import MySQLdb as db    # the mysql database API 
import time
import cgi  
import cgitb; cgitb.enable()# web debugging package; always import it into your web apps

# print out the HTTP headers right away, before we do any other statements
print ("Content-Type: text/html")
print ()# blank line

#Images
general = "https://image.flaticon.com/icons/svg/135/135763.svg"
vegetable = "https://image.flaticon.com/icons/svg/135/135715.svg"
meat = "https://image.flaticon.com/icons/svg/135/135628.svg"
dairy = "https://image.flaticon.com/icons/svg/135/135635.svg"
frozen = "https://image.flaticon.com/icons/svg/135/135581.svg"
other = "https://image.flaticon.com/icons/svg/135/135728.svg"
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
                  db="cs108_carole07_project")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print("""
    <html>
    <head>
    <title>Virtual Fridge</title>
    <body>
    <center>
    <p>
    <p>
    <h1><font size = +3" face = "verdana" >%s</font></h1>

    <p>
    """ % (title))

################################################################################
def doHTMLTail():

    print("""
    <p>
    <hr>
    <font face='verdana'>This page was generated at %s.</font><br>
    <font face='verdana'><a href="./finalProject.py"> Return to main page.</a></font>
    </center>
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
def homePage():
        
    #Presentation layer function to display a table containing all items in the fridge.
    # Create HTML table for output:
    
    print("""
    <p>
    <table>
        <tr>
            <td><img src="%s", width = "100", height = "100"></td>
            <td><font size = +1" face = "verdana" ><a href="?%s=0">Show All</a></font></td>
            <td></td>
            <td></td>
            <td><img src="%s", width = "100, height = "100"></td>
            <td><font size = +1" face = "verdana"><a href = "?%s=0">Dairy</a></font></td>
        </tr>
        <tr>
        </tr>
        <tr>
        </tr>
        <tr>
            <td><img src="%s", width = "100, height = "100"></td>
            <td><font size = +1" face = "verdana"><a href = "?%s=0">Vegetables</a></font></td>
            <td></td>
            <td></td>
            <td><img src="%s", width = "100, height = "100"></td>
            <td><font size = +1" face = "verdana"><a href = "?%s=0">Frozen</a></font></td>
        </tr>
        <tr>
        </tr>
        <tr>
        </tr>
        <tr>
            <td><img src="%s", width = "100, height = "100"></td>
            <td><font size = +1" face = "verdana"><a href = "?%s=0">Meat</a></font></td>
            <td></td>
            <td></td>
            <td><img src="%s", width = "100, height = "100"></td>
            <td><font size = +1" face = "verdana"><a href = "?%s=0">Other</a></font></td>
        </tr>
    </table>
        
    """ % (general, "general", dairy, "dairy", vegetable, "vegetable", frozen, "frozen", meat, "meat",other,"other"))
        

######################################
def getOneItem(itemID):
    """Middleware function to retrieve one item record from the database.
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT expiry_date, item_id, name, type
    FROM Fridge
    WHERE item_id=%s
    """

    # execute the query
    parameters = (int(itemID), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data
###################################
def getVegetables():
    """ 
    Middleware function to get vegetables from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge WHERE type = %s"""

    #execute query
    parameters = ("vegetable",)
    cursor.execute(sql,parameters)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
#####################################
def getMeat():
    """ 
    Middleware function to get meat from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge WHERE type = %s"""

    #execute query
    parameters = ("meat",)
    cursor.execute(sql,parameters)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
#####################################
def getDairy():
    """ 
    Middleware function to get dairy products from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge WHERE type = %s"""

    #execute query
    parameters = ("dairy",)
    cursor.execute(sql,parameters)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
#################################
def getFrozen():
    """ 
    Middleware function to get frozen products from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge WHERE type = %s"""

    #execute query
    parameters = ("frozen",)
    cursor.execute(sql,parameters)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
####################################
def getOther():
    """ 
    Middleware function to get other products from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge WHERE type = %s"""

    #execute query
    parameters = ("other",)
    cursor.execute(sql,parameters)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
######################################
def getAllItems():
    """ 
    Middleware function to get all items from the Fridge table.
    """

    #connect to database
    conn, cursor = getConnectionAndCursor()

    #build SQL
    sql = """SELECT expiry_date, item_id, name, type FROM Fridge"""

    #execute query
    cursor.execute(sql)

    #get data from database
    data = cursor.fetchall()

    #clean up
    conn.close()
    cursor.close()

    return data
#######################################
def showAllItems(data):
    """ 
    Presentation layer function to display a table containing all items in the fridge.
    """
    (expiry_date,item_id, name, t) = data[0]
    # Create HTML table for output:
    print("""
    <img src="%s", width = "450", height = "300">""" % general)

    print("""<p>
    <table border = 1>
            <tr>
                    <td><font size = +1" face = "verdana"><b>Item Name</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Expiry Date</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Type</b></font></td>
            </tr>
    """ )
    data = sorted(data)
    for row in data:
        # each iteration of this loop creates on row of output:
        (expiry_date,item_id, name, t) = row

        print("""
      <tr>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
      </tr>
      """ % (name, expiry_date, t,))

    print("""
    </table>
    <p>
    <font face = "verdana"><a href = "?addItemPage=0">Add Item</a></font>
    <font face = "verdana"><a href = "?editItemPage=0">Edit Item</a></font>
    <font face = "verdana"><a href = "?deleteItemPage=0">Delete Item</a></font>
    <p>
    """)


    print("<font face='verdana'>%d item(s) in the fridge.</font><br>" % len(data))
###########################################################################
def showDiffItems(data):
    """ 
    Presentation layer function to display a table containing all items in the fridge
    of a specific type.
    """
    (expiry_date, item_id, name, t) = data[0]
    # Create HTML table for output:

    if t == "vegetable":
        print("""<img src="%s", width = "450", height = "300">""" % vegetable)
    elif t == "meat":
        print("""<img src="%s", width = "450", height = "300">""" % meat)
    elif t == "dairy":
        print("""<img src="%s", width = "450", height = "300">""" % dairy)
    elif t == "frozen":
        print("""<img src="%s", width = "450", height = "300">""" % frozen)
    else:
        print("""<img src="%s", width = "450", height = "300">""" % other)
    print("""<p>
    <table border = 1>
            <tr>
                    <td><font size = +1" face = "verdana"><b>Item Name</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Expiry Date</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Type</b></font></td>
            </tr>
    """ )
    data = sorted(data)
    for row in data:
        # each iteration of this loop creates on row of output:
        (expiry_date, item_id, name, t) = row

        print("""
      <tr>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
      </tr>
      """ % (name, expiry_date, t,))
    print("""
    </table>
    <p>""")

    print("<font face='verdana'>%d item(s).</font><br>" % len(data))

############################################
def addNew():
    """ 
    Presentation layer function to allow users to add items into the fridge
    when it is empty.
    """
    print("""
    <p>
    <p>
    <form>
    <table>
        <tr>
            <td><input type = "text" name = "name" value = "New Item"></td>
            <td><select name= "type">
                <option value = "vegetable">Vegetable</option>
                <option value = "meat">Meat</option>
                <option value = "dairy">Dairy</option>
                <option value = "frozen">Frozen</option>
                <option value = "other">Other</option>
                </select></td>
            <td></td>
            <td><font face = "verdana">Expiry Date: </font></td>
            <td><input type = "date" name = "expiry"></td>
            <td><input type = "submit" name = "addNewItem" value = "Add Item"></td>

        </tr>
    </table>
    </form>  

    <p>
    """)
#############################################################
def editPage(data):
    """ 
    Presentation layer function to display a table containing all items in the fridge when user
    wants to edit items.
    """
    (expiry_date,item_id, name, t) = data[0]
    # Create HTML table for output:
    print("""
    <img src="%s", width = "450", height = "300">""" % general)

    print("""<p>
    <form>
    <table border = 1>
            <tr>
                    <td></td>
                    <td><font size = +1" face = "verdana"><b>Item Name</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Expiry Date</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Type</b></font></td>
            </tr>
    """ )
    data = sorted(data)
    for row in data:
        # each iteration of this loop creates on row of output:
        (expiry_date,item_id, name, t) = row

        print("""
      <tr>
        <td><input type = "radio" name = "item_id" value = "%d"></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
      </tr>
      """ % (item_id, name, expiry_date, t,))

    print("""
    </table>
    <p>
    <table>
        <tr>
            <td></td>
            <td></td>
            <td><input type="submit" name = "editItem" value = "Edit Item" </td>
            <td><input type="submit" name = "doneEdit" value = "Done" </td>
        </tr>
    </table
    </form>
    <p>
    <font face = "verdana"><a href = "?addItemPage=0">Add Item</a></font>
    <font face = "verdana"><a href = "?deleteItemPage=0">Delete Item</a></font>
    """)
####################################################
def editEntry(data):
    """
    Function called when user is editing an entry."""
    (expiry_date,item_id, name, t) = data[0]
    print("""
    <p>
    <p>
    <form>
    <table>
        <tr>
            <td><input type = "text" name = "name" value = {0!s}></td>
            <td><select name= "type">
                <option value = {1!s}>{2!s}</option>
                <option value = "vegetable">Vegetable</option>
                <option value = "meat">Meat</option>
                <option value = "dairy">Dairy</option>
                <option value = "frozen">Frozen</option>
                <option value = "other">Other</option>
                </select></td>
            <td></td>
            <td><font face = "verdana">Expiry Date: </font></td>
            <td><input type = "date" name = "expiry" value = {3!s}></td>
            <td><input type = "submit" name = "updateItem" value = "Update Item"></td>
            <td><input type = "hidden" name = "item_id" value = {4!s}></td>

        </tr>
    </table>
    </form>  

    <p>
    """.format(name, t, t, expiry_date,item_id))

####################################################
def updateEntry(item_id, name, t, expiry):
    '''Encapsulates the SQL to do an UPDATE query to modify the fridge.
    The update replaces the existing name and expiry date for the item
    record corresponding to item_id.'''

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    UPDATE Fridge 
    SET name=%s,
    type=%s,
    expiry_date=%s WHERE item_id = %s;"""
    

    # execute the query
    parameters = (name,t,expiry,item_id,)
    cursor.execute(sql,parameters)
    conn.commit()
    
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

############################################################
def deletePage(data):
    """ 
    Presentation layer function to display a table containing all items in the fridge when user
    wants to delete items.
    """
    (expiry_date,item_id, name, t) = data[0]
    # Create HTML table for output:
    print("""
    <img src="%s", width = "450", height = "300">""" % general)

    print("""<p>
    <form>
    <table border = 1>
            <tr>
                    <td></td>
                    <td><font size = +1" face = "verdana"><b>Item Name</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Expiry Date</b></font></td>
                    <td><font size = +1" face = "verdana"><b>Type</b></font></td>
            </tr>
    """ )
    data = sorted(data)
    for row in data:
        # each iteration of this loop creates on row of output:
        (expiry_date,item_id, name, t) = row

        print("""
      <tr>
        <td><input type = "radio" name = "item_id" value = "%d"></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
        <td><font face = "verdana">%s</font></td>
      </tr>
      """ % (item_id, name, expiry_date, t,))

    print("""
    </table>
    <p>
    <table>
        <tr>
            <td></td>
            <td></td>
            <td><input type="submit" name = "deleteItem" value = "Delete Item" </td>
            <td><input type="submit" name = "doneDelete" value = "Done" </td>
        </tr>
    </table
    </form>
    <p>
    <font face = "verdana"><a href = "?addItemPage=0">Add Item</a></font>
    <font face = "verdana"><a href = "?editItemPage=0">Edit Item</a></font>
    
    """)
####################################################
def addNewItem(name,t,expiry):
    '''Middleware function which encapsulates the SQL to insert a new item
    to the database.'''

    # connect to database
    conn, cursor = getConnectionAndCursor()
    tm = time.localtime()
    acquired = '%04d-%02d-%02d' % tm[0:3]
    # build SQL
    sql = """
    INSERT INTO Fridge (item_id,name,type,acquired_date,expiry_date) VALUES (0,%s,%s,%s,%s)
    """

    # execute the query
    parameters = (name,t,acquired,expiry,)
    cursor.execute(sql,parameters)
    conn.commit()

    # clean up
    conn.close()
    cursor.close()

############################################
def delete(item_id):
    """ 
    Allows users to remove an item from the database.
    """
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    DELETE FROM Fridge WHERE item_id in (%s)"""

    # execute the query
    parameters = (item_id,)
    cursor.execute(sql,parameters)
    conn.commit()
    
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()


#################################
if __name__ == "__main__":

    #get form field data
    form = cgi.FieldStorage()

    doHTMLHead("Welcome to your virtual fridge!")

    if "addNewItem" in form and "expiry" in form:
        name = form["name"].value
        t = form["type"].value
        expiry = form["expiry"].value
        addNewItem(name,t,expiry)
        data = getAllItems()
        showAllItems(data)

    elif "addItemPage" in form:
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
        else:
            showAllItems(data)
        addNew()

    elif "deleteItemPage" in form:
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
        else:
            deletePage(data)

    elif "editItemPage" in form:
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
        else:
            editPage(data)

    elif "editItem" in form:
        data = getAllItems()
        editPage(data)
        ID = form["item_id"].value
        data = getOneItem(ID)
        editEntry(data)

    elif "updateItem" in form:
        name = form["name"].value
        t = form["type"].value
        expiry = form["expiry"].value
        item_id = form["item_id"].value
        updateEntry(item_id,name,t,expiry)
        data = getAllItems()
        editPage(data)

    elif "doneEdit" in form:
        data = getAllItems()
        showAllItems(data)

    elif "doneDelete" in form:
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
        else:
            showAllItems(data)

    elif "general" in form:
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
            addNew()
        else:
            showAllItems(data)

    elif "vegetable" in form: 
        data = getVegetables()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have no vegetables in your fridge!</font>""")
        else:
            showDiffItems(data)

    elif "meat" in form:
        data = getMeat()
        if len(data) == 0:
            print("<font face = 'verdana'>You have no meat products in your fridge!</font>")
        else:
            showDiffItems(data)

    elif "dairy" in form:
        data = getDairy()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have no dairy products in your fridge!</font>""")
        else:
            showDiffItems(data)

    elif "frozen" in form:
        data = getFrozen()
        if len(data) == 0:
            print("<font face = 'verdana'>You have no frozen products in your fridge!</font>")
        else:
            showDiffItems(data)

    elif "other" in form:
        data = getOther()
        if len(data) == 0:
            print("<font face = 'verdana'>You have no products of this category!</font>")
        else:
            showDiffItems(data)

    elif "item_id" in form and "deleteItem" in form:
        item_id = form["item_id"].value
        delete(item_id)
        data = getAllItems()
        if(len(data)) == 0:
            print("""<font face = "verdana">You have nothing in your fridge!</font>""")
            addNew()
        else:
            deletePage(data)

    else:
    #default case: show all options
        homePage()

    doHTMLTail()
















