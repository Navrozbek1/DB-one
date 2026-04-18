import sqlite3 as sql

with sql.connect("6-database.db") as con:
    cur = con.cursor()
    
    # Jadval yaratish !
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        ism TEXT,
        fam TEXT,
        yosh INTEGER
        )""")
    
    # Malumot qo'shish !
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (1, "Navro'zbek", "Allamov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (2, "Hechkim", "Hechkimov", 99999999)""")
    
    # Malumot yangilash !!!
    cur.execute("""UPDATE users SET yosh = 18 WERE id = 1""")
    
    # Malumot o'chirish !
    cur.execute("""DELETE FROM users WHERE ism = 'Navro''zbek'""")
    
    # Jadvallar o'chirish !
    cur.execute("""DROP TABLE IF EXISTS users""")
    
    # Hamma jadvallarni o'chirish ! 
    cur.execute("""DROP TABLE *""")
    
    
    
"""Ko'chirish mumkin emas !"""