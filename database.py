import sqlite3

def connect_db():
    conn = sqlite3.connect("data.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def insert_record(name, age, email):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO records (name, age, email) VALUES (?, ?, ?)", 
                   (name, age, email))
    
    conn.commit()
    conn.close()
