import math 

class Fraction:
    def __init_(self, num, den):
        #validasi penyebut matematis
        if den == 0:
            raise ValueError("Denominator tak boleh 0")
        
        #pastikan penyebut selalu positif 
        if den < 0:
            num = -num
            den = -den

        #assign atribut class instance 
        self.num = num
        self.den = den 
        self._simplify()

    def _simplify(self)
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

        
    def _str_(self):
        return f"{self.num}/{self.den}"
    
    #output pengujian
    f = Fraction(1,2)
    print(f) #1/2 

    def add(self, other)
        #hitung pembilang (perkalian silang)

        