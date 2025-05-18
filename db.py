import sqlite3

def init_db():
    conn = sqlite3.connect("skillnest.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    is_premium INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()