from db.DataBase import connect_db


def create_task(name,description):
    try:
        conn,db=connect_db()
        db.execute("insert into tasks (name,description) values(?,?)",
        (name,description))
        conn.commit()
        db.close()
        return True
    except:
        return Flase

def update_task(id,name,description):
    try:
        conn,db=connect_db()
        db.execute("update tasks set name=?,description=? where id=?",
        (name,description,id))
        conn.commit()
        db.close()
        return True
    except:
        return Flase

def delete_task(id):
    try:
        conn,db=connect_db()
        db.execute("delete from tasks where id=?",
        [id])
        conn.commit()
        db.close()
        return True
    except:
        return Flase

def get_all_task():
    try:
        conn,db=connect_db()
        query=db.execute("select id,name,description from tasks")
        data=query.fetchall()
        conn.commit()
        db.close()
        return data
    except:
        pass
def get_one_task(id):
    try:
        conn,db=connect_db()
        query=db.execute("select id,name,description from tasks where id=?",[id])
        data=query.fetchone()
        conn.commit()
        db.close()
        return data
    except:
        pass
