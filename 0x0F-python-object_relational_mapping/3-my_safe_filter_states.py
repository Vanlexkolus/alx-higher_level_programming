#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa
"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument. But
this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
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
    sql_cmd = """SELECT *
    FROM states
    WHERE name=%s ORDER BY id ASC"""

    cursor.execute(sql_cmd, (argv[4],))
    states = cursor

    for state in states:
        print(state)

    cursor.close()
    db.close()
