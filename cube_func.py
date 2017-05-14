import sys
import os
import linecache
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *
#from geometry import *
#from matrix import *
#import matrix as c_matrix

from normal_vector import *
from glut_loader import *
from matrix_opengl import *
from graph_cg import *
#from geometry import *
#from matrix import *

colors = [(0.0,1.0,0.0,1.0),(0.0,0.0,1.0,1.0),(0.0,1.0,1.0,1.0),(1.0,1.0,1.0,1.0),(1.0,1.0,0.0,1.0),(1.0,0.0,0.0,1.0)]

def opened_cube(vertex,faces,initial_face, ang=90):
	
	#glLoadIdentity()

	#<DFS>

	#depth_fs returns an array
	#depth_fs[0] -> path 
	#depth_fs[1] -> neighbors
	DFS = depht_fs(graph_cube,initial_face)

	#faces vertex from the DFS path
	path = DFS[0]
	print path
	DFS_faces_vector = create_face_vector(faces,path)
	dfs_parents = DFS[1]
	print dfs

	#</DFS>

	#Create an array with an identity matrix for each face
	faces_matrix = []
	for i in range(6):
		faces_matrix.append(matrix(identity(4)))

	#Start drawing the faces
	face_i = path[0]	
	for face in DFS_faces_vector:
		
		glPushMatrix()	
		
		index = DFS_faces_vector.index(face)
		
		glColor4fv(colors[index])

		#Testing with only two faces
		#if index>=2:
		#	break
		#Doesn't need to apply any transformations at the first face
		if face!=DFS_faces_vector[0]:

			#Array pair = [face n-1, face n]
			pair = dfs_parents.pop(0)

			#face being modificated
			face_i = pair[1]
			face_prev = pair[0]
			#Array f1,f2 = faces[n]=[p1, p2, p3, p4]
			# Each p is a vertex of the face	
			f1 = faces[pair[0]]
			f2 = faces[pair[1]]

			#Calculate the normal array
			#point_x1 returns a array with the coordinates like [-1,1,1]
			point_a1 = vertex[f1[0]]

			# From a Array to a Point object
			#point_a1 = Point(point_a1[0],point_a1[1],point_a1[2])

			point_b1 = vertex[f1[1]]
			#point_b1 = Point(point_b1[0],point_b1[1],point_b1[2])

			point_c1 = vertex[f1[2]]
			#point_c1 = Point(point_c1[0],point_c1[1],point_c1[2])

			normal_vec_face_anterior = calc_normal(point_a1,point_b1,point_c1)
			print normal_vec_face_anterior

			point_a2 = vertex[f2[0]]
			#point_a2 = Point(point_a2[0],point_a2[1],point_a2[2])

			point_b2 = vertex[f2[1]]
            #point_b2 = Point(point_b2[0],point_b2[1],point_b2[2])

			point_c2 = vertex[f2[2]]
            #point_c2 = Point(point_c2[0],point_c2[1],point_c2[2])

			normal_vec_face_atual = calc_normal(point_a2,point_b2,point_c2)
			print normal_vec_face_atual

			cross_product = cross(normal_vec_face_atual,normal_vec_face_anterior)
			cross_product= cross_product.tolist()

			dot_product = dot(normal_vec_face_atual, normal_vec_face_anterior)
			print dot_product

			#Finding the edge
			edge = compare(f1,f2)

			point_1 = edge[0]
			point_1 = vertex[point_1]

			point_2 = edge[1]
			point_2 = vertex[point_2]

			edge_vector = difference(point_2,point_1)
			edge_vector = abs(edge_vector)
			print edge_vector
			
			axis = [cross_product[0]*edge_vector[0],cross_product[1]*edge_vector[1],cross_product[2]*edge_vector[2]]

			teste =dot(edge_vector,cross_product)
			print teste
			#if teste<0:
			#	ang = -ang
			#print "ang: " + str(ang)
			#print "f2: " + str(pair[1])
			tr = translateAndRotate(ang,point_1,axis)
			tr = matrix(tr)
			print 'type tr'
			print type(tr)
			print 'type m'
			print type(m)
			#comb = tr*m
			comb = tr*faces_matrix[face_prev]
			print "comb"
			print comb
			faces_matrix[face_i] = comb
			#print "tr"
			#print tr
			#glMultMatrixf(tr.view(type=ndarray))
			glMultMatrixf(comb.view(type=ndarray))
			#glMultMatrixf(faces_matrix[face_i])
		#glLoadIdentity()	
		
		
		
		#glColor4fv(colors[index])
		#glMultMatrixf(faces_matrix[face_i])
		
		#glColor4fv(colors[index])

		#desenha
		#glPopMatrix()
		glPushMatrix()
		glBegin(GL_QUADS)
		print "start drawing"

		for vert in face:
			glVertex3fv(vertex[vert])
			print vertex[vert]
		print "end drawing"
		
		glEnd()
		glPopMatrix()
		m = glGetDoublev(GL_MODELVIEW_MATRIX)
		m = matrix(m)
		
		
		print 'face_i: ' + str(face_i)
		print "m"
		print m
		#faces_matrix[face_i] = m

		glPopMatrix()
	#print 'faces_matrix'
	#print faces_matrix	
def main():
	results = loader('cube.ply')
	opened_cube(results[2],results[3],3)

if __name__ =='__main__':
	main()