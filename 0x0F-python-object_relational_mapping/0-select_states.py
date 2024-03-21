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

    """
    Check if all required arguments are provided
    """
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    """
    Connect to MySQL server
    """
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            database=argv[3]
        )
        curs = connection.cursor()

        """
        Execute the SQL query
        """
        curs.execute("SELECT * FROM states ORDER BY id ASC")
        data = curs.fetchall()

        """
        Display results
        """
        for row in data:
            print(row)

        """
        Close cursor and connection
        """
        curs.close()
        connection.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        exit(1)
