import sqlite3
def connect_db():
    try:
        conn = sqlite3.connect('todo.db')
        db=conn.cursor()
        return conn,db
    except:
        return "Error In Connection !"
