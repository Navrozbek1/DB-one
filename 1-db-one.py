import sqlite3 as sq 

with sq.connect("databese-1.db") as con:
    cur = con.cursor()
    
    # Jadval yaratish!
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER
        )""")
    

    cur.execute("""INSERT OR IGNORE INTO userS (id, first_name, last_name, age)
                VALUES (1, 'Olovuddin', 'Olimov', 18)""")
    cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
                VALUES (2, 'Anavr', 'Davronov', 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
                VALUES (1, 1, 'Olma', 25000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
                VALUES (2, 2, 'Uzum', 15000)""")
    
con.commit()

print("="*50)

print(f"User jadavali foydalanuvchilari: ")
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)
    
print("="*50)

print(f"User jadavali foydalanuvchilari: ")
cur.execute("SELECT * FROM xaridlar")
for row in cur.fetchall():
    print(row)
    
print("="*50)