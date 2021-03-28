#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name, FROM cities INNER JOIN states\
                   ON cities.state_id = states.id WHERE states.name=%s\
                   ORDER BY cities.id ASC".format(sys.argv[4]))
    data = cursor.fetchall()
    count = 1
    for row in data:
        while count <= len(data):
            print("{}, ".format(row[0]), end="")
            count += 1
    print()
    cursor.close()
    db.close()
