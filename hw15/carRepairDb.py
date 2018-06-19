#File: carRepairDB.py
#Author: Carole (Chia Jung) Sung
#Description: Demonstrate the python database API (DBAPI), i.e., writing and executing SQL queries from Python. This example uses an sqlite3 database file.
#
#Database API (DBAPI) objects we will use:
#Connection: The DBAPI Connection is an abraction of a connection to the DBMS.
#           It provides us with a Cursor object, and enables us to commit changes.
#
#Cursor:    The DBAPI Cursor object allows us to execute queries and obtain results

import sqlite3 as db

###########
def getDBConnectionAndCursor():
    '''This helper function establishes a connection to the database and returns
    connection and cursor objects.'''

    #connect to the database
    conn = db.connect('./cars.db')
    #obtain a cursor object
    cursor = conn.cursor()
    #return connection and cursor objects to calling context
    return conn, cursor

####################
def getAllCars():
    '''Connect to the database, exeute a SELECT query, and return the results of the query.'''
    #Obtain a database connection and cursor
    conn, cursor = getDBConnectionAndCursor()

    #Write the SQL
    sql = '''SELECT * FROM cars'''

    #Execute the SQL against the database curosr
    cursor.execute(sql)

    #read/process the result set from the database
    results = cursor.fetchall()

    #clean up
    cursor.close()
    conn.commit()
    conn.close()

    #return results
    return results
######################
def findCar(vin):
    '''Find a car in the database by matching the vin.'''
    # 1) Obtain a database connection and cursor
    conn, cursor = getDBConnectionAndCursor()
    
    # 2) Write some SQL
##    sql = ''' SELECT * FROM cars WHERE vin = %s''' % vin # SQL INJECTION VULNERABILITY
##
    sql = ''' SELECT * FROM cars WHERE vin = ?'''
    parameters = (vin,) #tuple containing parameters
    
    # 3) Execute the SQL against the database cursor
    cursor.execute(sql,parameters)
    
    # 4) Read/process the result set from the database
    results = cursor.fetchall()
    
    # 5) Clean up
    cursor.close()
    conn.commit()
    conn.close()
    
    # 6) Return results
    return results
#######################
def insertCar(vin, make, model, year, mileage):
    '''Insert a new car into the database.'''
    conn,cursor= getDBConnectionAndCursor()
    sql = '''INSERT INTO cars VALUES (?,?,?,?,?)'''

    parameters= (vin, make, model, year, mileage)
    
    cursor.execute(sql, parameters)
    
    rowcount = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()

    return rowcount
#######################
def main():
##
##    #delegate work to other functions as needed
##    results = getAllCars()
##    #print(results)
##    for row in results:
##        vin, year, make, model, mileage = row
##        print("%s %s (%s %s), %s miles" % (make, model, year, vin, mileage))
    records = findCar ('19UYA31581L986431')
    print (records)
    insertCar('1CZCT41JXMN1111999','2015','Chevrolet','Corvette','12345')
    results = getAllCars()
    for row in results:
        vin,year,make,model,mileage = row
        print("%s %s (%s %s), %s miles" % (make, model, year, vin, mileage))
        

main()

#General pattern for database API interactions
# 1) Obtain a database connection and cursor
# 2) write some SQL
# 3) Execute the SQL against the database cursor
# 4) 
