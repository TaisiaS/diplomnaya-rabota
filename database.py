import sqlite3 

def get_spo():

    conn = sqlite3.connect('BDproject.db')

    cursor = conn.cursor()

    sql = "SELECT * FROM College"

    cursor.execute(sql)

    College = cursor.fetchall()
 
    print(College[0])

    conn.close()

    return College
get_spo()