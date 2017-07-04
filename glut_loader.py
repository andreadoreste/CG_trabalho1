# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from cmath import *

#open a file
def loader(name):
#file name
#name = 'cube.ply'

	try:
		file = open(name,"r")
		lines= file.readlines()
		#find the number of vertex
		vertex_line = lines[3]
		vertex_line = vertex_line.split()
		number_of_vertex = int(vertex_line[2])
		vertex = []
		faces =[]
		maximum = len(lines)
		i=0
		while (i<maximum):
			if (i>=10):
				
				linesS=lines[i].split()
				n_vertex =[]
				for l in linesS:
					if(i>=10+number_of_vertex):
						l=int(l)
					else:
						l=float(l)	
					n_vertex.append(l)
				if(i<10+number_of_vertex):
					vertex.append(n_vertex)
				else:
					n_vertex.pop(0)
					faces.append(n_vertex)
					
			i+=1
		face_line = lines[7]
		face_line = face_line.split()
		number_of_face = face_line[2]
		return (number_of_vertex, number_of_face, vertex, faces)
		
	except IOError:
		print "Could not open file! Please, try again"

