import sys

class Matrix():
	def init(self, dimi, dimj):
		self.val = []
		self.dimi = dimi
		self.dimj = dimj
		for a in range(dimi):
			self.val += [[0]*dimj]

	def getI(self, i):
		return self.val[i]

	def get(self, i, j):
		return self.val[i][j]

	def __repr__(self):
		res = '\n'
		for i in range(len(self.val)):
			res += '[\t'
			for j in range(len(self.val[0])):
				res += str(self.val[i][j])
				res += '\t'
			res += ']\n'
		return res

	def set(self, i, j, n):
		self.val[i][j] = n

def emptyMatrix():
	dimi = int(raw_input("i dimension > "))
	dimj = int(raw_input("j dimension > "))
	matrix = Matrix()
	matrix.init(dimi, dimj)
	print
	print matrix

def newMatrix():
	i = int(raw_input('i > '))
	j = int(raw_input('j > '))
	return newMatrixIJ(i, j)

def newMatrixIJ(i, j):
	matrix = Matrix()
	matrix.init(i, j)
	for a in range(i):
		for b in range(j):
			matrix.set(a, b, int(raw_input('[%d, %d] > '%(a,b))))
	return matrix

def multMatrix(a, b):
	if a.dimj != b.dimi:
		return False
	res = Matrix()
	res.init(a.dimi, b.dimj)
	for ri in range(res.dimi):
		for rj in range(res.dimj):
			for n in range(b.dimi):
				res.set(ri, rj, res.get(ri, rj)+ (a.get(ri, n) * b.get(n, rj)))
	return res
def sumMatrix(a, b):
	if (a.dimi != b.dimi) or (a.dimj != b.dimj):
		return False
	res = Matrix()
	res.init(a.dimi, a.dimj)
	for i in range(a.dimi):
		for j in range(a.dimj):
			res.set(i, j, a.get(i, j) + b.get(i, j))
	return res

if __name__ == '__main__':
	mata = newMatrix()
	matb = newMatrix()
	print mata
	print matb
	print sumMatrix(mata, matb)
	print multMatrix(mata, matb)
