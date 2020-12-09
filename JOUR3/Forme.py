#coding:utf8

#classe Mère
class Forme:

    def __init__(self,point_origine, perimetre):
        self.point_origine = point_origine
    def calculerDistance(self):
        assert NotImplementedError('La classe fille doit implémenter la distance')
    def calculerPerimetre(self):
        assert NotImplementedError('La classe fille doit implémenter perimetre')        
    def afficher(self):

        return "{} \n{}\n".format(self.point_origine,self.perimetre)


#classe Filles
class Cercle(Forme):

    def __init__(self, rayon=1):
        super().__init__("cercle")
        self.__rayon = r
    def setRayon(self, r):
        self.__rayon = r
        return self.__rayon
    def getRayon(self):
         return self.__rayon
    def CalculerDistance(self):
        return r-point_origine 
    def CalculerPerimetre(self):
        return 2*pi*r

#classe filles
