import sqlite3

con = None
cur = None

def connect_to_db():
    global con, cur
    
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS NAMES(
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL
        );
    """)
    print("Table ready")

def input_name(fn: str, ln: str):
    global cur, con
    
    if cur is not None:
        cur.execute(
            "INSERT INTO NAMES (First_Name, Last_Name) VALUES (?, ?)",
            (fn, ln)
        )
        con.commit()

def discon():
    global con
    
    if con is not None:
        con.close()