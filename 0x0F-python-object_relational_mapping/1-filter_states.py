#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username,
    mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running
    on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
if __name__ == "__main___":
    from sys import argv
    import MySQLdb

    """
    Check if the num of args are 4
    """
    if len(argv) != 4:
        print("This module takes four args")
        exit(1)

    """
    Now we connect to the SQL server
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    curs = connection.cursor()
    """
    Now we execute SQL commands
    """
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = curs.fetchall()
    """
    Print the data
    """
    for row in data:
        print(row)
    """
    close cursor and connection
    """
    curs.close()
    connection.close()
