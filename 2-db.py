import sqlite3 as sq

con = sq.connect("databese-2.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    gender INTEGER,
    name TEXT,
    score INTEGER,
    level INTEGER        
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS games (
    id INTEGER,
    user_id INTEGER,
    score INTEGER,
    time INTEGER
    )""")

cur.execute("""INSERT INTO users (id, gender, name, score, level) VALUES (1, 1, "Navro'zbek", 15, 79)""")


con.commit()
con.close()
