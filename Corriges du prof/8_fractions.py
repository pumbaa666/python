def pgdc(a,b):
	while b:
		a,b = b, a % b
	return a

class Fraction:
	def __init__(self,num,denom=1):
		self.num = num
		self.denom = denom
		self.simplify()
		
	def __repr__(self):
		if self.denom != 1:
			return "%d/%d" % (self.num, self.denom)
		return "%d" % self.num
		
	def simplify(self):
		p = pgdc(self.num, self.denom)
		self.num /= p
		self.denom /= p
		
	def __mul__(self,other):
		return Fraction(self.num*other.num, self.denom*other.denom)
	
	def __add__(self,other):
		return Fraction(
			self.num*other.denom+ other.num*self.denom, 
			self.denom*other.denom)
			
	def __sub__(self,other):
		return Fraction(
			self.num*other.denom - other.num*self.denom, 
			self.denom*other.denom)
	
	def __neg__(self):
		return Fraction(-self.num,self.denom)

if __name__ == "__main__":
	f = Fraction(2,3)
	g = Fraction(3,4)
	print -f, g+f, g-f, g*f