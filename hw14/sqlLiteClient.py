# file: sqlLiteClient.py
# author: Aaron Stevens (azs@bu.edu)
#
# This program will allow us to interact with an sqlite3 database
# via a command prompt.
# At this time, we are not discussing HOW this program works.
# Just run it and type SQL commands at the prompt.
#
# 
import sqlite3 as db


class SQLLiteClient:

    def __init__(self, pathname):

        try:
            # check that the file name is valid. If not, print and error and exit
            f = open(pathname)
        except:
            print("The file %s was not found. Check that you have the correct file on disk." % pathname)
            self.validDB = False
            return
        
        self.conn = db.connect(pathname)
        self.cursor = self.conn.cursor()
        self.validDB = True
            
  
    def executeQuery(self, sql):

        try:
            self.cursor.execute(sql)
            
            # if a select query, show the results:
            if "SELECT" in sql.upper() or "PRAGMA" in sql.upper():

                data = self.cursor.fetchall()
                
                for row in data:
                    pattern = len(row) * "%s\t" 
                    print(pattern % row)

            # otherwise, show the row count
            else:

                print('%d rows were affected.' % self.cursor.rowcount)
                # commit the change to the database file so it is saved on disk
                self.conn.commit()
            
        except db.Error as e:
            print("An error occurred:", e.args[0])

        print('\n')

    
def main():

    pathname = './miniFB.db'
#    pathname = './cars.db'

    # create the SQLLiteClient object
    client = SQLLiteClient(pathname)

    if client.validDB:

        print("Welcome to the sqlLiteClient. Database file is: %s" % pathname)
        print()
        print("Type your commands at the prompt below. Hit enter to run the command. ")

        sql = ''
        while sql != 'quit' and sql != 'exit':

            print('''Enter your SQL or "quit" to quit.''')
            sql = input("")
            if "quit" != sql and 'exit' != sql:
                client.executeQuery(sql)
            
        print('Your database file %s has been updated. Goodbye!' % pathname)
        


main()

     
