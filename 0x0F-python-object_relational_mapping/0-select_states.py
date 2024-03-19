#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
    Your script should take 3 arguments: mysql username,
    mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running
    on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    curs = connection.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    data = curs.fetchall()
    for x in data:
        print(x)
