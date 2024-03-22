#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username, mysql
password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3])

    cursor = db.cursor()
    sql_cmd = """SELECT cities
    FROM states
    INNER JOIN states=%s
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(sql_cmd, (argv[4],))
    cities = cursor

    for city in cities:
        print(city)

    cursor.close()
    db.close()
