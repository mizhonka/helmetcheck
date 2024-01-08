from db import db
from flask import session
from sqlalchemy.sql import text

def get_links(id):
    sql=text("SELECT link, id FROM Links WHERE piece_id=:id")
    result=db.session.execute(sql, {"id":id}).fetchall()
    return result

def add(id, link):
    sql=text("INSERT INTO Links (piece_id, link) VALUES (:id, :link)")
    db.session.execute(sql, {"id": id, "link":link})
    db.session.commit()

def delete(id):
    sql=text("DELETE FROM Links WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()

def get_included_links():
    sql=text("SELECT L.link, P.title FROM Links L, Pieces P WHERE L.piece_id=P.id AND P.included=TRUE")
    result=db.session.execute(sql).fetchall()
    return result

def link_exists(id, link):
    sql=text("SELECT id FROM Links WHERE piece_id=:id AND link=:link")
    result=db.session.execute(sql, {"id":id, "link":link}).fetchone()
    if result:
        return True
    return False
