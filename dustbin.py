'''
Represents nodes in the problem graph or network.
Locating coordinates can be passed while creating the object or they
will be assigned random values.
'''
from globals import *

class Dustbin:

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def __init__ (self, x = None, y = None):
		self.x = x
		self.y = y

		if y == None and x == None:
			self.y = random.randint(0, yMax)
			self.x = random.randint(0, xMax)




	# Returns distance to vertex passed in as arg
	def distanceTo(self, db):
		p = self.getX(), self.getY()
		q = db.getX(), db.getY()
		return math.dist(p,q)

	# Gives string representation of the Object with coordinates
	def toString(self):
		s = '(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
		return s

	# Check if coordinates have been assigned or not
	# Dustbins with (-1, -1) as coordinates are created during creation on chromosome objects
	def checkNull(self):
		if self.x == -1:
			return True
		else:
			return False
