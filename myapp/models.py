from app import db

class Emne(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titel = db.Column(db.String(50), index = True, unique=True)
  resume = db.Column(db.String(300), index = True, unique=True)
  billedpath = db.Column(db.String(128))


laering = Emne(titel="Læringsspil", resume="Vi skulle lave et læringsspil, med Scratch, til første klassere, og følge en iterativ udviklings metode.", billedpath="img/tal-spil.png")

all_emner = Emne.query.all()
print(all_emner)