def pgdc(a,b):
    while b:
        a = b
        b = a%b
    return a

class Fraction:
    def __init__(self, numerateur, denominateur=1):
        self.numerateur = numerateur
        self.denominateur = denominateur
        self.reduire()
        
    def reduire(self):
        p = pgdc(self.numerateur, self.denominateur)
        self.numerateur /= p
        self.denominateur /= p

    def __repr__(self):
        return "%d/%d"% (self.numerateur, self.denominateur)