# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from cmath import *

#open a file
def loader(name):
#file name
#name = 'C:\Users\AndreaD\Desktop\cube.ply'
#name = 'cube.ply'

	print name
	try:
		file = open(name,"r")
		lines= file.readlines()
		#find the number of vertex
		vertex_line = lines[3]
		vertex_line = vertex_line.split()
		number_of_vertex = int(vertex_line[2])
		#print number_of_vertex
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
				#print n_vertex
				if(i<10+number_of_vertex):
					vertex.append(n_vertex)
				else:
					n_vertex.pop(0)
					faces.append(n_vertex)
					#print 'arestas'
					#print lines[i]
			
			i+=1
			
				#lineS = line.split()
				#for vertex in lines:
				#	print vertex
				#	#vertex=int(vertex)
				#	n_vertex=[]
				#	n_vertex.append(vertex)
				#print n_vertex
				#print lineS
		#print vertex
		#print faces
		face_line = lines[7]
		face_line = face_line.split()
		number_of_face = face_line[2]
		#print number_of_face
		#for line in lines:
		#data = {'number_of_vertex':number_of_vertex, 'number_of_face':number_of_face,'vertex': vertex,'faces':faces}
		return (number_of_vertex, number_of_face, vertex, faces)
		#return data	
		
	except IOError:
		print "Could not open file! Please, try again"

