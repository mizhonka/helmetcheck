from db import db
from flask import session
from sqlalchemy.sql import text

def get_links(id):
    sql=text("SELECT link FROM Links WHERE piece_id=:id")
    result=db.session.execute(sql, {"id":id}).fetchall()
    return [t[0] for t in result]

def add(id, link):
    sql=text("INSERT INTO Links (piece_id, link) VALUES (:id, :link)")
    db.session.execute(sql, {"id": id, "link":link})
    db.session.commit()
