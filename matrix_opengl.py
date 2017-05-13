from OpenGL.GL import *
from numpy import *

class Point(object):

	def __init__(self,x,y,z=0.0):
		self.x = x
		self.y = y
		self.z = z


def translateAndRotate(ang, p, axis):
	px = p[0]
	py = p[1]
	pz = p[2]

	axisX = axis[0]
	axisY = axis[1]
	axisZ = axis[2]

	#print p
	#print axis
	glPushMatrix()
	glLoadIdentity()
	glTranslate(px,py,pz)
	glRotate(ang,axisX,axisY,axisZ)
	glTranslate(-px,-py,-pz)
	T = glGetDoublev(GL_MODELVIEW_MATRIX)
	glPopMatrix()
	return T

def difference(arrayA,arrayB):
	arrayRx = arrayA[0]-arrayB[0]
	arrayRy = arrayA[1]-arrayB[1]
	arrayRz = arrayA[2]-arrayB[2]
	arrayR = [arrayRx,arrayRy,arrayRz]
	return arrayR

def compare(array1,array2):
	elements =[]
	for i in array1:
		for j in array2:
			if i==j:
				elements.append(i)
	return elements

def abs(vector):
	r =[]
	for i in vector:
		r.append(fabs(i))
	return r


def find_angle(v1,v2):
	vector =difference(v1,v2)
	abs_vector = abs(vector)
	#cos p = v.u/||v||.||u||
	vu = dot(vector,abs_vector)
	v = linalg.norm(vector)
	u = linalg.norm(abs_vector)
	print vu
	print v
	print u
	cos_p = vu/(u*v)
	return cos_p

