#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from geometry import *
from matrix import *

colors = [(0.0,1.0,0.0,1.0),(0.0,0.0,1.0,1.0),(0.0,1.0,1.0,1.0),(1.0,1.0,1.0,1.0), 
            (1.0,1.0,0.0,1.0),(1.0,0.0,0.0,1.0),(1.000, 0.412, 0.706,1.0),(1.000, 0.388, 0.278, 1.0), 
            (0.780, 0.082, 0.522, 1.0),(1.000, 0.647, 0.000, 1.0),(1.000, 0.855, 0.725, 1.0),(0.902, 0.902, 0.980, 1.0),
            (0.282, 0.239, 0.545, 1.0),(0.498, 1.000, 0.000, 1.0),(0.957, 0.643, 0.376, 1.0),(1.000, 0.753, 0.796, 1.0),
            (0.000, 0.980, 0.604, 1.0), (0.000, 0.000, 0.502, 1.0), (0.961, 0.961, 0.863,1.0), (0.753, 0.753, 0.753,1.0)]


#basic cube - closed
def cube(vertex,faces):
	#glBegin(GL_QUADS)
	#print vertex
	for face in faces:
                glBegin(GL_QUADS)
                point_a = vertex[face[0]]
                point_b = vertex[face[1]]
                point_c = vertex[face[2]]
                normal_vector = calc_normal(point_a,point_b,point_c)
                glNormal3fv(normal_vector)
		for vert in face:
			glVertex3fv(vertex[vert])

#			
#			print (vertex[vert])
                glEnd()

#		
            	
	#		print (vertex[vert])
	#glEnd()

	return


def hedros(vertex,faces):

        n_faces = len(faces)
        for face in faces:
            index = faces.index(face)
            glColor4fv(colors[index])
            #if n_faces ==6:
            #    glBegin(GL_QUADS)            
            #else:
                #glBegin(GL_TRIANGLES)
            glBegin(GL_POLYGON)
        #print vertex
        #for face in faces:
            point_a = vertex[face[0]]
            point_b = vertex[face[1]]
            point_c = vertex[face[2]]
            normal_vector = calc_normal(point_a,point_b,point_c)
            glNormal3fv(normal_vector)
            for vert in face:
                glVertex3fv(vertex[vert])
#                       
        #               print (vertex[vert])
            glEnd()
        return

#abrir o cubo com glRotate e glTranslate
def opened_cube(vertex,faces,inicial_face,ang=90):
    DFS = depht_fs(graph_cube, inicial_face)
    #DFS[0] -> ordem de abertura das faces
    print DFS[0]
    DFS_faces_vector = create_face_vector(faces,DFS[0])
    print DFS_faces_vector
    #dfs_parents -> vizinhos
    dfs_parents = DFS[1]
    print dfs_parents
    
    
    #cria um array de matrizes identidades, uma para cada face do cubo
    faces_matrix = []
    for i in range(6):
        faces_matrix.append(identity())
    print faces_matrix


    for face in DFS_faces_vector:   
        

        index = DFS_faces_vector.index(face)

        if index>=2:
            break
        #face inicial não sofre transformação             
        if face!=DFS_faces_vector[0]:
                        
            #faces pai e filha
            pair = dfs_parents.pop(0)
            print pair            

            #Descobrir o Eixo de Rotação
            f1 = faces[pair[0]]
            f2 = faces[pair[1]]
            print f1
            point_a1 = vertex[f1[0]]
            print point_a1
            point_b1 = vertex[f1[1]]
            point_c1 = vertex[f1[2]]
            normal_vector1 = calc_normal(point_a1,point_b1,point_c1)
            print normal_vector1
            

            point_a2 = vertex[f2[0]]
            point_b2 = vertex[f2[1]]
            point_c2 = vertex[f2[2]]
            normal_vector2 = calc_normal(point_a2,point_b2,point_c2)
            print normal_vector2
            #print pair
            
            face_anterior = normal_vector1
            face_atual = normal_vector2
            cross_product = cross(face_atual,face_anterior)
            print cross_product

            #pegar as arestas das faces n e n-1
            i1=pair[0]
            i2=pair[1]
            edge = compare(faces[i1],faces[i2])
            #if not edge:
            #       edge = compare(DFS_faces_vector[index-2],DFS_faces_vector[index])
                                
            #glPushMatrix()
            print edge
            v1 = edge[0]
            v1 = vertex[v1]
            print v1
            v2 = edge[1]
            v2 = vertex[v2]
            print normal_vector2
            #difference(a,b) = ax - bx, ay - by, az - bz
                       
            vector = difference(v2,v1)
            vector = abs(vector)
            axis = [cross_product[0]*vector[0],cross_product[1]*vector[1],cross_product[2]*vector[2]]
            axis = Point(axis[0],axis[1],axis[2])
            print axis
            
            v1 = Point(v1[0],v1[1],v1[2])
            v2 = Point(v2[0],v2[1],v2[2])

            tr = translateAndRotate(ang,v1,axis)
            t = faces_matrix[i]*tr
            print 'faces'
            print faces_matrix[i]
            print t
            print type(t)   
            glMultMatrixf(t.view(type=np.ndarray))
        
        
        glColor4fv(colors[index])
        #desenha
           
    
        glBegin(GL_QUADS)
        #glBegin(GL_TRIANGLES)
        print "start drawing"
        for vert in face:
            print vert
            print vertex[vert]
                    
            glVertex3fv(vertex[vert])
        glEnd()
        




