import sqlite3 as sql

with sql.connect("databese-3.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        ism TEXT,
        familiya TEXT,
        yosh INTEGER
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xarid (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        maxsulot_nomi TEXT,
        narx INTEGER
        )""")
    
    # Malumot kritish !
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh) 
                VALUES (1 , "Allamov", "Navro'zbek", 17)""") 
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh)
                VALUES (2 , "Madaminov", "Suhrob", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh)
                VALUES (3 , "Baydjayev", "Mulkamon", 17)""") 
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh)
                VALUES (4 , "Salimov", "Sarvar", 17)""") 
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh)
                VALUES (5 , "Madyarov", "Sarvar", 17)""") 
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, familiya, yosh)
                VALUES (6 , "Hakimberdiyev", "Sayitjon", 17)""") 


con.commit()
con.close()