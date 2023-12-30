from db import db
from flask import session
from sqlalchemy.sql import text

def get_all():
    sql=text("SELECT title, id, included FROM Pieces ORDER BY id")
    result=db.session.execute(sql).fetchall()
    return result

def get_by_id(id):
    sql=text("SELECT title, id FROM Pieces WHERE id=:id")
    result=db.session.execute(sql, {"id":id}).fetchone()
    return result

def add_new(name):
    sql=text("INSERT INTO Pieces (title, included) VALUES (:name, TRUE)")
    db.session.execute(sql, {"name": name})
    db.session.commit()

def hide(id):
    sql=text("SELECT included FROM Pieces WHERE id=:id")
    status=db.session.execute(sql, {"id":id}).fetchone()
    if status[0]:
        status=False
    else:
        status=True
    sql=text("UPDATE Pieces SET included=:status WHERE id=:id")
    db.session.execute(sql, {"status":status, "id":id})
    db.session.commit()

def delete(id):
    sql=text("DELETE FROM Pieces WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()

def update(id, name):
    sql=text("UPDATE Pieces SET title=:name WHERE id=:id")
    db.session.execute(sql, {"name":name, "id":id})
    db.session.commit()
