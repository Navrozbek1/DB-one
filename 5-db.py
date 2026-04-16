import sqlite3 as sql

with sql.connect("databese-5.db") as con:
    cur = con.cursor()
    
    
    # FOYDALANUVCHILAR JADVALI
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        ism TEXT,
        fam TEXT,
        yosh INTEGER,
        )""")
    
    # TEXNIKALAR JADVALI 
    cur.execute("""CREATE TABLE IF NOT EXISTS texnikalar (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        t_nomi TEXT, 
        t_narxi INTEGER,
        )""")
    
    # (users) ga malumot qo'shish
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (1, "Navro'zbek", "Allamov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (2, "Muxamadsoli", "Rejabov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (3, "Sarvar", "Inayatov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (4, "Ozod", "Sultonov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (5, "Aminboy", "Familyasini_bilmiman", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (6, "Nizomiddin", "Atanyazov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (7, "Aziz", "Allaberganov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (8, "Javoxir", "Komiljonov", 17)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (9, "Javoxir", "Qodirov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO users (id, ism, fam, yosh)
                VALUES (10, "Javoxir", "Qodirov", 18)""")
    
    
    # (texnikalar) ga malumot qo'shish
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (1, 10, "Televizor", 2500000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (2, 9, "Kirmoshina",4500000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (3, 8, "Iphone 13 pro max",9000000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (4, 7, "Honor x9c",4000000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (5, 6, "Blendr", 500000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (6, 5, "Damas", 100_000_000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (7, 4, "Soq chiqargich", 400000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (8, 3, "Elektr arra",2000000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (9, 2, "Drel",1500000)""")
    
    cur.execute("""INSERT OR IGNORE INTO texnikalar (id, user_id, t_nomi, t_narxi)
                VALUES (10, 1, "Nokiya",300000)""")
    
con.commit()  # Tugadi!