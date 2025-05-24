import sqlite3 

def get_spo(score):

    conn = sqlite3.connect('BDproject.db')

    cursor = conn.cursor()

    sql = f"SELECT * FROM College WHERE p_scores < {score};"
    print(sql)
    cursor.execute(sql)
    College = cursor.fetchall()

    conn.close()

    return College


def get_uni(score):

    conn = sqlite3.connect('BDproject.db')

    cursor = conn.cursor()

    sql = f"SELECT * FROM University WHERE p_scores < {score};"
    print(sql)
    cursor.execute(sql)

    University = cursor.fetchall()


    conn.close()

    return University
