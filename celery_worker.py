from celery import Celery
import sqlite3

celery = Celery(
    'tasks',
    broker='redis://localhost:6380/0'
)

@celery.task
def save_user(fn, ln):
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute("""
        INSERT INTO NAMES (First_Name, Last_Name)
        VALUES (?, ?)
    """, (fn, ln))

    con.commit()
    con.close()