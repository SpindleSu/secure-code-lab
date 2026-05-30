import sqlite3

def login(usuario):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE name='{usuario}'")