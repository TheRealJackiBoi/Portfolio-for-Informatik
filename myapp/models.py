from app import db

class Emne(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titel = db.Column(db.String(50), index = True, unique=True)
  resume = db.Column(db.String(300), index = True, unique=True)
  billed-path = db.Column(db.String(128))