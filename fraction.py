def gcd(m,n):
    """
    Euclid's Algorithm
    
    """
    while m%n != 0:
        m,n = n,m%n
        
    return n

class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den) 

    ## Deep Equality : is (a/b) = (c/d) ?
    ## Sure, if ad = bc 
    def __eq__(self, other):
        lhs = self.num*other.den
        rhs = self.den*other.num      
        return lhs == rhs
        
    def __ne__(self, other):
        lhs = self.num*other.den
        rhs = self.den*other.num      
        return lhs != rhs   
    
    def __add__(self, other):
        numerator = self.num*other.den + other.num*self.den
        denominator = self.den*other.den
        common = gcd(numerator, denominator)
        return Fraction(numerator//common, denominator//common)
        
    def __sub__(self, other):
        numerator = self.num*other.den - other.num*self.den
        denominator = self.den*other.den
        common = gcd(numerator, denominator)
        return Fraction(numerator//common, denominator//common)
       
    def __mul__(self, other):
        numerator = self.num*other.num
        denominator = self.den*other.den
        common = gcd(numerator, denominator)
        return Fraction(numerator//common, denominator//common)
        
    def __truediv__(self, other):
        numerator = self.num*other.den 
        denominator = other.num*self.den
        common = gcd(numerator, denominator)
        return Fraction(numerator//common, denominator//common)
    
    def __lt__(self, other):
        diff = self - other         
        return diff.num < 0
        
    def __gt__(self, other):
        diff = self - other         
        return diff.num > 0
        
            
        

    
def main():
    
    newFraction1 = Fraction(5,6)
    newFraction2 = Fraction(4,6)
    newFractionAdded = newFraction1 + newFraction2
    print(newFractionAdded)
    print(newFraction1 == newFraction2)
    print(newFraction1 > newFraction2)
    print(newFraction1 < newFraction2)
        
main()    
        
